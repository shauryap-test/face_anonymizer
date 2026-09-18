## Problem Statement
In the era of mass data collection, protecting individual privacy in images is a growing challenge. Manually editing images to blur faces is time-consuming. There is a need for a lightweight, automated, scriptable tool to detect and anonymize faces programmatically.

## Scope of the Project
The project is scoped strictly to Computer Vision face detection for 2D static images (JPEG, PNG). It operates entirely via the command-line interface. The core pipeline reads an image, detects frontal faces, applies an anonymizing matrix transformation, and saves the output. 

## Target Users
- Data scientists looking to anonymize image datasets before training ML models.
- Backend engineers needing a fast script to process user-uploaded content.
- Individuals wanting to strip identities from photos before public sharing.

## High-Level Features
- Automated Frontal Face Detection.
- Interchangeable Filter Module (Gaussian Blur / Nearest-Neighbor Pixelation).
- Comprehensive command-line argument support.
- Centralized system logging for monitoring module execution.
