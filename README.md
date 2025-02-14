# Cosmic Microwave Background Data Compression Project

This project focuses on processing and compressing cosmic microwave background (CMB) data stored in `.FITS` format. The primary Python library used for handling and processing these images is Healpy. Healpy facilitates coordinate transformations between galactic, Ecliptic, and Equatorial reference frames.

## Problem Statement

High-resolution CMB images (with high NSIDE values in Healpy) pose significant challenges due to their substantial RAM memory requirements. This project aims to develop effective compression tools to mitigate the memory usage of these high-resolution images.

## Objectives

1. **Coordinate Transformation**: Utilize Healpy to transform coordinates between different reference frames (galactic, Ecliptic, and Equatorial).
2. **Compression Strategy**: Investigate and develop suitable compression strategies to reduce memory usage. The project explores two primary approaches:
   - Transform the `.FITS` image from galactic coordinates to Cartesian coordinates and apply squared compression.
   - Apply compression directly to the galactic coordinates and determine the optimal compression strategy for this approach.

## Current Status

The project is in the exploratory phase, where different compression paths are being evaluated to identify the most efficient method for reducing memory usage without compromising data integrity.

## Usage

To run the project, ensure you have the necessary dependencies installed, including Healpy and other required libraries. The main processing and compression scripts are contained within the Jupyter notebook [`healpix.ipynb`](healpix.ipynb).

## Files

- [`healpix.ipynb`](healpix.ipynb): Jupyter notebook containing the main code for processing and compressing CMB data.
- [`wmap_band_iqumap_r9_7yr_Ka_v4.fits`](wmap_band_iqumap_r9_7yr_Ka_v4.fits): Example `.FITS` file containing CMB data.
- [`wmap_projected.aqmp`](wmap_projected.aqmp): Example compressed file.

## Dependencies

- Healpy
- NumPy
- Matplotlib
- Other libraries as specified in the notebook

## Future Work

- Determine the best compression strategy through extensive testing and evaluation.
- Optimize the chosen compression method for performance and memory efficiency.
- Document the final compression process and provide usage guidelines.

For more details, refer to the code and comments within the [`healpix.ipynb`](healpix.ipynb) notebook.