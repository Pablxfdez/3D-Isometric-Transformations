# Affine Isometric Transformation Project

## Introduction
This project focuses on affine isometric transformations applied to various systems with different numbers of state variables. The main objective is to visualize and manipulate objects in three dimensions using geometric transformations such as rotation and translation.

## Project Description
The practice involves applying concepts of affine isometric transformation, Euclidean metric, and calculations of diameter and centroid of a set of points. The project aims to generate animations that reproduce the simultaneous transformation of a rotation around the centroid of the system and a translation on the figure in 3D. This is achieved using rotation matrices and translation vectors, with values of t in the interval [0,1], representing the evolution of the transformation.

## Materials and Methods
The problem was approached using mathematical and geometrical principles, along with several Python libraries:

- **NumPy**: Used for handling matrices and vectors.
- **Matplotlib**: Employed for creating graphs, data visualization, and animations (FuncAnimation).
- **Scikit-image**: Utilized for loading the digital image 'arbol.png' and performing image processing operations.
- **Scipy-Spatial**: Applied for calculating the convex hull and the diameter of the set of points.
- **mpl_toolkits.mplot3d**: Used for generating an initial 3D figure.

The code is based on ideas provided by Robert in the template ‘GCOM2023-Practica4_plantilla’.

## Repository Contents

1. **FernandezdelAmoP_Practica4.pdf**
   - **Description**: This document provides a comprehensive overview of the project, including theoretical background, methodology, and explanation of the computational techniques used in the analysis.

2. **FernandezdelAmoP_Practica4.py**
   - **Description**: The Python script is the core of the project, containing the implementation of the affine isometric transformations on various systems. It includes the creation of animations to visualize the transformations.

3. **Hoja_arbol_limited1.gif**
   - **Description**: An animation showing the transformation of a system represented by the digital image 'arbol.png', focusing on the green leaf of the tree. This GIF illustrates the transformation with θ = 3π and v = (d,d,0), where d is the major diameter of the system.

4. **animacion_limited1.gif**
   - **Description**: This GIF animation showcases the transformation of a 3D figure from its initial state to its final state after undergoing simultaneous rotation and translation.

5. **README.md**
   - **Description**: The README file provides an overview of the repository, including a summary of the project, descriptions of the files contained within, and general information about the study's purpose and scope.

## Conclusion
This project demonstrates the application of affine isometric transformations in a Euclidean three-dimensional space. It highlights the utility of these transformations in image processing applications, such as analyzing the shape of leaves, to reduce differences in position and scale of system elements. The project successfully shows that affine isometric transformations are powerful tools for analyzing and processing systems in three-dimensional Euclidean space, enabling the creation of animations and visualizations for a better understanding of the studied systems.
