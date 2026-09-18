import argparse
import sys
from utils.file_io import FileIO
from core.detector import FaceDetector
from core.filters import AnonymizationFilters
from utils.logger import setup_logger

logger = setup_logger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="CLI Face Anonymization Tool")
    parser.add_argument("-i", "--input", required=True, help="Path to input image")
    parser.add_argument("-o", "--output", required=True, help="Path to save output image")
    parser.add_argument("-m", "--method", choices=['blur', 'pixelate'], default='blur', 
                        help="Anonymization method (blur or pixelate)")
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        logger.info(f"Processing input file: {args.input}")
        image = FileIO.read_image(args.input)
        detector = FaceDetector()
        faces = detector.detect_faces(image)
        if len(faces) > 0:
            if args.method == 'blur':
                processed_image = AnonymizationFilters.apply_gaussian_blur(image, faces)
            else:
                processed_image = AnonymizationFilters.apply_pixelation(image, faces)
        else:
            logger.info("No processing required. Returning original image.")
            processed_image = image
        FileIO.save_image(processed_image, args.output)
    except Exception as e:
        logger.error(f"Process failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
