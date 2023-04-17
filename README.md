
# F1 Poster Downloader

This is a Python script that downloads Formula 1 posters from the StatsF1 website. It downloads posters from all years between 1950 and 2021.

### Requirements

-   Python 3.x
-   Beautiful Soup 4
-   urllib

You can install the required libraries by running the following command:

```bash
pip install beautifulsoup4 urllib3
``` 
### Usage
1.  Clone the repository or download the code as a zip file and extract it.
2.  Open a terminal and navigate to the folder containing the script.
3.  Run the following command to start the script:

```bash
python f1_images.py
```
The script will create a folder named "f1_images" in your Pictures folder and will download all the posters in subfolders by year.

The script contains the following functions:

-   `getRawHTML(url)`: Takes a URL as an input and returns the raw HTML code.
-   `getImageURL(html_code, filename)`: Takes HTML code and a filename as inputs and returns a list of image URLs and corresponding image filenames.
-   `downImages(image_url, filename)`: Downloads an image from a URL and saves it with a specified filename.
-   `createFolder(path, folder_name)`: Creates a folder with a specified name at a specified path and returns the folder path.
-   `main()`: Runs the main part of the script, which downloads all the posters from the StatsF1 website.

### Note
-   The code might need to be modified if the structure of the StatsF1 website changes in the future.

### Images to download
https://drive.google.com/file/d/12bn82Qhjtxnc4nmurOUpDIfhqVb4rEk5/view?usp=sharing
