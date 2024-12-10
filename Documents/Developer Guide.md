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
   example:


## Planning Specs - Task Vignette

### 1.	User Input (photo search)

Carla finds a new plant she is unfamiliar with on a walk in the park by her new home. She uses the TAKE A PHOTO feature on the main screen of the app to take a photo of the plant. The app uses this image to generate the identifying information. A loading status bar appears on screen before text response appears.

Details for later:
 - The app could take a photo within the app OR have a image added from the phone’s gallery/photos folder

### 2.	Plant Identification

After the photo is added to the app, the identifying information appears on screen. Carla is able to find out the name of the plant, some basic features to help identify it, if the plant is poisonous or not, along with a longer, detailed description of the plant. 

The information appears as a category list that includes subheadings and the description below them for an organized reading experience. Colors may be used to differentiate the subheads from the body copy.

The screen includes a filter icon in the top right corner of the screen to ‘jump’ to specific information. Otherwise, the text field can be navigated by a scroll text feature.

Details for later:
 - Should this also mention a save icon if added later on?
 - Screen should include a thumbnail image of the original plant photo to use as reference


## Known Issues
Minor:
-	Currently, the app does not display correct plant information within the GUI display. The code has worked to export the information into the VS Code terminal, but does not show up on the intended text box.

Major;
-	The information that does display on the output text box shows the error “An error occurred while identifying the plant: name 'client' is not defined” which appears for both Upload Image and Enter URL actions. However, the debugger tool within VS Code does not display where the error occurs within the code.

## 
