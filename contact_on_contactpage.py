
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def GettingContactsOnContactPage(url):
    """this function takes in the content hyperlink that is found
    in get_contacts function and scrapes the contact page for an email"""

    response=requests.get(url,  timeout=5)# grabbing the url
    html=response.content# turning it into content
    soup=BeautifulSoup(html,'html.parser')# creating out soup


    # if the company gives useful information just through getting rid of the html jargen
    #reference https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
    # getting rid of the script sytle in html
    for script in soup(["script", "style"]):
        (script.extract())    # rip it out

    # get text
    # grabbing the first chunk of text
    text = soup.get_text()

    # creating a list of the text that shows up by splitting the text at the new line of each section then stripping away the new lines
    text_on_contact_pg= [t for t in text.split('\n') if t.strip()]
    email=[]
    for text in text_on_contact_pg:
        #find an email
        if len(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",text))==0:
            # print("this is not an email")
            #email=[]# no email so leaving it empty
            #email.append()
            pass
        else:
            # print("the email is",re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",text))
            email.append(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",text)[0])

    #removing, any duplicts
    email=list(set(email))
    #returns a list
    return(email)
# print(GettingContactsOnContactPage())
