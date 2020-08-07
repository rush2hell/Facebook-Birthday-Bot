from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

webpage = webdriver.Chrome()

webpage.get("https://facebook.com")

email = webpage.find_element_by_id("email")
email.send_keys("rushabhfight@gmail.com")

password = webpage.find_element_by_id("pass")
password.send_keys(")(*&^%$#@!!@#$%^&*()")

login = webpage.find_element_by_id("u_0_b")
login.click()

time.sleep(10)
webpage.get("https://www.facebook.com/events/birthdays/")


find_text = webpage.find_element_by_xpath("//textarea[@title='Write a birthday wish on his timeline...']")

find_text.send_keys("Happy Birthday, good wishes")
find_text.send_keys(Keys.ENTER)
webpage.refresh()


