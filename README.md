Project Title
One Paragraph of project description goes here

Getting Started


Wearabletech CompanyScraper

(codes that need to run are Flask_app.py and ExecutesEverything.py)

To run this package please run the webapp Flask_app.py

Then to run ExecutesEverything.py continuously so that our webapp is frequently updating companies run from terminal: while :; do python ExecutesEverything.py;  sleep 10; done
--------------------------------------------------------------------------------
modules needed to run package:
•	bs4 pip3 install beautifulsoup4
o	 details about package: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
•	flask  pip3 install Flask
o	details about package: http://flask.pocoo.org/docs/1.0/installation/
•	selenium pip3 install -U selenium
o	details about package: https://pypi.org/project/selenium/
•	instaloader pip3 install instaloader
o	details about package: https://pypi.org/project/instaloader/
•	pythonwhois pip3 install pythonwhois
o	details about package: https://github.com/joepie91/python-whois
•	whois pip3 install whois
o	details about package https://pypi.org/project/whois/
•	Requests  pip3 install requests 
•	urllib.parse (python package)
•	re (python package)
•	datetime (python package)
•	ast (python package)
•	os (python package)
•	pathlib(python package)
•

----------------------------------------------------------------------------------
Brief explanation of how this package works:

What is going on in the ExecutesEverything.py:

User_post_hashtag.py  obtains the usernames that have used the specified hashtag
get_website.py gets url in someone’s instagram bio
CompanyInfo.py  gets information company information on the url’s found in get_website.py by using all these files listed
company_location.py
search_location.py
geocode.py
whois_location.py
contact_on_contactpage.py
bar_bones.py
bio_google.py
parser.py

the CompanyInfo.py results are then stored in a textfile called company_info.txt

headless_selenium.py function take a screen shot of each of the urls just found in the headless_selenium.py function
