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
-	run main.py in the project root folder
-	keys.py should be used within .gitignore to run API keys securely
   example:

    	open_ai_api_key = "XXX" ; cloud_name ="XXXX" ; api_key = "XXXX" ; api_secret ="XXXX"


## Limitations
- Currently, there is no way for generated plant information to be saved within the app. Information output would need to be copied/pasted to an outside source if you want to keep any information it tells you.

