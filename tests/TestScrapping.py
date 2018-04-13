import unittest
import WebScrapper.WebScrapperV2 as ws
import utils.string_op as so
import utils.file_op as fo
import os

download_folder = "E:/e-Books/_allitebooks/"


class TestScrapping(unittest.TestCase):

    def test_download_file_list(self):
        url_to_download = 'http://www.gutenberg.org/files/1342/1342-pdf.pdf'
        fo.download_file(url_to_download, 'test', '1342-pdf.pdf')
        self.assertTrue(os.path.isfile(download_folder + 'test/1342-pdf.pdf'))
        fo.rm(download_folder + 'test/1342-pdf.pdf')
        fo.rmd(download_folder + 'test')

    def test_get_book_link(self):
        content = ws.get_content_from_file('pro-c-8-8th-edition.html')
        content2 = ws.get_content_from_file('embedded-systems-architecture-for-agile-development-2.html')

        soup = ws.create_soup_from_url_content(content)
        soup2 = ws.create_soup_from_url_content(content2)

        book_link = ws.get_book_link(soup)
        book_link2 = ws.get_book_link(soup2)

        asserted_link = 'http://www.buildeazy.com/plans/test.pdf'

        self.assertTrue(book_link, asserted_link)
        self.assertFalse(book_link2)

        content.close()
        content2.close()


    # def test_get_book_details(self):
    #     content = ws.get_content_from_file('pro-c-8-8th-edition.html')
    #     soup = ws.create_soup_from_url_content(content)
    #     book_details = ws.get_book_info(soup)
    #     # asserted_book_details = {'author': ' Andrew Troelsen,  Philip Japikse',
    #     #             'isbn': ' 1484230175',
    #     #             'year': ' 2017',
    #     #             'pages': ' 1372',
    #     #             'language': ' English',
    #     #             'file_size': ' 29.5 MB',
    #     #             'file_format': ' PDF',
    #     #             'category': ' C#'}
    #     asserted_book_details = [u' Andrew Troelsen, \u200e Philip Japikse',
    #                              u' 1484230175',
    #                              u' 2017',
    #                              u' 1372',
    #                              u' English',
    #                              u' 29.5 MB',
    #                              u' PDF',
    #                              u' C#']
    #     self.assertEqual(asserted_book_details, book_details)

    def test_get_category(self):
        content = ws.get_content_from_file('pro-c-8-8th-edition.html')
        soup = ws.create_soup_from_url_content(content)
        book_category = ws.get_category(soup).strip()
        asserted_category = 'C#'
        self.assertEqual(book_category, asserted_category)
        content.close()


if __name__ == '__main__':
    unittest.main()