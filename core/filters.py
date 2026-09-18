import cv2
import numpy as np

class AnonymizationFilters:
    @staticmethod
    def apply_gaussian_blur(image, blocks):
        output_img = image.copy()
        for (x, y, w, h) in blocks:
            roi = output_img[y:y+h, x:x+w]
            blurred_roi = cv2.GaussianBlur(roi, (99, 99), 30)
            output_img[y:y+h, x:x+w] = blurred_roi
        return output_img

    @staticmethod
    def apply_pixelation(image, blocks, blocks_num=10):
        output_img = image.copy()
        for (x, y, w, h) in blocks:
            roi = output_img[y:y+h, x:x+w]
            temp = cv2.resize(roi, (blocks_num, blocks_num), interpolation=cv2.INTER_LINEAR)
            pixelated_roi = cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
            output_img[y:y+h, x:x+w] = pixelated_roi
        return output_img
