from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from rich import print


chrome_options = Options()
#chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)


dork = "/wp-admin"
domain = "https://yourwordpresswebsite.com"


starten1 = browser.get(domain+dork)
time.sleep(1)
print("[blue] WP ADMIN OPEN")


einloggenemail = browser.find_element(By.ID, "user_login")
einloggenemail.send_keys("#####USERNAME#####")

einloggenpasswort = browser.find_element(By.ID, "user_pass")
einloggenpasswort.send_keys("#####PASSWORD#####")

loginbtn1 = browser.find_element(By.ID, "wp-submit")
loginbtn1.click()
time.sleep(2)

print("[green] SUCCESFUL LOGIN")



designauswahl1 = browser.find_element(By.CSS_SELECTOR, "#menu-appearance > a > div.wp-menu-name")
designauswahl1.click()
time.sleep(1)


themehinzufuegen1 = browser.find_element(By.CSS_SELECTOR, "#wpbody-content > div.wrap > a")
themehinzufuegen1.click()
time.sleep(1)


themesuche = browser.find_element(By.ID, "wp-filter-search-input")
themesuche.send_keys("Astra")
time.sleep(3)



installclick1 = browser.find_element(By.CSS_SELECTOR, "#wpbody-content > div.wrap > div.theme-browser.content-filterable.rendered > div > div:nth-child(1)")
installclick1.click()
time.sleep(1)


installclick2 = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[5]/div[1]/div[1]/a")
installclick2.click()
time.sleep(1)
print("[green] THEME SUCCESFULLY INSTALLED")


time.sleep(30)

themeaktivieren = browser.find_element(By.LINK_TEXT, "Aktivieren")
themeaktivieren.click()
time.sleep(1)
