## Plant Indicator App

# General Description:
This app will be an interactive way to explore native or local plants at a park in Ames, IA. The app will allow the user to search for native/local plants they encounter by using an image search. This app is intended to help those who are interested in the plants they encounter in their local environment but are unaware of plant specifics needed for a direct search, such as the plant or species names.

Since all of Central Iowa is located entirety within the USDA Hardiness Zone 5b, any plants found within Ames should result in the same native/local options, so users would be able to use this app at any of the parks in Ames or surrounding areas.

Once the user inputs the image of the plant they want to identify, the app will generate a data response that will include the identifying plant information such as the common plant name, species name, short description of general and planting information, if the plant poses any threat to the user, ect. This data will be generated using the Perenual API database and visuals will be generated with TKInter GUI.

Users will also be able to filter this data depending on specific information they are most interested in and could potentially ‘save’ or ‘favorite’ certain plant searches they want to look into further.

# Task Vignette:
1.	User Input (current location)

Carla is a new resident to Iowa and Ames more specifically. She recently moved here from West Texas and is curious about the different range of native plants Iowa has in comparison to the West Texas desert. 

She opens the app and inputs her updated location for better search results. Clicking on LOCATION she is able to input ‘Ames, Iowa’ into a search bar, and clicks SAVE button. Alternatively, she could enter the zip code instead.

Details for later:
o	Could this access the maps feature for geo-location?
o	Result could generate a basic map as the location page image after input


2.	User Input (photo search)

Carla finds a new plant she is unfamiliar with on a walk in the park by her new home. She uses the TAKE A PHOTO feature on the main screen of the app to take a photo of the plant. The app uses this image to generate the identifying information. A loading status bar appears on screen before text response appears.

Details for later:
o	The app could take a photo within the app OR have a image added from the phone’s gallery/photos folder


3.	Plant Identification

After the photo is added to the app, the identifying information appears on screen. Carla is able to find out the name of the plant, some basic features to help identify it, if the plant is poisonous or not, along with a longer, detailed description of the plant. 

The information appears as a category list that includes subheadings and the description below them for an organized reading experience. Colors may be used to differentiate the subheads from the body copy.

The screen includes a filter icon in the top right corner of the screen to ‘jump’ to specific information. Otherwise, the text field can be navigated by a scroll text feature.

Details for later:
o	Should this also mention a save icon if added later on?
o	Screen should include a thumbnail image of the original plant photo to use as reference

4.	Filter Search

Carla is pleased to see the detailed response the app generated for her, however, the information is quite lengthy. She is looking for the description of the plant but does not want to scroll through the entire page to find that section. 

She clicks the filter icon on the top right corner of the screen. A dropdown menu appears with the names of each category of information the results generated. She finds DESCRIPTION on the dropdown menu and clicks it. This ‘jumps’ the text to the short description category in the text field.

Details for later:
o	What other ways could the filter work?
	Reverse order
	Relevancy
•	But how would this be determined?

5.	Potentially: Save Search/Share

Carla likes the plant she found and is wanting to show it to her friend when she gets home from her walk. 

She clicks the SAVE icon (heart or star) to save it within the app to reference later. This way she can use the app multiple times throughout her walk as needed if she finds new plants to identify.

A box with a check mark inside and the text “Save Complete” below it appears on the screen briefly to confirm the search was saved, then disappears. The information is saved on another page within the app.

When accessing the new Save page, the saved content is listed in a list column view which can be clicked on to review all data. The list is made of rectangular boxes with the name of each plant centered within it. The boxes can be scrolled through and sorted alphabetically, or date/time added/saved. Carla can click on each box and a new screen will appear showing the results in the same manner it appeared on the initial search page. 

A SHARE icon appears in the top right corner next to the filter icon. Once clicked on, a pup up window appears that connects with sharing options (via social media sites, through contacts, or other).

Details for later:
o	This could be a good set up for the home screen as well
o	Should all icons be visible at the top even if the page is not developed?


 
# App Flow:
![image](https://github.com/user-attachments/assets/30d0672b-ac6e-48d9-a823-0e3d5662b8bf)

