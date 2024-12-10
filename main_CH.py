import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from openai import OpenAI
import requests
import cloudinary
import cloudinary.uploader

from keys import cloud_name, api_key, api_secret, open_ai_api_key
from io import BytesIO


class PlantRecognitionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plant Recognition App")
        self.geometry("600x950")

        # Main Frame
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=1, fill="both", padx=10, pady=10)

        # Image Upload or URL Section
        photo_label = ttk.Label(main_frame, text="Upload a Plant Image or Enter Image URL:")
        photo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w", columnspan=2)

        # Create image_frame
        image_frame = ttk.Frame(main_frame, width=400, height=400)
        image_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        image_frame.grid_propagate(False)  # Prevent frame from resizing

        # Configure grid for image_frame
        image_frame.grid_rowconfigure(0, weight=1)
        image_frame.grid_columnconfigure(0, weight=1)

        # Create and place image_label inside image_frame
        self.image_label = tk.Label(image_frame, bg="lightgray", relief="solid")
        self.image_label.grid(row=0, column=0, sticky="nsew")

        # Buttons for upload and URL
        upload_button = ttk.Button(main_frame, text="Upload Image", command=self.upload_image)
        upload_button.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        url_button = ttk.Button(main_frame, text="Enter URL", command=self.enter_url)
        url_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Plant Information Section (Scrollable)
        info_label = ttk.Label(main_frame, text="Plant Information:")
        info_label.grid(row=3, column=0, padx=10, pady=5, sticky="w", columnspan=2)

        self.plant_info_text = ScrolledText(main_frame, wrap="word", width=70, height=25)
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
 
            # run recognition on image, must be converted into cloudanary url first
            self.recognize_plant(file_path, None)
            

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
                response = requests.get(image_url)
                if response.status_code != 200:
                    messagebox.showerror("Error", "Invalid image URL. Please try again.")
                    return
                
                # display image
                image_data = BytesIO(response.content)
                self.display_image(image_data)

                # run recognition on URL
                self.recognize_plant(None, image_url)
            url_window.destroy()

        submit_button = ttk.Button(url_window, text="Submit", command=process_url)
        submit_button.pack(pady=10)

    def display_image(self, image_source):
        """Displays an uploaded image or URL image."""
        try:
            image = Image.open(image_source)
            image.thumbnail((400, 400))  # Create a thumbnail for display
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


    def upload_to_cloudinary(self, image_path):
        from keys import cloud_name, api_key, api_secret
        cloudinary.config(
                cloud_name = cloud_name,
                api_key = api_key,
                api_secret = api_secret
            )
        try:
            # Upload the image to Cloudinary
            response = cloudinary.uploader.upload(image_path)
            image_url = response['url']  # Get the URL of the uploaded image
            print(f"Image URL: {image_url}")
            return image_url

        except Exception as e:
            messagebox.showerror("Error", f"Error uploading image: {str(e)}")
            return None

    def recognize_plant(self, image_path=None, imageURL=None):
            from keys import open_ai_api_key

            # Display a message while processing
            self.display_plant_info("Working ...")
            self.update_idletasks()  # Force GUI to update
   
            # got a filename, upload to get a url
            if image_path is not None:
                image_url = self.upload_to_cloudinary(image_path)
                if image_url is None:
                    return   # Exit if image upload failed
            
            # got a URL
            if imageURL is not None:
                image_url = imageURL
            

    
            client = OpenAI(api_key=open_ai_api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                            {
                            "role": "user",
                                "content": [
                                {"type": "text", "text": "What type of plant is this? Identify its common name and scientific name for the species, growth habits, and care instructions. Output raw text instead of markdown."},
                                {
                                "type": "image_url",
                                "image_url": {
                                    "url": image_url,
                                },
                                },
                            ],
                            } 
                        ],
                temperature=0,
                max_tokens=300, # limit output to 300 tokens
            )

            self.display_plant_info(response.choices[0].message.content)


if __name__ == "__main__":
    app = PlantRecognitionApp()
    app.mainloop()