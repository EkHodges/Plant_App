# Plant Indicator App

This app is a simple plant identification tool that can utilize AI tools to identify images of plants either through a direct upload or from a URL. The primary use for this app would be to quickly identify a plant’s name or care instructions for educational or documentation purposes. The AI prompts can also be altered to produce new responses based on the user’s need. The documents folder contains the project sketch and project spec.

## Installation
-	Use pip to install the third-party packages
-	TKInter is used for GUI display
-	OpenAI is used for image interpretation
o	Make sure to install the most recent Open AI version to ensure the code runs properly
-	API keys from OpenAI and Cloudinary are needed to run this code
o	API keys should be saved in a keys.py file under .gitignore

## Usage
-	main.py: run in the project root folder
-	keys.py should be used within .gitignore to run API keys securely
-	test images are stored in the Images folder and can be accessed when the code is ran

## Code Examples
This project is meant to be ran with Python code. Here are some examples of the app’s features:

Uploading images 2 ways:
   
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


Use Open AI to identify the image:
      
      response = client.ChatCompletion.create(
          model="gpt-4",
          messages=[
          {"role": "system", "content": "You are a helpful plant expert."},
          {"role": "user", "content": prompt},
          ]

Display plan information in a scroll text box:
   
    def display_plant_info(self, info):
        """Displays the plant information in the scrollable text box."""
        self.plant_info_text.config(state="normal")
        self.plant_info_text.delete("1.0", "end")
        self.plant_info_text.insert("1.0", info)
        self.plant_info_text.config(state="disabled")


## Known Issues
-	Currently the app does not display correct plant information within on the GUI display. The code has worked to export the information into the VS Code terminal, but does not show up on the intended text box.
-	The information that does display on the output text box shows the error “An error occurred while identifying the plant: name 'client' is not defined” which appears for both Upload Image and Enter URL actions.
o	However, the debugger tool within VS Code does not display where the error occurs within the code.

