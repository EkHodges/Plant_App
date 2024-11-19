import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
#import cv2
import requests
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk  # This contains the self.notebook widget but is also has themed/styles widgets e.g. ttk.Button
import platform

# API configuration 
from keys import cloud_name, api_key, api_secret, open_ai_api_key   # make sure keys.py is you .gitignore!!!!

class PlantIndicator(tk.Tk):
    def __init__(self, api_keys):
        super().__init__()
        self.title("Plant Indicator App")
        #self.geometry("400x300")

       # optional: set some style elements
        style = ttk.Style()
        print("Available themes:", style.theme_names())

        # set the theme based on the platform
        if platform.system() == 'Darwin':  # macOS
            style.theme_use('aqua')  # Use the default macOS theme
        else:
            style.theme_use('clam')  # Use the 'clam' theme for other platform

        # Customize the self.Notebook tab style
        style.configure('TNotebook.Tab', 
                        font=('Helvetica', 10, 'bold'), 
                padding=[10, 5], 
                background='lightblue')
        
        self.api_keys = api_keys

        # Create a notebook (tab control)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=1, fill='both')


        # Create two self.frames (Photo Recognition and Plant Information)
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)

        # Add the self.frames to the self.notebook
        self.notebook.add(self.frame1, text="Photo Recognition")
        self.notebook.add(self.frame2, text="Plant Information")
        self.notebook.pack(expand=1, fill="both")


        # self.Frame 1: Photo Recognition
        photo_label = ttk.Label(self.frame1, text="Upload a Plant Image:")
        photo_label.grid(row=0, column=0, padx=10, pady=10)

        # Label to display the selected image
        self.image_label = tk.Label(self.frame1)
        self.image_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.plant_name_label = ttk.Label(self.frame1, text="")  # Initially empty
        self.plant_name_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)# self.

        upload_button = ttk.Button(self.frame1, text="Upload Image", command=self.open_image)
        upload_button.grid(row=0, column=1, padx=10, pady=10)


        # self.Frame 2: Plant Information
        self.plant_info_label = ttk.Label(self.frame2, text="Plant information will appear here after photo recognition.")
        self.plant_info_label.grid(row=0, column=0, padx=10, pady=10)


    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Open the image with Pillow and display it
            img = Image.open(file_path)
            img.thumbnail((300, 300))  # Resize for display purposes
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # Keep a reference

            # Recognize the plant from the image
            self.recognize_plant(file_path)

    def recognize_plant(self, image_path):
        print(image_path)
        # upload to cloudinary using self.api_keys['cloud_name'], self.api_keys['api_key'], self.api_keys['api_secret']
        # and get the image url

        # send the image url to OpenAI to recognize the plant an store the resulting string

        # add a textarea to frame2: ScrolledText(self.frame2, wrap='word', width=40, height=6)
        # write the recognition string to the textarea

        '''
        # Function to call the Perenual API and recognize the plant
        def recognize_plant(self, image_path):
            # Open the image file in binary mode
            with open(image_path, "rb") as image:   
                # Prepare the API request
                files = {"image": image}
                params = {"api_key": self.API_KEY}

                API_URL = "https://perenual.com/api/v2/plants"

                # Send the request to Perenual API
                response = requests.post(f"{API_URL}/identify", files=files, params=params)

                if response.status_code == 200:
                    data = response.json()
                    if data and data.get('data'):
                        # Extract plant info from the response
                        plant_name = data['data'][0]['common_name']  # Example field: common name
                        scientific_name = data['data'][0]['scientific_name']
                        care_level = data['data'][0].get('care_level', 'Not available')
                        light_level = data['data'][0].get('light', 'Not available')

                        # Display the plant information in the Plant Information self.frame
                        plant_info = f"Plant Name: {plant_name}\nScientific Name: {scientific_name}\nCare Level: {care_level}\nLight Level: {light_level}"
                        self.plant_info_label.config(text=plant_info)

                        # Update the plant name label under the image
                        self.plant_name_label.config(text=f"Plant Name: {plant_name}")
                    else:
                        self.plant_info_label.config(text="No plant recognized.")
                        self.plant_name_label.config(text="No plant recognized.")
                else:
                    self.plant_info_label.config(text=f"Error: {response.status_code}")
                    self.plant_name_label.config(text="Recognition failed.")
        '''

api_keys = {
    "cloud_name": cloud_name,
    "api_key": api_key,
    "api_secret": api_secret,
    "open_ai_api_key": open_ai_api_key
}

app =   PlantIndicator(api_keys) # make sure to pass the API key
app.mainloop()