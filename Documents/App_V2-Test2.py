import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import requests
import openai
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import cloudinary
import cloudinary.uploader

from keys import open_ai_api_key, cloud_name, api_key, api_secret

class PlantIdentifierApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plant Identifier App")

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=1, fill='both')

        # Create frames for Photo Recognition and Plant Information
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)

        # Add frames to notebook
        self.notebook.add(self.frame1, text="Photo Recognition")
        self.notebook.add(self.frame2, text="Plant Information")

        # Frame 1: Upload Image and Display
        self.photo_label = ttk.Label(self.frame1, text="Upload a Plant Image:")
        self.photo_label.grid(row=0, column=0, padx=10, pady=10)

        self.image_label = tk.Label(self.frame1)
        self.image_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.upload_button = ttk.Button(self.frame1, text="Upload Image", command=self.open_image)
        self.upload_button.grid(row=0, column=1, padx=10, pady=10)

        # Frame 2: Display Plant Information
        self.plant_info_text = ScrolledText(self.frame2, width=40, height=10, wrap='word')
        self.plant_info_text.grid(row=0, column=0, padx=10, pady=10)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Open the image and display it
            img = Image.open(file_path)
            img.thumbnail((300, 300))  # Resize the image for display
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk

            # Upload the image to Cloudinary
            self.upload_to_cloudinary(file_path)

    def upload_to_cloudinary(self, image_path):
        try:
            # Upload the image to Cloudinary
            response = cloudinary.uploader.upload(image_path)
            image_url = response['url']  # Get the URL of the uploaded image
            print(f"Image URL: {image_url}")

            # Send the image URL to OpenAI for identification
            self.identify_plant(image_url)
        except Exception as e:
            messagebox.showerror("Error", f"Error uploading image: {str(e)}")

    def identify_plant(self, image_url):
        try:
            # Send a request to OpenAI with the image URL
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"Identify the plant from this image URL: {image_url}. Provide common name, scientific name, and care instructions.",
                temperature=0.7,
                max_tokens=150
            )
            
            # Extract and display plant details in the scrolled text area
            plant_info = response.choices[0].text.strip()
            self.display_plant_info(plant_info)
        except Exception as e:
            messagebox.showerror("Error", f"Error identifying plant: {str(e)}")

    def display_plant_info(self, plant_info):
        self.plant_info_text.delete(1.0, tk.END)  # Clear previous information
        self.plant_info_text.insert(tk.END, plant_info)  # Insert new plant information


if __name__ == "__main__":
    app = PlantIdentifierApp()
    app.mainloop()
