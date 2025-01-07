# Digital Image Processing Project

This repository contains projects for the Digital Image Processing course, covering a variety of image processing techniques and algorithms. Each project focuses on a unique aspect of image manipulation, analysis, and enhancement, implemented using custom Python code without third-party libraries.

## Table of Contents
1. [Project 1: Image Flipping and Chroma Keying](#project-1-image-flipping-and-chroma-keying)
2. [Project 2: Distortion and Correction](#project-2-distortion-and-correction)
3. [Project 3: Shape Counting and Compression](#project-3-shape-counting-and-compression)
4. [Project 4: Fourier Transform and Filtering](#project-4-fourier-transform-and-filtering)
5. [Project 5: Denoising and Advanced Filtering](#project-5-denoising-and-advanced-filtering)

---

### Project 1: Image Flipping and Chroma Keying
This project introduces basic image manipulation techniques:
1. **Image Flipping**: Flip images horizontally or vertically to reverse their orientation.
2. **Chroma Keying**: Replace green screen backgrounds in images with custom graphical backgrounds using Euclidean distance-based color replacement.

---

### Project 2: Distortion and Correction
This project focuses on image transformations and corrections:
1. **Barrel Distortion**: Apply radial distortion to images for a fisheye effect.
2. **Naive Correction**: Reverse distortion effects using inverse distortion functions.
3. **Correction with Interpolation**: Use advanced interpolation methods to improve correction accuracy.

---

### Project 3: Shape Counting and Compression
This project emphasizes image analysis and encoding:
1. **Shape Counting**: Analyze images to count geometric shapes (circles, squares, rectangles, and ellipses) using binary processing and blob-coloring.
2. **Compression**: Implement run-length encoding and decoding to compress and reconstruct binary images efficiently.

---

### Project 4: Fourier Transform and Filtering
This project explores frequency-domain techniques for image processing:
1. **DFT Computation**: Compute forward, inverse, and magnitude of Fourier transforms without using built-in libraries.
2. **Linear Filtering**: Apply Gaussian and Laplacian filters for spatial image enhancement.
3. **Frequency Domain Filtering**: Remove periodic noise from images using frequency-based filtering techniques.

---

### Project 5: Denoising and Advanced Filtering
This project addresses noise reduction and advanced filtering:
1. **Median Filter**: Remove noise by replacing pixel values with the median of their neighborhood.
2. **Arithmetic and Geometric Mean Filters**: Apply mean-based filters to smooth images.
3. **Adaptive Filters**: Use local noise characteristics to enhance image denoising capabilities.

---

### General Notes
- Follow the provided code structure.
- Do not modify critical files such as `requirements.txt`, `jenkinsfile`, or `dip.py`.
- Ensure compatibility with Jenkins CI/CD tests.

### License
This project is property of the Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston. 

