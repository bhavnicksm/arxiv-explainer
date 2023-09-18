import re

def check_valid_url(text):

    url_pattern = r'https?://\S+'

    if re.match(url_pattern, text):
        return True
    else:
        return False


def check_arxiv_url(text):
    arxiv_pattern = r'https?://arxiv.org/\S+'
    # url = "https://arxiv.org/abs/2103.12345"

    if re.match(arxiv_pattern, text):
        return True
    else:
        return False
