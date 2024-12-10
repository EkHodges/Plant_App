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


## Known Issues
Minor:
-	Currently, the app does not display correct plant information within the GUI display. The code has worked to export the information into the VS Code terminal, but does not show up on the intended text box.

Major:
-	The information that does display on the output text box shows the error “An error occurred while identifying the plant: name 'client' is not defined” which appears for both Upload Image and Enter URL actions.


## Future iterations:
 - Ability to save generated information
 - Information can be shown in scroll text or list view / filtered by user
 - Colors can be added for effect or distinction
 - Users could take a photo within the app and use that for identification instead of uploading existing images
 - User could refine searches based on geolocation
