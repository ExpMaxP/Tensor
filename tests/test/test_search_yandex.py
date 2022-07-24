import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_search_main():
    BASE_URL = 'https://yandex.ru/'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(BASE_URL)

    linkYandex = driver.find_element(By.XPATH, '//a[@class ="home-link home-logo__link"]').get_attribute("href")
    buttonSearch = driver.find_element(By.ID, 'text')
    buttonSearch.send_keys("Тензор")

    time.sleep(0.5)
    subMenu = driver.find_elements(By.XPATH, "//ul[@Role='listbox']/li")

    time.sleep(2)
    buttonSearch.send_keys(Keys.ENTER)

    time.sleep(0.5)
    searchResult = driver.find_elements(By.XPATH, '//ul[@id="search-result"]/li[1]')

    assert BASE_URL == linkYandex, f" BaseUrl {BASE_URL} =! LinkUrl {linkYandex}"
    assert len(subMenu) > 0, f"Number submenu  is not > 0 ( {len(subMenu)} )"
    assert searchResult[0].text.__contains__("tensor.ru"), f"First web link is not contains (tensor.ru)"

    driver.quit()


def test_yandex_pictures():
    BASE_URL = 'https://yandex.ru/'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(BASE_URL)
    time.sleep(1)

    driver.find_element(By.XPATH, '//div[@class="services-new__icon services-new__icon_images"]').click()

    driver.switch_to.window(driver.window_handles[1])

    linkPageImages = driver.find_element(By.XPATH, '//head/link[@rel="alternate"]').get_attribute("href")

    time.sleep(2)
    driver.find_element(By.XPATH, '//div[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]').click()

    """get value"""
    valueFieldSearch = driver.find_element(By.NAME, 'text').get_attribute('value')

    time.sleep(1)

    lidtPictures = driver.find_elements(By.XPATH, "//a[@class= 'serp-item__link']")
    lidtPictures[0].click()

    driver.find_element(By.XPATH, '//div[contains(@class, "CircleButton_type_next")]').click()


    assert linkPageImages.__contains__("https://yandex.ru/images/"), \
        f"{linkPageImages} is not contains (https://yandex.ru/images/) "
    assert valueFieldSearch is not None

    driver.quit()

