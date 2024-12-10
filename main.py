import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from openai import OpenAI
import requests
from io import BytesIO

from keys import cloud_name, api_key, api_secret, open_ai_api_key


class PlantRecognitionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plant Recognition App")
        self.geometry("600x900")

        # Main Frame
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=1, fill="both", padx=10, pady=10)

        # Image Upload or URL Section
        photo_label = ttk.Label(main_frame, text="Upload a Plant Image or Enter Image URL:")
        photo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w", columnspan=2)

        self.image_label = tk.Label(main_frame, bg="lightgray", width=60, height=20, relief="solid")
        self.image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for upload and URL
        upload_button = ttk.Button(main_frame, text="Upload Image", command=self.upload_image)
        upload_button.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        url_button = ttk.Button(main_frame, text="Enter URL", command=self.enter_url)
        url_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Plant Information Section (Scrollable)
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
            plant_info = self.identify_plant(image_path=file_path)
            self.display_plant_info(plant_info)

    def enter_url(self):
        """Handles image upload via URL."""
        url_window = tk.Toplevel(self)
        url_window.title("Enter Image URL")
        url_window.geometry("400x150")

        url_label = ttk.Label(url_window, text="Enter Image URL:")
        url_label.pack(pady=5)
        url_entry = ttk.Entry(url_window, width=50)
        url_entry.pack(pady=5)

        def process_url():
            image_url = url_entry.get()
            if image_url:
                try:
                    response = requests.get(image_url)
                    response.raise_for_status()
                    image_data = BytesIO(response.content)
                    self.display_image(image_data)
                    plant_info = self.identify_plant(image_data=image_data)
                    self.display_plant_info(plant_info)
                except Exception as e:
                    self.display_plant_info(f"Error: Unable to process URL.\n{e}")
            url_window.destroy()

        submit_button = ttk.Button(url_window, text="Submit", command=process_url)
        submit_button.pack(pady=10)

    def display_image(self, image_source):
        """Displays an uploaded image or URL image."""
        try:
            image = Image.open(image_source)
            image = image.resize((300, 300))  # Resize for display
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            self.display_plant_info(f"Error displaying image: {e}")

    def identify_plant(self, image_path=None, image_data=None):
        """Sends the image to OpenAI and retrieves plant information."""
        try:
            # Use image_path or image_data as input for further processing
            prompt = (
                "I am describing a plant for identification. "
                "Identify its name, species, growth habits, and care instructions. "
            )

            # Send a request to OpenAI with the image URL
            response = openai.ChatCompletion.create(
                model="gpt-4",
                prompt=f"Identify the plant from this image URL: {image_url}. Provide common name, scientific name, and care instructions.",
                temperature=0.7,
                max_tokens=150
            )
            
            print(response.choices[0])
            
            # OpenAI API call
            response = client.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful plant expert."},
                    {"role": "user", "content": prompt},
                ]
            )

            # Extracting the content of the response
            plant_details = response["choices"][0]["message"]["content"]
            return plant_details

        except Exception as e:
            return f"An error occurred while identifying the plant: {str(e)}"


    def display_plant_info(self, info):
        """Displays the plant information in the scrollable text box."""
        self.plant_info_text.config(state="normal")
        self.plant_info_text.delete("1.0", "end")
        self.plant_info_text.insert("1.0", info)
        self.plant_info_text.config(state="disabled")


if __name__ == "__main__":
    app = PlantRecognitionApp()
    app.mainloop()