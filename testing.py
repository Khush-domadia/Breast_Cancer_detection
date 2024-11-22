import os

import cv2 as cv
import numpy as np
from keras.models import load_model

folder_path = "base/static/adminResourses/upload_image/"
output_folder_zero = "base/static/adminResourses/output/zero/"
output_folder_one = "base/static/adminResourses/output/one/"

model = load_model('base/service/model/Brest CNN 2.h5')


# def draw_highlight(image, mask, color):
#     highlighted_image = image.copy()
#     mask_resized = cv.resize(mask, (image.shape[1], image.shape[0]))  # Resize mask to match image size
#     _, thresh = cv.threshold(mask_resized, 0.5, 255, cv.THRESH_BINARY)
#     contours, _ = cv.findContours(thresh.astype(np.uint8), cv.RETR_EXTERNAL,
#                                   cv.CHAIN_APPROX_SIMPLE)
#     for contour in contours:
#         x, y, w, h = cv.boundingRect(contour)
#         cv.rectangle(highlighted_image, (x, y), (x + w, y + h), color, 2)
#     return highlighted_image


def image_classification():
    status_list = []  # Initialize an empty list to store status for each image

    try:
        # Get the latest image from the folder
        img_list = os.listdir(folder_path)
        latest_image = max(img_list, key=lambda x: os.path.getmtime(
            os.path.join(folder_path, x)))

        img_path = os.path.join(folder_path, latest_image)
        img = cv.imread(img_path, cv.IMREAD_COLOR)

        if img is None:
            print(f"Failed to load image: {latest_image}")
            status_list.insert(0, "Failed to load image")  # Insert at 0 index
            return "Failed to load image"

        img_size = cv.resize(img, (50, 50), interpolation=cv.INTER_AREA)
        img_size = np.expand_dims(img_size, axis=0)
        predictions = model.predict(img_size)

        if predictions.ndim != 2 or predictions.shape[1] < 2:
            print(f"Invalid predictions for image: {latest_image}")
            status_list.insert(0, "Invalid predictions")  # Insert at 0 index

        Y_pred_classes = np.argmax(predictions, axis=1)
        print(f"Predicted class: {Y_pred_classes}")

        if Y_pred_classes == 0:
            output_path = os.path.join(output_folder_zero, latest_image)
            cv.imwrite(output_path, img)
            print(f"Image classified as class 0: {latest_image}. Saved to {output_path}")
            status_list.insert(0, "Less probability for Cancer")  # Insert at 0 index
        elif Y_pred_classes == 1:
            output_path = os.path.join(output_folder_one, latest_image)
            cv.imwrite(output_path, img)
            print(f"Image classified as class 1: {latest_image}. Saved to {output_path}")
            status_list.insert(0, "High probability for Cancer")  # Insert at 0 index
        else:
            print(f"No action defined for class {Y_pred_classes} prediction for image: {latest_image}")
            status_list.insert(0, "No action defined")  # Insert at 0 index

    except Exception as e:
        print(f"Error occurred during image classification: {e}")
        return []

    print("Images with highlighted areas saved successfully.")
    print(status_list)
    return status_list[0]  # Returning the latest status
