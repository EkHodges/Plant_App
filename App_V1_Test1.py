import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import cloudinary
import cloudinary.uploader
import openai
from tkinter.scrolledtext import ScrolledText
import platform
from keys import cloud_name, api_key, api_secret, open_ai_api_key  # Ensure keys.py is in .gitignore

class PlantIndicator(tk.Tk):
    def __init__(self, api_keys):
        super().__init__()
        self.title("Plant Indicator App")
        
        style = ttk.Style()
        print("Available themes:", style.theme_names())
        if platform.system() == 'Darwin':
            style.theme_use('aqua')
        else:
            style.theme_use('clam')
        style.configure('TNotebook.Tab', font=('Helvetica', 10, 'bold'), padding=[10, 5], background='lightblue')

        self.api_keys = api_keys
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=1, fill="both")

        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
        self.notebook.add(self.frame1, text="Photo Recognition")
        self.notebook.add(self.frame2, text="Plant Information")

        photo_label = ttk.Label(self.frame1, text="Upload a Plant Image:")
        photo_label.grid(row=0, column=0, padx=10, pady=10)

        self.image_label = tk.Label(self.frame1)
        self.image_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.plant_name_label = ttk.Label(self.frame1, text="")
        self.plant_name_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        upload_button = ttk.Button(self.frame1, text="Upload Image", command=self.open_image)
        upload_button.grid(row=0, column=1, padx=10, pady=10)

        self.plant_info_text = ScrolledText(self.frame2, wrap='word', width=40, height=6)
        self.plant_info_text.grid(row=0, column=0, padx=10, pady=10)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk
            self.recognize_plant(file_path)

    def recognize_plant(self, image_path):
        cloudinary.config(
            cloud_name=self.api_keys['cloud_name'],
            api_key=self.api_keys['api_key'],
            api_secret=self.api_keys['api_secret']
        )
        response = cloudinary.uploader.upload(image_path)
        image_url = response['url']
        
        openai.api_key = self.api_keys['open_ai_api_key']
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{
                "role": "user",
                "content": f"What type of plant is shown at this URL? {image_url} Please provide a text-only response."
            }],
            temperature=0,
            max_tokens=300
        )

        plant_info = response.choices[0].message['content']
        self.plant_info_text.insert("1.0", plant_info)

api_keys = {
    "cloud_name": cloud_name,
    "api_key": api_key,
    "api_secret": api_secret,
    "open_ai_api_key": open_ai_api_key
}

app = PlantIndicator(api_keys)
app.mainloop()