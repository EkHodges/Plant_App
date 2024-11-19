import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import requests
import json
import openai

from keys import cloud_name, api_key, api_secret, open_ai_api_key

class PlantRecognitionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plant Recognition App")
        self.geometry("600x900")

        # Main Frame
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=1, fill="both", padx=10, pady=10)

        # Image Upload Section
        photo_label = ttk.Label(main_frame, text="Upload a Plant Image:")
        photo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w", columnspan=2)

        self.image_label = tk.Label(main_frame, bg="lightgray", width=60, height=20, relief="solid")
        self.image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for upload
        upload_button = ttk.Button(main_frame, text="Upload Image", command=self.upload_image)
        upload_button.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        # Plant Information Section
        info_label = ttk.Label(main_frame, text="Plant Information:")
        info_label.grid(row=3, column=0, padx=10, pady=5, sticky="w", columnspan=2)

        self.plant_info_text = ScrolledText(main_frame, wrap="word", width=70, height=15)
        self.plant_info_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.plant_info_text.insert("1.0", "Plant information will appear here after identification.")
        self.plant_info_text.config(state="disabled")

    def upload_image(self):
        """Handles image upload from the user's device."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if file_path:
            self.display_image(file_path)
            plant_data = self.identify_plant(file_path)
            self.display_plant_info(plant_data)

    def display_image(self, image_source):
        """Displays an uploaded image."""
        try:
            image = Image.open(image_source)
            image = image.resize((300, 300))  # Resize for display
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            self.display_plant_info(f"Error displaying image: {e}")

    def get_plant_details_from_openai(self, common_name, scientific_name):
        """Get detailed plant information using OpenAI."""
        try:
            prompt = (
                f"Provide detailed information about the plant {common_name} ({scientific_name}). "
                f"Include how it grows, care instructions, and any interesting facts."
            )
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a plant expert."},
                    {"role": "user", "content": prompt},
                ]
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error fetching details from OpenAI: {e}"

    def display_plant_info(self, info):
        """Displays the plant information in the scrollable text box."""
        self.plant_info_text.config(state="normal")
        self.plant_info_text.delete("1.0", "end")
        self.plant_info_text.insert("1.0", info)
        self.plant_info_text.config(state="disabled")


if __name__ == "__main__":
    app = PlantRecognitionApp()
    app.mainloop()
