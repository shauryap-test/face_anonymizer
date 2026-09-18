# PrivacyGuard CLI: Face Detection & Anonymization Tool

## Overview
PrivacyGuard is a command-line interface (CLI) tool designed to detect human faces in images and anonymize them to protect privacy. It operates entirely without a GUI, offering quick, scriptable privacy protection for datasets or personal images.

## Features
- **Accurate Face Detection**: Utilizes OpenCV Haar Cascades for rapid bounding-box detection.
- **Multiple Anonymization Modes**: Choose between Gaussian blur and Pixelation.
- **CLI-First Architecture**: Easy to integrate into batch processing scripts or backend pipelines.
- **Robust Error Handling**: Safely validates file paths and image formats before processing.

## Technologies Used
- Python 3.10+
- OpenCV (cv2) for Computer Vision algorithms
- NumPy for array manipulation
- Argparse for command-line parsing

## Installation & Running
1. Clone the repository and navigate to the root directory.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the CLI tool:
   `python main.py -i input.jpg -o output.jpg -m pixelate`
   *(Options for `-m` are `blur` or `pixelate`)*

## Testing Instructions
1. Place a test image `test_image.jpg` with clear frontal faces in the root folder.
2. Run: `python main.py -i test_image.jpg -o test_blur.jpg -m blur`
3. Check the root folder for `test_blur.jpg` to verify successful anonymization.
4. Test error handling by passing a non-existent file: `python main.py -i fake.jpg -o output.jpg`
