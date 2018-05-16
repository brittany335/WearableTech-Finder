
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from ast import literal_eval # used when we are opening our textfile


def get_external_url(textfile):
    """gets the external url (ie the url in someone's instagram bio) by webscraping the persons instagram page
    returns a list of the urls """

    # opening our textfile as a list and not as a string of a list
    with open(textfile) as f:
        mainlist = [list(literal_eval(line)) for line in f]

    # grab the most recent usernames added to the list
    mostrecent=(mainlist[-1])

    # remove the most recent usernames added to the list so that we can join all old usernames together
    mainlist.remove(mostrecent)

    # joining all the older usernames from the lists of lists and makes them into one list https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
    flat_list = [item for sublist in mainlist for item in sublist]

    # find the unique usernames from the mostrecent list in comparision with all the older lists of usernames https://stackoverflow.com/questions/5305164/get-difference-from-two-lists-in-python
    users_not_yet_scraped=list(set(mostrecent)-set(flat_list))

    url_list=[]
    for username in users_not_yet_scraped:
        # creating their instagram page so that we can scrape their page
        url="https://www.instagram.com/"+username+"/?hl=en"
        response=requests.get(url, timeout=5)# grabbing the url
        html=response.content# turning it into content
        soup=BeautifulSoup(html,'html.parser')# creating our soup
        # grabbing a persons url if they have one
        url=re.findall("(?<=false,\"external_url\":\")[^\"]+",str(soup))
        # if there is no url don't add it to the list:
        if len(url)!=0:
            url_list.append(url[0])

    #removing the links with top traffic websites  because I want unique company links# reference https://stackoverflow.com/questions/28565920/python-remove-the-certain-string-from-list-if-string-includes-certain-keyword

    # opening the list of traffic websites and creating that into a list
    with open("top_traffic_websites.txt") as f:
       top_traffic_websites = f.readlines()
       # remove whitespace characters like `\n` at the end of each line
       top_traffic_websites = [website.strip() for website in top_traffic_websites]

    #removing top traffic websites
    unique_company_websites_list = [website for website in url_list if not any(word in website for word in top_traffic_websites)]
    return(unique_company_websites_list)
#
# textfile="list_of_instagram_usernames.txt"
# print(get_external_url(textfile))
