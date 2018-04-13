def get_file_name_of_url(url):
    file_name = url[(url.rfind('/')+1):]
    return file_name
