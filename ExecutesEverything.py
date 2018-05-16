#!/Users/BCohen/anaconda3/bin/python

################### WHAT THIS FILE DOES ##############################
#this file brings everything together, it runs the file that finds the people that posted about wearabletech todays
#then it grabs these users bio urls and makes sure we havn't used them before,
# then puts those urls into contact_and_email9 which then grabs each company info and outputs a list of dicitonarys of each compnay information
# then that list of comapny information is stores in company_info.text
#then we take a screen shot of the url of those new companys found
############################################################################
#this function needs to run to get the instagram posts on the hashtag wearabletech
#then it adds these usernames to the textfile list_of_instagram_usernames.txt
from user_post_hashtag import usernames
hashtag="wearabletech"
(usernames(hashtag))
############################################################################
# uses the textfile list_of_instagram_usernames.txt that was updated by the function usernames()
# then uses these 10 usernames to see if any of them have a url on their instagram page and outputs a list of the urls that were found out of those 10 usernames
from get_website import get_external_url
url_list=get_external_url("list_of_instagram_usernames.txt")
print(url_list)
############################################################################
#this takes in the list of url's created by get_external_url and gets information on each of those urls
from CompanyInfo import GetCompanyInfo
print( "going to find company info ")
# GetCompanyInfo(url_list)
companies_list=(GetCompanyInfo(url_list))
print( "company info search completed")
############################################################################
#append the list of company information to a text file to keep track of every company scraped
with open("company_info.txt","a") as f: #in write mode
    f.write("{}\n".format(companies_list))
############################################################################
#go and take a screenshot of each of the urls found in a headless browser
from headless_selenium import ScreenShot
for company in companies_list:
    print(company["href"])
    ScreenShot(company["href"])
