# Plant Indicator App Developer Guide

## Overview
This app is a simple plant identification tool that can utilize AI tools to identify images of plants either through a direct upload or from a URL. The primary use for this app would be to quickly identify a plant’s name or care instructions for educational or documentation purposes. The AI prompts can also be altered to produce new responses based on the user’s need.

### Installation
-	Use pip to install the third-party packages
-	TKInter is used for GUI display
-	OpenAI is used for image interpretation
      -	Make sure to install the most recent Open AI version to ensure the code runs properly
-	API keys from OpenAI and Cloudinary are needed to run this code

### Usage
-	run main.py in the project root folder
-	keys.py should be used within .gitignore to run API keys securely


## Planning Specs: Plant Identification

After the photo is added to the app, the identifying information appears on screen. User is able to find out the name of the plant, some basic features to help identify it, if the plant is poisonous or not, along with a longer, detailed description of the plant, etc. A thumbnail of the original image appears with the generated information.

User can input a photo of a plant for identification or add a URL from online.


## Code Examples
This project is meant to be ran with Python code. Here are some examples of the app’s features:

Uploading images 2 ways:
   
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


            """Send a request to OpenAI with the image URL"""
            response = openai.ChatCompletion.create(
                model="gpt-4",
                prompt=f"Identify the plant from this image URL: {image_url}. Provide common name, scientific name, and care instructions.",
                temperature=0.7,
                max_tokens=150
            )


Use Open AI to identify the image:
      
      def identify_plant(self, image_path=None, image_data=None):
        """Sends the image to OpenAI and retrieves plant information."""
        try:
            # Use image_path or image_data as input for further processing
            prompt = (
                "I am describing a plant for identification. "
                "Identify its name, species, growth habits, and care instructions. "
            )

Display plan information in a scroll text box:
   
    def display_plant_info(self, info):
        """Displays the plant information in the scrollable text box."""
        self.plant_info_text.config(state="normal")
        self.plant_info_text.delete("1.0", "end")
        self.plant_info_text.insert("1.0", info)
        self.plant_info_text.config(state="disabled")

## Limitations
- Currently, there is no way for generated plant information to be saved within the app. Information output would need to be copied/pasted to an outside source if you want to keep any information it tells you.


## Future iterations:
 - Ability to save generated information
 - Information can be shown in scroll text or list view / filtered by user
 - Colors can be added for effect or distinction
 - Users could take a photo within the app and use that for identification instead of uploading existing images
 - User could refine searches based on geolocation
