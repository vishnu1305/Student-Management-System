import os
import pymongo
from PIL import Image
from tkinter import filedialog
import tkinter as tk
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Connect to MongoDB
uri = "mongodb+srv://sxcmt:sxcmt@sxcmt.uvrp8pj.mongodb.net/?retryWrites=true&w=majority&appName=SXCMT"
client = MongoClient(uri, server_api=ServerApi('1'))   
db = client["userdb"]
collection = db["image"]

# Function to upload photos from a folder to MongoDB
# def upload_photos(folder_path):
#     for filename in os.listdir(folder_path):
#         if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
#             with open(os.path.join(folder_path, filename), "rb") as f:
#                 photo_data = f.read()
#             photo_document = {"filename": filename, "data": photo_data}
#             print(photo_document)
#             collection.insert_one(photo_document)

#     print("great success")


def convert_to_jpeg(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to JPEG format
    if img.mode != "RGB":
        img = img.convert("RGB")

    return img

def upload_photos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            # Convert to JPEG format
            img = convert_to_jpeg(os.path.join(folder_path, filename))

            # Save the image to a temporary file
            temp_jpeg_file = os.path.splitext(filename)[0] + ".jpeg"
            temp_jpeg_path = os.path.join(folder_path, temp_jpeg_file)
            img.save(temp_jpeg_path, "JPEG")

            # Read the JPEG file and upload it to MongoDB
            with open(temp_jpeg_path, "rb") as f:
                photo_data = f.read()
            photo_document = {"filename": temp_jpeg_file, "data": photo_data}
            collection.insert_one(photo_document)

            # Delete the temporary JPEG file
            # os.remove(temp_jpeg_path)

    print("great success")



# Function to retrieve a photo by filename
def retrieve_photo(filename):
    photo_document = collection.find_one({"filename": filename})
    print(filename)
    if photo_document:
        # Extract file extension from filename
        _, file_extension = os.path.splitext(filename)
        

        
        current_directory = os.getcwd()

        if True:
    # Construct the absolute path to the directory where you want to save the images
            save_directory = os.path.join(current_directory, "Assests/Images/")
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)  # Create the directory if it doesn't exist

            # Construct the absolute file path for saving the image
            save_path = os.path.join(save_directory, filename)
            with open(save_path, "wb") as f:
                f.write(photo_document["data"])
            print(f"Photo saved to: {save_path}")
            return True
        else:
            print("Save operation canceled.")
            return False
    else:
        print("Photo not found.")
        return False

# Example usage:
# Upload photos from a folder
# upload_photos("D:/picture/New folder")

# Retrieve a photo by filename
# retrieve_photo("BCA2022001.jpeg")
