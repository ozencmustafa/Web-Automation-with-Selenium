from selenium import webdriver

import time

import login

import js2py

browser = webdriver.Chrome()
browser.get("https://www.instegram.com/")

time.sleep(2)

advanced = browser.find_element_by_xpath("//*[@id='details-button']")
advanced.click()
proceed = browser.find_element_by_xpath("//*[@id='proceed-link']")
proceed.click()
time.sleep(1)

username = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

username.send_keys(login.username)
password.send_keys(login.password)
time.sleep(1)


login =  browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]")
login.click()
time.sleep(5)

save =  browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/section/div/button")
save.click()
time.sleep(5)
not_now =  browser.find_element_by_css_selector(".aOOlW.HoLwm")
not_now.click()

probutton = browser.find_element_by_xpath(".//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/a")
probutton.click()

buttonlist = browser.find_elements_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
time.sleep(2)

print(buttonlist)
#buttonlist[1].click()

for each in buttonlist:
    print(each.text)


##jscommand = """
##liste = document.body.querySelector("._8-yf5");
##"""
##
##liste = browser.execute_script(jscommand)
##
##print(liste)


