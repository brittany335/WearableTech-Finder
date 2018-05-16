import instaloader
import datetime
import re

def usernames(hashtag):
    """obtains the usernames that have used the specified hashtag (ie wearabletech)
     that are from today then adds ten of these usernames to a textfile called list_of_instgram_usernames
     (note: the reason why I don't add all the usernames is because I find company information related to theneonmuse
     usernames and more then ten will sometimes give a request error for making too many requests)"""

    L = instaloader.Instaloader()# creating our instagram handle

    todays_date=(datetime.datetime.today().strftime('%Y-%m-%d'))# capture todays date

    usernames=[]
    # find the posts on the hashtag specified
    for posts in L.get_hashtag_posts(hashtag):
        # checking if the date they were posted is todays date (using regex to get rid of the time that is included in posts.date)
        date_of_post=re.findall("[0-9]{4}[-][0-9]{2}[-][0-9]{2}",str(posts.date))
        print(date_of_post,posts.owner_username)
        # adding these usernames to a list
        usernames.append(str(posts.owner_username))
        if todays_date!=date_of_post[0]:# if it wasn't posted today stop the loop
            break

    usernames=usernames[:-1]# remove the person from the day before

    ###########running code 24/7 do this ############(grabe the first ten in the recently posted username list like so)
    #usernames=usernames[:10]
    #usernames=list(set(usernames))
    #due to the fast that when i do usernames=list(set(usernames)) this changed the order of the usernames
    #that was recently posted and randomizes them so it's not the best way if we are running this code 24/7
    ######################

    ########### not running code 24/7 do this###########
    #this will randomize the instragram posts that day so not grabbing from most recently posted so that we typically get some output
    usernames=list(set(usernames))# get rid of duplicat posts in same day
    # only grab the first ten so that we don't get a request error
    usernames=usernames[:10]
    ######################

    # appending todays list to a file,  this list to a text file to keep track of everyperson scraped
    with open("list_of_instagram_usernames.txt","a") as f: #in write mode
        f.write("{}\n".format(usernames))# adding a new line https://stackoverflow.com/questions/21839803/how-to-append-new-data-onto-a-new-line
    return(usernames)
# hashtag="wearabletech"
# print((usernames(hashtag)))
