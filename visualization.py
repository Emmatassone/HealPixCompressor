import healpy as hp
import matplotlib.pyplot as plt

def visualize_maps(original_map, compressed_map, metadata):
    """Visualize original and compressed HEALPix maps side-by-side."""
    plt.figure(figsize=(16, 7))
    
    # Plot original map
    hp.mollview(original_map, 
                sub=(1, 2, 1),
                title=f"Original Map\nNSIDE={metadata['original_nside']}",
                unit='Temperature [μK]',
                min=np.nanmin(original_map),
                max=np.nanmax(original_map))
    
    # Plot compressed map
    hp.mollview(compressed_map, 
                sub=(1, 2, 2),
                title=f"Compressed Map\nNSIDE={metadata['current_nside']} ({metadata['dtype']})",
                unit='Temperature [μK]',
                min=np.nanmin(original_map),
                max=np.nanmax(original_map))
    
    plt.tight_layout()
    plt.show()