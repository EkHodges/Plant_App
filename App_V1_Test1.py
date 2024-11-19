import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

pip install openai pillow
import os
from openai import OpenAI
from keys import open_ai_api_key


class PlantRecognitionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plant Recognition App")
        self.geometry("600x800")

        # Main Frame
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=1, fill="both", padx=10, pady=10)

        # Photo Upload Section
        photo_label = ttk.Label(main_frame, text="Upload a Plant Image:")
        photo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Label to display the uploaded image
        self.image_label = tk.Label(main_frame, bg="lightgray", width=60, height=15, relief="solid")
        self.image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Upload Button
        upload_button = ttk.Button(main_frame, text="Upload Image", command=self.upload_image)
        upload_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Plant Information Section (Scrollable)
        info_label = ttk.Label(main_frame, text="Plant Information:")
        info_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.plant_info_text = ScrolledText(main_frame, wrap="word", width=70, height=15)
        self.plant_info_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.plant_info_text.insert("1.0", "Plant information will appear here after photo recognition.")
        self.plant_info_text.config(state="disabled")  # Initially read-only

    def upload_image(self):
        """Handles image upload, analysis, and displaying the result."""
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if not file_path:
            return  # If the user cancels the file dialog

        # Display the uploaded image
        image = Image.open(file_path)
        image = image.resize((300, 300))  # Resize for display
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Send the image to OpenAI for analysis
        plant_info = self.identify_plant(file_path)

        # Display the information in the scrollable text box
        self.plant_info_text.config(state="normal")
        self.plant_info_text.delete("1.0", "end")
        self.plant_info_text.insert("1.0", plant_info)
        self.plant_info_text.config(state="disabled")

    def identify_plant(self, image_path):
        """Sends the image to OpenAI API for analysis and retrieves plant information."""
        try:
            # Open the image file
            with open(image_path, "rb") as image_file:
                response = openai.Image.create(
                    file=image_file,
                    purpose="describe_image"
                )

            # Process the response
            plant_description = response.get("data", [{}])[0].get("description", "No description available.")
            return f"Identified Plant Information:\n\n{plant_description}"

        except Exception as e:
            return f"An error occurred while identifying the plant: {str(e)}"


if __name__ == "__main__":
    app = PlantRecognitionApp()
    app.mainloop()