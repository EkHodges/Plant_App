# Version 1 Progress Report 1


pip install requests #this is causing a bug

import tkinter as tk
from tkinter import filedialog

#for uploading the photo block on home screen / test later with photos
    #purpose - Allow users to upload images
    #task - File/photo uploads (use TKInter)
    
def upload_photo():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

photo_path = upload_photo()
print(f"Photo uploaded: {photo_path}")


##


#for image processing and identification
    #purpose - process uploaded photo
    #task - Use API for plant identification

import requests

def identify_plant(photo_path):
    api_url = https://perenual.com/
    with open(photo_path, 'rb') as img_file:
        response = requests.post(api_url, files={'image': img_file})
    return response.json()

plant_info = identify_plant(photo_path)
print(plant_info)


#add API key: sk-sNxo66f4b6854b73b7007 (perenual.com)
import os

api_url = https://perenual.com/
api_key = os.getenv("sk-sNxo66f4b6854b73b7007")
headers = {'Api-Key': api_key}
response = requests.post(api_url, files=files, headers=headers)

##

#for data gathering using wikipedia
    #purpose - gather relative information about the plant one identified
    #task - gather data from web (could use machine learning for this?)

import wikipedia

def get_plant_info(plant_name):
    try:
        summary = wikipedia.summary(plant_name, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found for {plant_name}: {e.options}"
    except wikipedia.exceptions.PageError:
        return f"No information found for {plant_name}"

plant_name = "Rose"  # Replace with actual identified plant name
plant_details = get_plant_info(plant_name)
print(plant_details)


##


#for checking plant safety
    #purpose - determine if safe or poisonous
    #task - use database of toxic plants to cross-reference the plant identified is safe or not

#import csv - example of using a csv database
#would need ot gather small sample of poisonous plants for central ia to use for this project

def is_plant_poisonous(plant_name):
    with open('toxic_plants.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if plant_name.lower() in row[0].lower():
                return True
    return False
#a
poisonous = is_plant_poisonous(plant_name)
if poisonous:
    print(f"Warning: {plant_name} is poisonous!")
else:
    print(f"{plant_name} is safe.")
#b
print(f"Plant Name: {plant_name}")
print(f"Plant Information: {plant_details}")
if poisonous:
    print(f"Warning: {plant_name} is poisonous!")


##


#for user interaction and data display
    #purpose - present user with plant information
    #task - GUI output display

import tkinter as tk

def show_plant_info(plant_name, plant_info, is_poisonous):
    window = tk.Tk()
    window.title("Plant Info")

    tk.Label(window, text=f"Plant Name: {plant_name}").pack()
    tk.Label(window, text=f"Plant Info: {plant_info}").pack()
    if is_poisonous:
        tk.Label(window, text="Warning: This plant is poisonous!", fg="red").pack()

    window.mainloop()

# Example usage
show_plant_info(plant_name, plant_details, poisonous)


##


#error display

try:
    plant_info = identify_plant(photo_path)
except Exception as e:
    print(f"Error identifying the plant: {e}")