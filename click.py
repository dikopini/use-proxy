from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('E:/RWID/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service = s)

url = 'https://kemdikbud.go.id/main'
driver.get(url)

link = driver.find_element(By.LINK_TEXT, 'Berita')
link.click()

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="content"]'))
    )
    print('berita dari kemendikbud')
    articles = main.find_elements(By.XPATH, '//article[@class="single_post"]')
    i = 0
    for article in articles:
        headers = article.find_elements(By.XPATH, '//div[@class="col-lg-12"]/h5/strong/a')[i].text
        print(headers)
        i += 1
    driver.back()

    print('')
    print('')

    ling = driver.find_element(By.LINK_TEXT, 'Pengumuman')
    ling.click()

    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="content"]'))
    )

    print('pengumuman dari kemendikbud')
    articles = main.find_elements(By.XPATH, '//article[@class="single_post"]')
    i = 0
    for article in articles:
        headers = article.find_elements(By.XPATH, '//div[@class="col-lg-12"]/h5/strong/a')[i].text
        print(headers)
        i += 1
    driver.back()

except:
    driver.quit()