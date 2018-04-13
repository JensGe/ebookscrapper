from bs4 import BeautifulSoup
import requests, re
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


def get_nav(soup):
    nav_main = []
    nav_sub = []

    first_ul = soup.ul
    all_li_in_ul = first_ul.find_all_next('li')

    for item in all_li_in_ul:
        link = item.a['href']
        if (link.count('/') == 4) and link not in nav_main:
            nav_main.append(link)
        if link.count('/') == 5:
            nav_sub.append(link)

    return nav_main, nav_sub


def get_last_page_count(soup):
    last_page_regex = re.compile('Last Page')
    return soup.find('a', attrs={'title': last_page_regex}).string


def get_links_to_books(soup):
    book_links = []

    first_main = soup.main
    all_articles = first_main.find_all_next('article')

    for item in all_articles:
        book_links.append(item.div.a['href'])

    return book_links


def get_book_pdf_link(soup):
    pdf_link_span = soup.find('span', attrs={'class': 'download-links'})
    return pdf_link_span.a['href']


def get_book_info(soup):
    # book_details = {'author': '',
    #                 'isbn': '',
    #                 'year': '',
    #                 'pages': '',
    #                 'language': '',
    #                 'file_size': '',
    #                 'file_format': '',
    #                 'category': ''}
    book_detail_div = soup.find('div', attrs={'class': 'book-detail'})
    book_temp_details = book_detail_div.find_all('dd')
    book_details = []
    for element in book_temp_details:
        book_details.append(element.text)
    return book_details


def create_download_list(links_to_book_pages):
    download_list = []
    for item in links_to_book_pages:
        item_content = get_url_content(item)
        item_soup = create_soup_from_url_content(item_content)
        item_link = get_book_pdf_link(item_soup)
        download_list.append(item_link)
        print(item_link)
        sleep(3)
    return download_list


def download_file_list(url_list):
    for url in url_list:
        file_name = so.get_file_name_of_url(url)
        fo.download_file(url, file_name)
        print("Downloaded " + file_name)
        sleep(3)
