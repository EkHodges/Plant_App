# Title: Local Plant Indicator 

## Description:
    This app will be an interactive way to explore local plants at an Ames park. The app will allow the user to search for local plants using an image search in which the app will     generate a data response that may include plant information such as the plant name, species name, a short description of general information about the plant, zone information. Users will also be able to filter this data depending on specific information they are most interested in. 

## Users:
    The primary use for this app would be targeted to people who want to connect with their local flora species and learn more about plants in their area. The secondary use would be for education and would inform users who are interested in learning about native plants.

## Problem to Help Solve:
    This app would help interested users find and identify local and native plants in Ames. By using an image search within a refined search zone, this app can provide users with a quick and precise identification process based on their current location.

## Work Path:
    -	User will choose an area they want to explore or can access their exact location using map data (i.e. a local park in Ames)
    
    -	User will add image of plant they want to learn more about
                - Source images will be pre-collected based on location and can be used in root file as references for Google Reverse Image search via python code to gather information through API database
                
    -	The app would generate a list of information about the specific plant
    
    -	User can further filter search results depending on what they are most interested in
    
    -	(?) General URL that links to an online search (not sure if this is possible, but could be helpful)

## Data Utilized:
    -	Data will be gathered/used from Perenual API (https://perenual.com/docs/api) which will provide the plant identification information (up to 100 API requests/day)
    
    -	Images can be linked to Google for searching so processing may be dependent upon internet access
    
    -	Small need for data analysis for filtering use

## Results:
    The app will generate a text response that is broken into columns based on the different categories of information to be generated. Users will also be able to filter results based on the category they are most interested in. A possible feature would be to save or ‘favorite’ a search to reference at a later time.

