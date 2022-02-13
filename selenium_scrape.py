from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


s = Service('E:/RWID/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service = s)

url = 'https://www.kemdikbud.go.id/main/blog/category/berita'
driver.get(url)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="content"]'))
    )
    articles = main.find_elements(By.XPATH, '//article[@class="single_post"]')
    i = 0
    for article in articles:
        headers = article.find_elements(By.XPATH, '//div[@class="col-lg-12"]/h5/strong/a')[i].text
        print(headers)
        i += 1
finally:
    driver.quit()
