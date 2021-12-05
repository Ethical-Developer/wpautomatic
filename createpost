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



neuerpost1 = browser.find_element(By.NAME, "post_title")
neuerpost1.send_keys("Hello, this is a New Post")


inhaltpost = browser.find_element(By.NAME, "content")
inhaltpost.send_keys("Hello World")

speichern1 = browser.find_element(By.NAME, "save")
speichern1.click()
time.sleep(2)

print("[green] POST SUCCESFUL POSTED")



beitraege = browser.find_element(By.CSS_SELECTOR, "#menu-posts > a > div.wp-menu-name")
beitraege.click()
