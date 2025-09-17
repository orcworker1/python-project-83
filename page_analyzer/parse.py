from bs4 import BeautifulSoup


def parser(html):
    soup = BeautifulSoup(html.text, "html.parser")
    h1 = soup.h1.string if soup.h1 else ""
    title = soup.title.string if soup.title else ""
    meta_desc = soup.find("meta", attrs={"name": "description"})
    description = meta_desc["content"] if meta_desc else ""
    return h1, title, description


