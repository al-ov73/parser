import time
from selenium import webdriver as wd
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


url = "https://www.avito.ru/ulyanovsk/kvartiry/prodam/4-komnatnye/vtorichka-ASgBAgICA0SSA8YQ5geMUsoIhlk?district=389"

options = wd.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
browser = wd.Chrome(options=options)
browser.get(url)
time.sleep(1)
browser.save_screenshot("parser/screenshots/avito/1.png")
# open_search = browser.find_element(By.CLASS_NAME, "header_search")
# open_search.click()
# time.sleep(1)
# browser.save_screenshot("2.png")
# # регистрируем текстовое поле и имитируем ввод строки "Git"
# search = browser.find_element(By.CLASS_NAME, "search-modal_input")
# search.send_keys("Git")

# # ставим на паузу, чтобы страница прогрузилась
# time.sleep(3)
# browser.save_screenshot("3.png")
# загружаем страницу и извлекаем ссылки через атрибут rel
soup = BeautifulSoup(browser.page_source, 'lxml')
posters = \
   soup.find_all('div', {'class': 'iva-item-content-rejJg'})[:5]

# форматируем результа
for poster in posters:
    h3 = poster.find('h3')
    if h3:
        print(h3.contents[0].replace('\xa0', ''))
    a = poster.find('a', href=True)
    if a:
        # print(a['title'])
        print(f"https://www.avito.ru{a['href']}")
    price = poster.find(itemprop="price").get('content')
    if price:
        print('{0:,}'.format(int(price),",").replace(',', ' '))
    # print(poster.next_element['title'], ,' ', poster[])
    # print(f"https://www.avito.ru{poster['href']}")
