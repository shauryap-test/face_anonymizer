import cv2
import os
from utils.logger import setup_logger

logger = setup_logger(__name__)

class FileIO:
    @staticmethod
    def read_image(file_path: str):
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"Cannot find {file_path}")
        image = cv2.imread(file_path)
        if image is None:
            logger.error(f"Failed to decode image: {file_path}")
            raise ValueError(f"Invalid image format: {file_path}")
        return image

    @staticmethod
    def save_image(image, output_path: str) -> bool:
        success = cv2.imwrite(output_path, image)
        if success:
            logger.info(f"Image successfully saved to {output_path}")
        else:
            logger.error(f"Failed to save image to {output_path}")
        return success
