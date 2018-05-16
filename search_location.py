import re

def RegexLocation(text):
    """This function is used to look at text from a webpage and try and find a location within that text. It does it by
    looking for any text that contains a digit, maybe lower case letters and uper case letters. It also removes
     any digits attached with prices or percent signs because that will mess up the geocode function from working properly"""

    return all(re.search(pattern, text) for pattern in ['^[^\$]*$','^[^\%]*$','\d+', '[a-z]*', '[A-Z]'])
    
