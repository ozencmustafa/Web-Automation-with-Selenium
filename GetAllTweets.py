from selenium import webdriver
import login
import time
browser = webdriver.Chrome()
browser.get("https://twitter.com/login")
time.sleep(3)
username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")

username.send_keys(login.username)
password.send_keys(login.password)
time.sleep(1)

giris = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div/div")
giris.click()
time.sleep(2)
search = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]")
search.click()
searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")
searchArea.send_keys('yazilimayolver')

searchArea.send_keys(u'\ue007')
time.sleep(5)




tweets = []

"""
Javascript code scroll icin kullanildi
"""
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
##""" Tekrar Python """
    elements = browser.find_elements_by_css_selector(".css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0")
    for e in elements:
        tweets.append(e.text)
##""" Java script """
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)



tweetCount = 1
with open("twits.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("***************************************\n")
        tweetCount += 1
        
        
            



time.sleep(15)

##browser.close()


