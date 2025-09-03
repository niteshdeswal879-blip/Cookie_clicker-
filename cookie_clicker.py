from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

language=driver.find_element(By.ID,value="langSelect-EN")
language.click()

sleep(1)
cookie=driver.find_element(By.CSS_SELECTOR, value='#bigCookie')

sleep(3)
cursor=driver.find_element(By.ID, value='productPrice0')
print(cursor.text)

five_min=time()+ 60*8
wait_time=30
timeout=time()+wait_time

while True:
    cookie.click()
    # driver.execute_script("arguments[0].click()",cookie)

    if time()>timeout:
        try:
            product = driver.find_elements(by=By.CSS_SELECTOR, value=".product.unlocked.enabled")

            for you in reversed(product):
                if "enabled" in you.get_attribute("class"):
                    you[-1].click()

        except:
            pass

        timeout=time()+wait_time

    if time()>five_min:
        cookies=driver.find_element(by=By.ID,value="cookies")
        coc=cookies.text.split("\n")[1]
        print(coc)

        break





