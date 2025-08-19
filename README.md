# PCA-implementation
CA Implementation from Scratch in Python
This project demonstrates a step-by-step implementation of Principal Component Analysis (PCA) from scratch using Python and NumPy. It covers the fundamental steps of PCA, including data centring, covariance matrix computation, eigen decomposition, principal component selection, and data projection onto lower dimensions. The result is visualised using Matplotlib.

### Overview
PCA is a widely used dimensionality reduction technique that transforms high-dimensional data into a smaller set of variables (principal components) — capturing the most important variance patterns in the data. This project walks through the core mathematics and coding of PCA, providing a strong foundation for understanding how PCA works under the hood.

## What is PCA?
PCA transforms data to a new coordinate system.

The first principal component captures the greatest variance in the data.

Each subsequent component captures the next highest variance orthogonally.

PCA helps in visualisation, noise reduction, and feature extraction.

## How It Works
Centre the data: Subtract the mean from each feature to centre the data around zero.

Compute covariance matrix: Measure how features vary together.

Eigen decomposition: Calculate eigenvalues and eigenvectors of the covariance matrix.

Select principal components: Sort the eigenvalues and select the top components to retain.

Project data: Transform original data onto the selected principal components.

Visualise: Plot the reduced-dimensional data in 2D (or 3D).
