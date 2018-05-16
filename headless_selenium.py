# followed this tutorial https://medium.com/@stevennatera/web-scraping-with-selenium-and-chrome-canary-on-macos-fc2eff723f9e
from pathlib import Path
import os
def ScreenShot(url):

    """this function takes a screen shot of a url in a headless browser and then saves that file to a folder called images"""

    #I am going to make the name of the images the name of the url,
    # I first need to remove specifc characters from a url that could screwup an image file being made
    #I then need to also remove either the https or http attached to the url becasue
    # I am going to need to grab this filename for my webapp where in Companyinfo I am creating a png
    # value to match with the image but many times going to a website the http might change to https or vise versa
    # so i need to elinate this issue
    table = str.maketrans(dict.fromkeys('*"\[];|:!@#$/.'))
    filename=(url.translate(table))
    filename=(url.translate(table)).replace("https","").replace("http","")

    #check if the screenshot was already made for a url since I don't wnat to waste precious time taking a screenshot of a company already made
    my_file = Path("./images/"+filename+".png")
    if my_file.is_file():
        print("image already made")

    else:# make image
        print("make image")
        from selenium import webdriver
        # opening up selenium to create a headless broswer
        options = webdriver.ChromeOptions()
        options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
        options.add_argument('window-size=800x841')
        options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        # savings a screenshot to the folder we want (addopted from this stack overflow https://stackoverflow.com/questions/3422262/take-a-screenshot-with-selenium-webdriver)
        driver.save_screenshot("./images/"+filename+".png")
        driver.quit()

# url="https://www.nike.com/us/en_us/"
# ScreenShot(url)
