import numpy as np
import cv2
import pytesseract
import datetime

def perform_ocr(image_path, tesseract_cmd, output_folder):
    """
    Function to perform OCR on an image and save the output to a text file.

    :param image_path: Path to the image file.
    :param tesseract_cmd: Path to the Tesseract executable.
    :param output_folder: Folder where the output text file will be saved.
    """
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    # Reading of image
    image = cv2.imread(image_path)
    if image is None:
        print('Could not open or find the image.')
        return

    # Contrast enhancement
    alpha = 1.4 # contrast control
    beta = 0    # brightness control
    new_image = np.zeros(image.shape, image.dtype)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y, x, c] = np.clip(alpha * image[y, x, c] + beta, 0, 255)

    # Grayscaling contrasted image
    gray_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

    # Tesseract configuration and OCR
    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(gray_image, config=config)

    # Generate a unique filename using the current date and time
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_name = f'output_{current_time}.txt'
    output_file_path = f'{output_folder}\\{output_file_name}'

    # Write the OCR result to a text file
    with open(output_file_path, 'w') as file:
        file.write(text)

    # Print a confirmation message
    print(f"OCR output written to {output_file_path}")

# Example usage
perform_ocr('C:/Users/ITSC27/Downloads/camscanner-10971-1.jpg', 
            'C:\\Users\\ITSC27\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe', 
            'C:\\Users\\ITSC27\\Desktop\\Project')
