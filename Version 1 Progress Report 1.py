# Version 1 Progress Report 1


%pip install requests #this is causing a bug

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


##


#for searching

def main():
    print("Welcome to the Plant Identifier App!")
    
    while True:
        print("\nMain Menu:")
        print("1. Upload a plant photo for identification")
        print("2. Search for plants")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            photo_path = input("Enter the path to the plant photo: ")
            plant_info = identify_plant(photo_path)  # Assuming you already have this function
            if plant_info:
                print(f"Plant identified: {plant_info}")
        elif choice == "2":
            search_plants(plants_data)  # Call the search function
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Example plant data
plants_data = {
    "Rose": {"region": "Temperate", "toxicity": "Safe", "facts": "Roses are popular ornamental plants."},
    "Oleander": {"region": "Mediterranean", "toxicity": "Poisonous", "facts": "Oleander is highly toxic."},
    "Cactus": {"region": "Desert", "toxicity": "Safe", "facts": "Cacti are adapted to arid environments."}
}

# Run the app
main()

#for multi-criteria searches

def search_by_region_and_toxicity(plants_data, region, toxicity):
    results = {plant: info for plant, info in plants_data.items() 
               if info["region"].lower() == region.lower() and info["toxicity"].lower() == toxicity.lower()}
    return results if results else "No plants found matching those criteria."

#for fuzzy find searches

pip install rapidfuzz

from rapidfuzz import process

# Your plant data (example)
plants_data = {
    "Rose": {"region": "Temperate", "toxicity": "Safe", "facts": "Roses are popular ornamental plants."},
    "Oleander": {"region": "Mediterranean", "toxicity": "Poisonous", "facts": "Oleander is highly toxic if ingested."},
    "Cactus": {"region": "Desert", "toxicity": "Safe", "facts": "Cacti are adapted to survive in arid environments."}
}

# Function to perform fuzzy search
def fuzzy_search_plant_name(plants_data, search_name):
    plant_names = list(plants_data.keys())
    # Get the closest match to the user's input
    matches = process.extract(search_name, plant_names, limit=3, score_cutoff=50)
    
    if matches:
        print(f"Fuzzy Search Results for '{search_name}':")
        for match in matches:
            print(f"Found: {match[0]} with confidence {match[1]:.2f}%")
            # Display plant information
            print(plants_data[match[0]])
            print()
    else:
        print(f"No close matches found for '{search_name}'.")

# Example of using the fuzzy search
user_input = input("Enter plant name: ")
fuzzy_search_plant_name(plants_data, user_input)

Enter plant name: Ros
Fuzzy Search Results for 'Ros':
Found: Rose with confidence 90.00%
{'region': 'Temperate', 'toxicity': 'Safe', 'facts': 'Roses are popular ornamental plants.'}

#integrate fuzzy find into main search menu
def search_plants(plants_data):
    print("Search Options:")
    print("1. Search by plant name")
    print("2. Fuzzy search by plant name (partial matches)")
    print("3. Search by region")
    print("4. Search by toxicity (Safe/Poisonous)")
    
    choice = input("Choose an option (1/2/3/4): ")
    
    if choice == "1":
        plant_name = input("Enter plant name: ")
        result = search_by_name(plants_data, plant_name)
        print(result)
    elif choice == "2":
        fuzzy_name = input("Enter plant name (fuzzy search): ")
        fuzzy_search_plant_name(plants_data, fuzzy_name)
    elif choice == "3":
        region = input("Enter native region: ")
        result = search_by_region(plants_data, region)
        print(result)
    elif choice == "4":
        toxicity = input("Enter toxicity (Safe/Poisonous): ")
        result = search_by_toxicity(plants_data, toxicity)
        print(result)
    else:
        print("Invalid choice, please try again.")


##


#Using google reverse image search to get data
    #making the API request

import requests

# Set your Custom Search Engine ID and API Key here
CSE_ID = "your_cse_id_here"
API_KEY = "your_api_key_here"

# Function to search Google Images for a plant
def google_image_search(query):
    url = f"https://www.googleapis.com/customsearch/v1"
    
    params = {
        "q": query,  # Search query (plant name)
        "cx": CSE_ID,  # Custom Search Engine ID
        "key": API_KEY,  # API key
        "searchType": "image",  # Search type set to image
        "num": 3  # Number of results to return
    }

    # Make the request to the Google Custom Search API
    response = requests.get(url, params=params)

    if response.status_code == 200:
        search_results = response.json()
        if "items" in search_results:
            image_urls = [item['link'] for item in search_results['items']]
            return image_urls
        else:
            return "No results found."
    else:
        return f"Error: {response.status_code}"

# Example usage: Search for a Rose
query = "Rose plant"
image_results = google_image_search(query)

# Print the image URLs returned from Google
for idx, image_url in enumerate(image_results):
    print(f"Image {idx + 1}: {image_url}")

#integrate into app
def identify_plant_and_search_image(plant_name):
    # Get plant info (from your app's plant identification logic)
    plant_info = identify_plant(plant_name)  # Assuming you have this function
    
    if plant_info:
        print(f"Plant identified: {plant_name}")
        print(plant_info)

        # Perform a Google Image Search based on the identified plant name
        image_results = google_image_search(plant_name)

        # Display the top image results
        print("Related images:")
        for idx, image_url in enumerate(image_results):
            print(f"Image {idx + 1}: {image_url}")
    else:
        print("Plant not found.")