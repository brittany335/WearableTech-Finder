
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


from company_location import SearchingCompanyLocation
from search_location import RegexLocation
from geocode import GeocodeLocation
from Whois_location import WhoisLocation

from contact_on_contactpage import GettingContactsOnContactPage


from bar_bones import BarBones
from bio_google import fetch_results
from parser import parse_results

def GetCompanyInfo(url_list):
    """this function uses all the other functions created to gather company infromation
    It takes in a url that is in the form of a list and outputs a list of dictionarys for each url that
    contains the barbones (which is the png used for finder the name of the image in my flask app), the href, the
    email, contact_link ( as in the href page to the contact page (not super relevent )) and a description of the company """

    # creating a dictionary of the get_contacts
    company_info=[]

    for url in url_list:

        company_info_dictionary={"png":[],"href":[],"contact_link":[],"email":[],"location":[],"description":[]}
        # turn bit.ly or any other shortened link to orginal link

        #using a try except to deal with company urls that break the system
        try:
            orginal_link = requests.head(url, allow_redirects=True)
            print(orginal_link.url)

            response=requests.get(orginal_link.url,  timeout=5)# grabbing the url
            html=response.content# turning it into content
            soup=BeautifulSoup(html,'html.parser')# creating our soup

            # finding the hyper links
            #href is the hyperlink
            hyper_links=[link.get("href") for link in soup.find_all("a")]


            #grabbing the url to the contact then checking if the set is empty ie if they don't have a url
            # seeing if the anchor has the word contact in it unforutnitly unalbe to figure out if the anchore has the word contact attached to it bc that would be going into each html and each html is different wether they have a div or nto :/
            contact_link=set([contact for contact in hyper_links if contact and "contact" in contact]) #  if the element and the word listing is in the element (becuase there could be a hyperlink that is NONE whcich is why we need the and )
            # seeing if the anchor has a @ in it to link to an email
            contact_by_email=set([contact for contact in hyper_links if contact and "@" in contact]) #  if the element and the word listing is in the element (becuase there could be a hyperlink that is NONE whcich is why we need the and )
            created_hyperlink=[]

            #if the contact_link is empty but there is an an email hyperlink
            if len(contact_link)==0 and len(contact_by_email)!=0:
                #no url to contact exists so grabbing the email within the hyper_links
                # sometimes some sites contact is just a link that opens to an email so this grabs that
                # print("contact information by email exists", orginal_link.url,contact_by_email)
                company_info_dictionary["email"]=(list(contact_by_email))
                #add a dictionary of information to a dictionary of the url
                # company_info[orginal_link.url]=company_info_dictionary


                bar_bones_of_website=BarBones(orginal_link.url)

                #finding the description of the company
                keyword, html=fetch_results(bar_bones_of_website[0], 1, 'en')
                description=parse_results(html,keyword)

                #adding description to dictionayr
                company_info_dictionary["description"]=(description)

                #looking for location with my searchcompanylocation function
                location=SearchingCompanyLocation(orginal_link.url)

                #putting that result into the geocodelocaiton
                location=GeocodeLocation(str(location[0]))

                #if no location found go to the backup which is the whoislocation function
                if len(location)==0:
                    location=WhoisLocation(bar_bones_of_website[0])
                    company_info_dictionary["location"]=(location)
                else:
                    company_info_dictionary["location"]=(location)

                #add the hyperlink to the dictionary
                company_info_dictionary["href"]=(orginal_link.url)


                #creating out image name for the company so that we can match it later with the flask app
                table = str.maketrans(dict.fromkeys('*"\[];|:!@#$/.'))
                #sometimes a compnay might be called and their link might change from http to https so we need to get rid of this for when we are checking our image name with the dictionary in our flask app
                filename=(orginal_link.url.translate(table)).replace("https","").replace("http","")

                company_info_dictionary['png']=(filename+'.png')
                company_info.append(company_info_dictionary)


            # if contact information exists via contact_link and contact_by_email
            elif len(contact_link)!=0 and len(contact_by_email)!=0:
                company_info_dictionary["email"]=(list(contact_by_email))

                # use the contact by email for the contact info but find the hyperlink for contacts for location
                # url to contact info
                # figuring out if the ancore to the contact link is an actore link or an extention to the orgianl links
                part_of_orginal_link=url[0:15]
                # print("part_of_orginal_link",part_of_orginal_link)
                full_contact_link=set([contact for contact in list(contact_link) if contact and part_of_orginal_link in contact])

                if len(list(full_contact_link))!=0:# this means the contact_link is actually a properly link
                    #(do nothign to the contact link)
                    # print("use orginal hyperlink",orginal_link.url,full_contact_link)
                    company_info_dictionary["contact_link"]=(list(full_contact_link))

                    bar_bones_of_website=BarBones(orginal_link.url)
                    keyword, html=fetch_results(bar_bones_of_website[0], 1, 'en')
                    description=parse_results(html,keyword)

                    company_info_dictionary["description"]=(description)


                    location=SearchingCompanyLocation(list(full_contact_link)[0])
                    location=GeocodeLocation(str(location[0]))
                    if len(location)==0:
                        location=WhoisLocation(bar_bones_of_website[0])
                        company_info_dictionary["location"]=(location)
                    else:
                        company_info_dictionary["location"]=(location)

                    company_info_dictionary["href"]=(orginal_link.url)


                    table = str.maketrans(dict.fromkeys('*"\[];|:!@#$/.'))
                    filename=(orginal_link.url.translate(table)).replace("https","").replace("http","")


                    company_info_dictionary['png']=(filename+'.png')
                    company_info.append(company_info_dictionary)



                else:# this means we need to create the properer hyperlink to use

                    bar_bones_of_website=BarBones(orginal_link.url)

                    keyword, html=fetch_results(bar_bones_of_website[0], 1, 'en')
                    description=parse_results(html,keyword)

                    company_info_dictionary["description"]=(description)

                    # remove the forward slash in the begingin and the end of the hyerplink,ex   /contact/  --> contact , and then adding this to the orginal link
                    contact_link=orginal_link.url+list(contact_link)[0][1:]

                    created_hyperlink.append(contact_link)
                    company_info_dictionary["contact_link"]=(created_hyperlink)

                    location=SearchingCompanyLocation(contact_link)
                    location=GeocodeLocation(str(location[0]))
                    if len(location)==0:
                        location=WhoisLocation(bar_bones_of_website[0])
                        company_info_dictionary["location"]=(location)
                    else:
                        company_info_dictionary["location"]=(location)
                    company_info_dictionary["href"]=(orginal_link.url)


                    table = str.maketrans(dict.fromkeys('*"\[];|:!@#$/.'))
                    filename=(orginal_link.url.translate(table)).replace("https","").replace("http","")


                    company_info_dictionary['png']=(filename+'.png')
                    company_info.append(company_info_dictionary)

            # # if we only have the contact_link
            elif len(contact_link)!=0 and len(contact_by_email)==0:


                # url to contact info
                # figuring out if the ancore to the contact link is an actore link or an extention to the orgianl links
                part_of_orginal_link=orginal_link.url[0:15]

                full_contact_link=set([contact for contact in list(contact_link) if contact and part_of_orginal_link in contact])
                if len(list(full_contact_link))!=0:# this means the contact_link is actually a properly link
                    #(do nothign to the contact link)
                    company_info_dictionary["contact_link"]=(list(full_contact_link))

                    #finding any email on that page
                    email=(GettingContactsOnContactPage(list(full_contact_link)[0]))
                    company_info_dictionary["email"]=(email)

                    bar_bones_of_website=BarBones(orginal_link.url)

                    location=SearchingCompanyLocation(list(full_contact_link)[0])
                    location=GeocodeLocation(str(location[0]))

                    if len(location)==0:
                        location=WhoisLocation(bar_bones_of_website[0])
                        company_info_dictionary["location"]=(location)
                    else:
                        company_info_dictionary["location"]=(location)


                    keyword, html=fetch_results(bar_bones_of_website[0], 1, 'en')
                    description=parse_results(html,keyword)

                    company_info_dictionary["description"]=(description)

                    company_info_dictionary["href"]=(orginal_link.url)


                    table = str.maketrans(dict.fromkeys('*"\[];|:!@#$/.'))
                    filename=(orginal_link.url.translate(table)).replace("https","").replace("http","")


                    company_info_dictionary['png']=(filename+'.png')
                    company_info.append(company_info_dictionary)

                else:# this means we need to create the properer hyperlink to use

                    # remove the forward slash in the begingin and the ned
                    contact_link=orginal_link.url+list(contact_link)[0][1:]

                    created_hyperlink.append(contact_link)
                    company_info_dictionary["contact_link"]=(created_hyperlink)

                    #finding any email on that page
                    email=(GettingContactsOnContactPage(contact_link))

                    company_info_dictionary["email"]=(email)

                    bar_bones_of_website=BarBones(orginal_link.url)

                    location=SearchingCompanyLocation(contact_link)
                    location=GeocodeLocation(str(location[0]))

                    if len(location)==0:
                        location=WhoisLocation(bar_bones_of_website[0])
                        company_info_dictionary["location"]=(location)
                    else:
                        company_info_dictionary["location"]=(location)


                    keyword, html=fetch_results(bar_bones_of_website[0], 1, 'en')
                    description=parse_results(html,keyword)

                    company_info_dictionary["description"]=(description)
                    company_info_dictionary["href"]=(orginal_link.url)

                    table = str.maketrans(dict.fromkeys('*"\[];|:!@#$/.'))
                    filename=(orginal_link.url.translate(table)).replace("https","").replace("http","")


                    company_info_dictionary['png']=(filename+'.png')
                    company_info.append(company_info_dictionary)


            #not contact link page and no email exist so scraping the main webpage given to this function
            elif len(contact_link)==0 and len(contact_by_email)==0:


                email=(GettingContactsOnContactPage(orginal_link.url))
                company_info_dictionary["email"]=(email)
                #
                bar_bones_of_website=BarBones(orginal_link.url)
                location=SearchingCompanyLocation(orginal_link.url)
                location=GeocodeLocation(str(location[0]))

                if len(location)==0:
                    location=WhoisLocation(bar_bones_of_website[0])
                    company_info_dictionary["location"]=(location)
                    # print("stuff",company_info_dictionary)
                else:
                    company_info_dictionary["location"]=(location)

                keyword, html=fetch_results(bar_bones_of_website[0], 1, 'en')
                description=parse_results(html,keyword)

                company_info_dictionary["description"]=(description)

                company_info_dictionary["href"]=(orginal_link.url)

                table = str.maketrans(dict.fromkeys('*"\[];|:!@#$/.'))
                filename=(orginal_link.url.translate(table)).replace("https","").replace("http","")


                company_info_dictionary['png']=(filename+'.png')
                company_info.append(company_info_dictionary)

        except Exception as e:# dealing with requests.exceptions.SSLErro errors, delaing wit hthe websites that cause it to break
            # print(e)
            pass
    return(company_info)
# url=["https://bit.ly/2rhU89G"]
# url=["https://www.triing.in/"]
# # # url=['http://www.dynaback-tshirt.com/', 'http://www.touchinginnovations.de/', 'https://theneonmuse.com/', 'http://www.freyjasewell.co.uk/']
# # url=['http://lynqme.com/', 'http://www.alexiswalsh.com/', 'http://catarse.me/gedeaninha']
# url=["https://buyitall.today/"]
# url=['http://www.wearablefashion.co/', 'https://tinyurl.com/yblczys8', 'https://myndplay.com/']
# # # url=["https://tinyurl.com/yblczys8"]
# # url=["https://myndplay.com/"]
#
# print(GetCompanyInfo(url))
