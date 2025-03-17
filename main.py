import argparse
from healpix_processor import HealpixProcessor
from visualization import visualize_maps

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Compress and visualize HEALPix maps.")
    parser.add_argument("input_file", type=str, help="Path to the input HEALPix FITS file.")
    parser.add_argument("--output_h5", type=str, default="compressed_map.h5", help="Path to save the compressed HDF5 file.")
    parser.add_argument("--target_nside", type=int, default=1024, help="Target NSIDE for downsampling.")
    parser.add_argument("--dtype", type=str, default="uint16", choices=["uint8", "uint16", "float32"], help="Data type for quantization.")
    parser.add_argument("--visualize", action="store_true", help="Visualize the original and compressed maps.")
    args = parser.parse_args()

    # Initialize the HealpixProcessor
    processor = HealpixProcessor()

    # Compress the HEALPix map
    processor.compress_healpix(args.input_file, args.output_h5, args.target_nside, args.dtype)

    # Visualize if requested
    if args.visualize:
        original_map = processor.read_map(args.input_file)
        compressed_map, meta = processor.decompress_healpix(args.output_h5)
        visualize_maps(original_map, compressed_map, meta)

if __name__ == "__main__":
    main()