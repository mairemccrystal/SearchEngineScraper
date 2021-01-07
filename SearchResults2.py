import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4

def get_results(search_term):
    url = "https://www.bing.com/news/search?q=coronavirus+northern+ireland&FORM=HDRSC6s"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)

    search_box = browser.find_element_by_xpath("(//input[contains(@class,'b_searchbox')])[1]")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.submit()

    links = browser.find_elements_by_xpath("//a[@class='title']")
    results = []
    urltext = []

    for link in links:
        href = link.get_attribute("href")
        urlwords = link.text
        results.append(href)
        urltext.append(urlwords)

    #return urltext
    return results


def get_words(search_term):
    url = "https://www.bing.com/news/search?q=coronavirus+northern+ireland&FORM=HDRSC6s"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)

    search_box = browser.find_element_by_xpath("(//input[contains(@class,'b_searchbox')])[1]")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.submit()

    links = browser.find_elements_by_xpath("//a[@class='title']")
    results = []
    urltext = []

    for link in links:
        href = link.get_attribute("href")
        urlwords = link.text
        results.append(href)
        urltext.append(urlwords)

    return urltext
    #return results


get_results("Coronavirus Northern Ireland")



