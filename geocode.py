import urllib.parse
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def GeocodeLocation(location):
    """takes in a string  (from company_location) then checks if there actually is a location that is found
    finds the location, returns a list of the locations"""
    # converting the string into what we can use for sending a url ie converts a sentence like "where am i" to where+am+i&oq
    location=urllib.parse.quote(location, safe='')
    #making a get request to the googleapis geocode
    url="https://maps.googleapis.com/maps/api/geocode/json?address="+location+"&key=AIzaSyCSSqDFPG7qIiVU1KlUukm2WGSwz-uDxi4"
    response=requests.get(url,  timeout=5)# grabbing the url
    address=[]

    # if geocode fuckign fails for some god awful reason we need to make this try except block
    try:
        # grab the data that is spit out into json format
        data = response.json()
        results = data['results']
        # import pprint
        # pp=pprint.PrettyPrinter()
        # pp.pprint(results

        # go into the results:
        for result in results:
            address.append(result["formatted_address"])

        from difflib import SequenceMatcher#https://stackoverflow.com/questions/43561877/how-do-i-compare-two-sentence-strings-for-a-similarities-in-python

        # fixing geocodes error (geocode will output everyform of the address that is similar and obviously we wnat just the correct addresses
        #ex: lets say the address is 201 angell street providence rhoadisland geocode will output multiple forms of this so like 1)angell street providence rhoadisland 2) 201 angell street providence rhoadisland 3)angell street  rhoadisland)
        while len(address)>1:# if there is more then one locaiton in the list
            ratios=[]
            try:
                for number in range(len(address)-1):
                    ratio = SequenceMatcher(None, address[number], address[number+1]).ratio()
                    ratios.append(ratio)
                    if ratio>.6:
                        if len(address[number])>len(address[number+1]):
                            address.remove(address[number+1])
                        else:
                            address.remove(address[number])

            except IndexError:
                pass
            if (all(i <= .60 for i in ratios))==True:# making sure everything is a unique address
                break# get out of the while loop
    except ValueError: # there was a 400 response  # includes simplejson.decoder.JSONDecodeError
        pass
    return(address)
# x="Thank You! With Modulaj we augmented jewellery through technology and brought it into the 21st century.We are happy you came along for the ride. Anticipate a return to Brutalist architecture of Montreal, circa 1967—a city poised at the end of history—the last beacon for the last modern man. Inspired by Société de transport de Montréal, Modulaj revives mid-century modernity: poured concrete cubes, stacked sheet metal, and cuboids of tinted glass. 1/10th the size of a smart phone. And almost as clever.Digital Trends Jewellery hasn't changed in 5000 years. With Modulaj we have augmented jewellery with technology and brought it into the 21st century.Thank you! We are happy you came along for the ride."
# print(GeocodeLocation(x))
