from bs4 import BeautifulSoup
import requests
from utils import file_op as fo
from utils import string_op as so
from time import sleep


def get_url_content(url):
    return requests.get(url).content


def get_content_from_file(file):
    content_file = open(file, 'r')
    return content_file


def create_soup_from_url_content(content):
    return BeautifulSoup(content, "html.parser")


def get_book_link(soup):
    pdf_link_span = soup.find('span', attrs={'class': 'download-links'})
    try:
        book_link = pdf_link_span.a['href']
        return book_link
    except:
        return False


def get_category(soup):
    try:
        cat_link = soup.find('a', attrs={'rel': 'category'})
        category = cat_link.text
        return category
    except:
        return 'Unknown'


def download_book(link_to_book_page):
    book_page_content = get_url_content(link_to_book_page)
    book_page_soup = create_soup_from_url_content(book_page_content)

    book_link = get_book_link(book_page_soup)
    if not book_link:
        print("No Book Link")
        return False

    category = get_category(book_page_soup)
    file_name = so.get_file_name_of_url(book_link)
    if file_name == '':
        print("No Filename")
        return False
    if not fo.download_file(book_link, category, file_name):
        return False
    return True


def download_ebooks(starting_url, start, depth):
    if start == 1:
        first_content = get_url_content(starting_url)
        first_soup = create_soup_from_url_content(first_content)

        first_main = first_soup.main
        all_articles = first_main.find_all_next('article')

        for item in all_articles:
            link_to_book_page = item.div.a['href']
            sleep(3)
            if not download_book(link_to_book_page):
                continue
        start = 2

    for i in range(start, depth+1):
        print("** Navigating to page " + str(i) + " ...")
        next_content = get_url_content(starting_url + "/page/" + str(i))
        next_soup = create_soup_from_url_content(next_content)

        next_main = next_soup.main
        next_articles = next_main.find_all_next('article')

        for item in next_articles:
            link_to_book_page = item.div.a['href']
            sleep(6)
            if not download_book(link_to_book_page):
                continue

    return True


