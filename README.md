# WearableTech Finder

This package finds companys from a specified hashtag posted that day from instagram then scrapes the companys found for an email, bio, and address. It is then displays everything on a webapp.

## Getting Started

To run please open two terminals. In one terminal run the Flask_app.py to get a visual output of the results:
```
python Flask_app.py
```
In the other run ExecutesEverything.py. To run ExecutesEverything.py continuously so that the Flask_app.py is frequently updated in terminal run 

```
while :; do python ExecutesEverything.py;  sleep 10; done
```

### Prerequisites
This package is only support on python3 

modules used to run this package include: 

•	bs4  (details about module  https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
```
pip3 install beautifulsoup4
```
•	flask (details about module http://flask.pocoo.org/docs/1.0/installation/)
```
pip3 install Flask
```
•	selenium (details about module https://pypi.org/project/selenium/)
```
pip3 install -U selenium
```
•	instaloader (details about module https://pypi.org/project/instaloader/)
```
pip3 install instaloader
```
•	pythonwhois (details about module https://github.com/joepie91/python-whois)
```
pip3 install pythonwhois
```
• whois (details about module https://pypi.org/project/whois/)
```
pip3 install whois
```
• Requests
```
pip3 install requests
```

### Inside ExecutesEverything.py

1) User_post_hashtag.py obtains the usernames that have used the hashtag specified 
2) get_website.py obtains the url to the username from the instagram bio
3) CompanyInfo.py gets company information on the url’s found in get_website.py by using all these files listed:

          company_location.py
          search_location.py
          geocode.py
          whois_location.py
          contact_on_contactpage.py
          bar_bones.py
          bio_google.py
          parser.py


4) The CompanyInfo.py results are then stored in a textfile called company_info.txt
5) headless_selenium.py function take a screen shot of each of the urls found in the CompanyInfo.py function

### Change the hashtag

To change the hashtag being search to find companys go into ExecutesEverything.py and change the hashtag to one you prefer.

### Scrape companys not from instagram

If you wish to use this package to scrape general companys just use the CompanyInfo.py script and put in as many urls as you wish to scrape in a list. 
