import pythonwhois
import whois

def WhoisLocation(url):
    """finds the location of a url with packages like pythonwhois and whois
    NOTE: the url must be bar_bones, otherwise the whois wont work ex(https://www.nike.com/ won't work it needs to be nike.com) """
    location=[]
    location_str_list=[]
    try: # first try this
    #trying with pythonwhois to see if the location exists
        obj=pythonwhois.get_whois(url)
        for key in obj['contacts']['registrant']:
            location.append(obj['contacts']['registrant'][key])
        #turn the list into a string with a space between them
        str=' '.join(location)
        location_str_list.append(str)
    except TypeError:
        pass
    except Exception:# dealing wit hthe rest of the socket errros and whois.parser.PywhoisError
        pass
    if  len(location_str_list)==0:
        try: # if the first try doesn't work try this
            w = whois.whois(url)
            #if any of these are none we get a TypeError so to get rid of that we check if they are none or not to deal wit hthat issue
            if whois.whois(url)["address"]==None:
                pass
            else:
                location.append(whois.whois(url)["address"])
            if whois.whois(url)["city"]==None:
                pass
            else:
                location.append(whois.whois(url)["city"])
            if whois.whois(url)["state"]==None:
                pass
            else:
                location.append(whois.whois(url)["state"])
            if whois.whois(url)["zipcode"]==None:
                pass
            else:
                location.append(whois.whois(url)["zipcode"])
            if whois.whois(url)["country"]==None:
                pass
            else:
                location.append(whois.whois(url)["country"])

            #turn the list into a string
            str=' '.join(location)
            location_str_list.append(str)
        except Exception:# dealing with socket errors
            pass
        except KeyError:
            pass
        except TypeError:# there were maybe multiple addresses and my code coudln't figure that out
            print("multiple")
            pass
        except whois.parser.PywhoisError:
            pass
    return(location_str_list)

# url="runvi.io"
# print(WhoisLocation(url))
