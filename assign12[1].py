#Caleb Mogyabiyedom
#CS51
#5/3/2023
#assign12

from stackqueue import *
import urllib
import time
from urllib.request import urlopen


def is_valid_pomona_url(url_string):
    """
    A function that checks if the website is a pomona.edu website
    :param url_string: url of the website
    :return:a boolean
    """
    return "pomona.edu" in url_string


def is_full_url(url_string):
    """
    A function that checks whether the input url is a valid website
    :param url_string:url of website
    :return: boolean True if it is and false if otherwise
    """
    for letter in url_string:# iterates through each character in the string
        #checks the first 5 charaters of the string
        if url_string[0:4] == "http":
            return True
        else:
            return False

def get_all_urls(page):
    """
    A function that gets all the urls available in a page
    :param page: url of a website
    :return: a list of urls
    """
    urls = []
    # while is_full_url(page):
    try:
        web_page = urlopen(page, timeout=2)  # opens the webpage

        search_line = '<a href=' #refers to what marks a url in a page.

        page_text = web_page.read().decode('ISO-8859-1')

        begin_index = page_text.find(search_line)

        while begin_index != -1:

            end_index = page_text.find('"' or "'", begin_index+9)
            url = page_text[begin_index+9:end_index]

            if is_full_url(url):# checks whether the url is valid

                urls.append(page_text[begin_index+9:end_index])

            begin_index = page_text.find(search_line, end_index)


    except urllib.error.URLError: # gives instructions on what to do when url is invalid
        print("Ignoring:" + page)
        return []
    except urllib.error.HTTPError:#gives instructions on what to do when url is invalid
        print("Ignoring:" + page)
        return []
    return urls # a list of urls in the page


def filter_pomona_urls(url_list):
    """
    A function that goes through a list of urls and returns one with pomona.edu in it
    :param url_list: a list of urls
    :return: a list of urls containing pomona.edu
    """
    pomona_urls=[]
    for url in url_list:
        if "pomona.edu" in url:
            pomona_urls.append(url)#adds pomona.edu containing urls to the pomona_urls list
    return pomona_urls




def crawl_pomona(start_url, to_visit,max_urls_num):
    """
    A function that visits all the websites containing pomona.edu from the starting url
    :param start_url: where the search begins
    :param to_visit: a stack or a queue indicating how the search is to be implemented
    :param max_urls_num: maximum number of urls to crwal
    :return: list ofurls visited
    """

    visited=[start_url]
    num_crawled = 0 #keeps track of the number of urls being crawled
    to_visit.add(start_url)


    while not to_visit.is_empty() and num_crawled <= max_urls_num:

        current_url = to_visit.remove()
        print("Crawling:" + current_url)
        time.sleep(0.1)
        # print(num_crawled)

        all_urls = get_all_urls(current_url)
        url_pomona_deeper = filter_pomona_urls(all_urls)# includes all urls with pomona.edu whiles using the
        #starting url as a starting point
        for url in url_pomona_deeper:
            if url not in visited:
                num_crawled += 1#updates the number of urls crawled

                to_visit.add(url)
                visited.append(url)


    return visited# list of urls visited


def write_pomona_urls(start_url, to_visit,max_url_num, filename ):
    """
    A function that writes all the urls being visited unto a file
    :param start_url: where the search begins
    :param to_visit: a stack or a queue indicating how the search is to be implemented
    :param max_url_num: maximum number of urls to crwal
    :param filename: name of file
    :return: none
    """
    print(start_url)

    file = open(filename, "w")
    crawled_list = crawl_pomona(start_url, to_visit, max_url_num)#getting all the urls which are to be writeen on file
    try:
        for url in crawled_list:
            file.write(str(url) + "\n")
            #print(url)
        file.close()
    except http.client.InvalidURL: #a possible error that may occur
        print("Ignoring:" + url )


"""
Queue
Crawling:https://www.pomona.edu/academics/departments/computer-science/faculty-staff
Crawling:https://www.pomona.edu/map/?id=523#!m/54434
Crawling:https://www.pomona.edu/directory/people/eleanor-birrell
Crawling:https://www.pomona.edu/directory/people/tzu-yi-chen
Crawling:https://www.pomona.edu/directory/people/anthony-clark
Crawling:https://www.pomona.edu/directory/people/joseph-c-osborn
Crawling:https://www.pomona.edu/directory/people/alexandra-papoutsaki
Crawling:https://www.pomona.edu/directory/people/yuqing-melanie-wu
Crawling:https://www.pomona.edu/map/?id=523#!m/54413
Crawling:https://www.pomona.edu/directory/people/zilong-ye
Crawling:https://www.pomona.edu/directory/people/thomas-yeh
Crawling:https://www.pomona.edu/directory/people/kim-b-bruce
Crawling:https://www.pomona.edu/directory/people/everett-l-bull
Crawling:https://www.pomona.edu/map/?id=523#!m/54476
Crawling:https://www.pomona.edu/directory/people/corey-leblanc
Crawling:http://www.cs.pomona.edu/~ebirrell/
Crawling:http://www.cs.pomona.edu/~tzuyi
Crawling:https://cs.pomona.edu/~ajc/
Crawling:https://cs.pomona.edu/~ajc/arcslab/
Crawling:https://research.pomona.edu/jcosborn
Crawling:https://research.pomona.edu/faim/
Crawling:http://www.cs.pomona.edu/~apapoutsaki
Crawling:http://www.cs.pomona.edu/~mwu
Crawling:http://pages.pomona.edu/~zyaa2019/
Ignoring:http://pages.pomona.edu/~zyaa2019/
Crawling:http://www.cs.pomona.edu/~kim/
Crawling:https://www.pomona.edu/academics/departments/computer-science
Crawling:https://www.pomona.edu
Crawling:http://www.cs.pomona.edu/classes/cs54
Crawling:http://www.cs.pomona.edu/classes/cs101
Crawling:https://www.pomona.edu/
Crawling:https://www.pomona.edu/news/2022/11/01-computer-science-students-work-autonomous-robots-campus-lab
Crawling:https://cs.pomona.edu/classes/cs105/
Crawling:https://cs.pomona.edu/~dkauchak/
Crawling:https://cs.pomona.edu/classes/cs140/
Crawling:https://cs.pomona.edu/classes/cs152/
Crawling:https://research.pomona.edu/jcosborn/
Crawling:https://research.pomona.edu/jcosborn/cv/
Crawling:https://research.pomona.edu/faim
Crawling:https://cs.pomona.edu/classes/cs54
Crawling:https://cs.pomona.edu/classes/cs181g
Crawling:https://cs.pomona.edu/classes/cs190
Crawling:https://research.pomona.edu/faim/publications/
Crawling:https://research.pomona.edu/faim/category/research-journal/bootstrapping-mappy/
Crawling:https://research.pomona.edu/faim/category/research-journal/accessibility-via-mappy/
Crawling:https://cs.pomona.edu/classes/cs51a/
Crawling:https://cs.pomona.edu/~dkauchak/classes/s19/cs51a-s19/
Crawling:https://cs.pomona.edu/classes/cs51a/archive/2022spring/
Crawling:https://cs.pomona.edu/classes/cs062-2017fa/
Crawling:http://www.cs.pomona.edu/classes/cs062-2018sp/
Crawling:http://www.cs.pomona.edu/classes/cs062-18fa/
Crawling:https://cs.pomona.edu/classes/cs062-2019fa/
Crawling:https://cs.pomona.edu/classes/cs62/sp20/
Crawling:https://cs.pomona.edu/classes/cs62/fa21/
Crawling:http://www.cs.pomona.edu/classes/cs190/
Crawling:http://www.cs.pomona.edu
Crawling:http://www.pomona.edu
Crawling:http://www.pomona.edu/
Crawling:http://www.cs.pomona.edu/splashe/
Crawling:http://www.cs.pomona.edu/
Crawling:https://www.pomona.edu/administration/academic-dean/general/faculty-jobs
"""

"""
Stack
Crawling:https://www.pomona.edu/academics/departments/computer-science/faculty-staff
Crawling:https://www.pomona.edu/directory/people/corey-leblanc
Crawling:https://www.pomona.edu/map/?id=523#!m/54476
Crawling:https://www.pomona.edu/directory/people/everett-l-bull
Crawling:https://www.pomona.edu/directory/people/kim-b-bruce
Crawling:http://www.cs.pomona.edu/~kim/
Crawling:http://www.cs.pomona.edu/

"""



"""
In the experiments, I found that the first 100 urls visited by Stack and Queue  will be different. Stack visited 
urls that were closer to the startin url while queue visited those that were far away.Using Queue is to be preferred 
since it ensures that urls from different parts of the page are included.
"""




















































