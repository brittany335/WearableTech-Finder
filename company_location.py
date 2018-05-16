
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


from search_location import RegexLocation


def SearchingCompanyLocation(url):
        """scrapes a websites for html then uses RegexLocation
        function to use the information scraped to grabe a possible location. returns a single list of the location that also contains a ton of text jammed into it"""
        location=[]
        response=requests.get(url,  timeout=5)# grabbing the url
        html=response.content# turning it into content
        soup=BeautifulSoup(html,'html.parser')# creating out soup

        locations={"location":[]}
        # if the company gives useful info in the paragraph tag
        content_in_paragraph=[paragraph.getText() for paragraph in soup.find_all('p')]# grabbing the infromation from the paragraph tags

        #removing the new line or tab
        paragraph=[element.replace('\n'," ").replace('\t',"") for element in content_in_paragraph]
        # removing wierd excess space https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
        paragraph=[' '.join(element.split()) for element in paragraph]

        # from the paragraph tags seeing if there is a location being used by passing it to our RegexLocation() funciton
        location_with_paragraph_tag=(list(filter(RegexLocation, paragraph)))# next just gives us the first one, filter turns the value from the is_location() funtion no longer boolean

        #  getting rid of the html jargen
        #reference https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
        # getting rid of the script sytle in html
        for script in soup(["script", "style"]):
            (script.extract())    # rip it out

        # get text
        # grabbing the first chunk of text
        text = soup.get_text()

        # creating a list of the text that shows up by splitting the text at the new line of each section then stripping away the new lines
        final_required = [t for t in text.split('\n') if t.strip()]

        # removing wierd excess space https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
        c=[' '.join(element.split()) for element in final_required]

        location_without_paragraph_tag=(list(filter(RegexLocation, c)))#filter turns the value from the is_location() funtion no longer boolean

        # find which list is longer if there is only one thing found in the lists
        # if the list size is   equal and equals 1
        if len(location_without_paragraph_tag) == len(location_with_paragraph_tag) and len(location_with_paragraph_tag)==1:
            # print("size of lists is 1")
            if len(location_without_paragraph_tag[0])==len(location_with_paragraph_tag[0]):
                # print("the two lists are the exact same ")
                # if there is the word copyright get rid of it bc it is a problem with the geocode
                location.append((location_without_paragraph_tag[0]).replace('Copyright',""))
            elif len(location_without_paragraph_tag[0])>len(location_with_paragraph_tag[0]):
                # print("location_without_paragraph_tag is bigger")
                location.append((location_without_paragraph_tag[0]).replace('Copyright',""))
            else:
                # print("location_with_paragraph_tag is bigger")
                location.append((location_with_paragraph_tag[0]).replace('Copyright',""))
        # if the list size is equal and equals zero
        if len(location_without_paragraph_tag) == len(location_with_paragraph_tag) and len(location_with_paragraph_tag)==0:
            # there is no location found
            # print("there is no location found")
            location.append((location_with_paragraph_tag))

        # if the sizes arn't equal we want to find the size of the string of the lists
        location_without_paragraph_tag_list=[]
        location_with_paragraph_tag_list=[]
        if len(location_without_paragraph_tag) != len(location_with_paragraph_tag):
            # print("the sizes of the two lists arn't equal")
            location_without_paragraph_tag_str=' '.join(location_without_paragraph_tag)
            location_with_paragraph_tag_str=' '.join(location_with_paragraph_tag)


            location_without_paragraph_tag_list.append(location_without_paragraph_tag_str)

            location_with_paragraph_tag_list.append(location_with_paragraph_tag_str)

            if len(location_without_paragraph_tag_str)>len(location_with_paragraph_tag_str):
                location.append(location_without_paragraph_tag_str.replace('Copyright',""))
            else:
                location.append(location_with_paragraph_tag_str.replace('Copyright',""))

        # if the sizes of the tags are equal and are larger then 0 and 1 ind the size of the string of the lists
        location_without_paragraph_tag_list=[]
        location_with_paragraph_tag_list=[]
        if len(location_without_paragraph_tag) == len(location_with_paragraph_tag):
            location_without_paragraph_tag_str=' '.join(location_without_paragraph_tag)
            location_with_paragraph_tag_str=' '.join(location_with_paragraph_tag)

            location_without_paragraph_tag_list.append(location_without_paragraph_tag_str)

            location_with_paragraph_tag_list.append(location_with_paragraph_tag_str)

            if len(location_without_paragraph_tag_str)>len(location_with_paragraph_tag_str):
                location.append(location_without_paragraph_tag_str.replace('Copyright',""))
            elif len(location_without_paragraph_tag_str)<len(location_with_paragraph_tag_str):
                location.append(location_with_paragraph_tag_str.replace('Copyright',""))
            else:
                location.append(location_with_paragraph_tag_str.replace('Copyright',""))

        return(location)
# url='https://www.esighteyewear.com/contact'
# url='https://www.triing.in/'
# print(SearchingCompanyLocation(url))
