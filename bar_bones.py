
def BarBones(website):
    """takes in a url and grabs the bar bones of it so for example if a url is http://www.epson.jp/products/trume/ it will out put  epson.jp
    this is necissary for the function Whois_location which doesn't work when the url has www or .com attached"""
    bar_bone_website=[]
    if website and "www" in website:
        head, sep, tail=website.partition("//") # head is http: sep is the seperator // and tail is the rest of it sawearables.com/

        head,sep,tail=tail.partition("/")

        head,sep,tail=head.partition("www.")# with http

        bar_bone_website.append(tail)
    else:
        head, sep, tail=website.partition("//") # head is http: sep is the seperator // and tail is the rest of it sawearables.com/

        head,sep,tail=tail.partition("/")

        bar_bone_website.append(head)

    return(bar_bone_website)
# url="https://www.brittanyannecohen.com/"
# print(BarBones(url))
