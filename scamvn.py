from bs4 import BeautifulSoup
import requests
import csv
 
def crawlData(url):
    links = []
    for i in range(10):
        _url = url + "?trang={i}".format(i=i)
        response = requests.get(_url)
        soup = BeautifulSoup(response.content, "html.parser")
        domain = soup.findAll('a', attrs={
            "data-placement":"top",
            "data-toggle":"tooltip"
        })
        links += [link.text for link in domain]

    f = open('./scamvn.csv', 'w', encoding='UTF-8')
    writer = csv.writer(f)
    writer.writerow(links)
    f.close()


if __name__ == "__main__":
    crawlData("https://scamvn.com/danh-sach")