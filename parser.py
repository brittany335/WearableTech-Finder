#PLEASE note: code fully adapted from http://edmundmartin.com/scraping-google-with-python/
# I DO NOT take credit for this scraper of a google search, I changed something to use for my personal purpose

from bs4 import BeautifulSoup
def parse_results(html, keyword):
    """used to scrape the html from bio_google and gives us the description result
    of the keyword that would show up as the result on google  """
    soup = BeautifulSoup(html, 'html.parser')

    description_result=[]
    found_results = []
    rank = 1
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:

        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'r'})
        description = result.find('span', attrs={'class': 'st'})
        if link and title:
            link = link['href']
            title = title.get_text()
            if description:
                description = description.get_text()
            if link != '#':
                found_results.append({'keyword': keyword, 'rank': rank, 'title': title, 'description': description})
                rank += 1
    if len(found_results)!=0:
        result=found_results[0]["description"]
        description_result.append(result)
    else:
        pass
    return(description_result)
# print(parse_results(html,keyword))
# x=parse_results(html,'brittanyannecohen.com')
# print(x[0]["description"])
