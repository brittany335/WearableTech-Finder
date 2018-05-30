# WearableTech Finder (Python 3)

This package finds companys from a specified hashtag posted that day from instagram then scrapes the companys found for an email, bio, and address. It is then displays everything on a webapp.

## Getting Started

To run please open two terminals. In one terminal run the Flask_app.py to get a visual output of the results:
```
python3 Flask_app.py
```
In the other run ExecutesEverything.py. To run ExecutesEverything.py continuously so that the Flask_app.py is frequently updated in terminal run 

```
while :; do python3 ExecutesEverything.py;  sleep 10; done
```
Once those two files are running go to http://127.0.0.1:6039/ to see the site 

### Installation 
```
pip3 install -r requirements.txt
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

To change the hashtag being searched to find companys go into ExecutesEverything.py and change the hashtag to one you prefer.

### Scrape companys not from instagram

If you wish to use this package to scrape general companys just use the CompanyInfo.py script and put in as many urls as you wish to scrape in a list. 
