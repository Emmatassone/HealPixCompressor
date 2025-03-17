import healpy as hp
import numpy as np
import h5py

class HealpixProcessor:
    def read_map(self, input_file):
        """Read a HEALPix map from a FITS file."""
        return hp.read_map(input_file)

    def compress_healpix(self, input_file, output_h5, target_nside=None, dtype="uint16"):
        """Compress a HEALPix map by downsampling and quantizing."""
        map_data = self.read_map(input_file)
        original_nside = hp.get_nside(map_data)
        
        if target_nside is not None:
            if target_nside >= original_nside:
                raise ValueError("target_nside must be smaller than original NSIDE")
            map_data = hp.ud_grade(map_data, target_nside)
            current_nside = target_nside
        else:
            current_nside = original_nside
        
        if dtype != "float32":
            map_min = np.nanmin(map_data)
            map_max = np.nanmax(map_data)
            scaled_data = (map_data - map_min) / (map_max - map_min)
            
            if dtype == "uint16":
                quantized = (scaled_data * 65535).astype(np.uint16)
            elif dtype == "uint8":
                quantized = (scaled_data * 255).astype(np.uint8)
            else:
                raise ValueError("Unsupported dtype. Use uint8/uint16/float32")
        else:
            quantized = map_data.astype(np.float32)
            map_min = map_max = None
        
        with h5py.File(output_h5, 'w') as f:
            dset = f.create_dataset('map', data=quantized, compression='gzip', compression_opts=9)
            dset.attrs['original_nside'] = original_nside
            dset.attrs['current_nside'] = current_nside
            if dtype != "float32":
                dset.attrs['min_val'] = map_min
                dset.attrs['max_val'] = map_max
            dset.attrs['dtype'] = dtype

    def decompress_healpix(self, input_h5):
        """Decompress a HEALPix map from an HDF5 file."""
        with h5py.File(input_h5, 'r') as f:
            dset = f['map']
            quantized = dset[:]
            metadata = {
                'original_nside': dset.attrs['original_nside'],
                'current_nside': dset.attrs['current_nside'],
                'dtype': dset.attrs['dtype']
            }
            if metadata['dtype'] != 'float32':
                metadata['min_val'] = dset.attrs['min_val']
                metadata['max_val'] = dset.attrs['max_val']
        
        if metadata['dtype'] == 'uint16':
            scaled = quantized.astype(np.float32) / 65535
        elif metadata['dtype'] == 'uint8':
            scaled = quantized.astype(np.float32) / 255
        else:
            return quantized, metadata
        
        reconstructed = scaled * (metadata['max_val'] - metadata['min_val']) + metadata['min_val']
        reconstructed[quantized == 0] = np.nan  # Preserve NaN values
        return reconstructed, metadata