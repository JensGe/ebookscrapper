from WebScrapper import WebScrapperV2 as ws
from time import sleep

main_url = "http://www.allitebooks.com"
# main_file = "tests/allitebooks.html"

#TODO Check for integer
# and start < end

start = input("Start Page: ")
depth = input("End Page: ")

ws.download_ebooks(main_url, int(start), int(depth))


