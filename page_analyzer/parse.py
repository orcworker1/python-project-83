from bs4 import BeautifulSoup


def parser_h1(html):
    soup = BeautifulSoup(html.text, "html.parser")
    h1 = soup.h1.string if soup.h1 else ""
    return h1


def parser_title(html):
    soup = BeautifulSoup(html.text, "html.parser")
    title = soup.title.string if soup.title else ""
    return title


def parser_description(html):
    soup = BeautifulSoup(html.text, "html.parser")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    description = meta_desc["content"] if meta_desc else "Нет описания"
    return description





