import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4

def get_results(search_term):
    url = "https://www.bing.com/news/search?q=coronavirus+northern+ireland&FORM=HDRSC6s"

    browser = webdriver.Chrome()
    browser.get(url)
    wait = WebDriverWait(browser, 100)
    browser.implicitly_wait(100)

    search_box = browser.find_element_by_xpath("(//input[contains(@class,'b_searchbox')])[1]")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.submit()

    links = browser.find_elements_by_xpath("//a[@class='title']")
    #links = browser.find_elements_by_xpath("//div[@class='r']//a")
    results = []

    for link in links:
        href = link.get_attribute("href")
        results.append(href)
        print(href)

    return print(results)


get_results("Coronavirus Northern Ireland")



