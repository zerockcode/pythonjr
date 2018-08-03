
from datetime import time

from selenium import webdriver

driver = webdriver.Chrome('C:\zzz\chromedriver.exe')
driver.maximize_window()

driver.get("https://login.11st.co.kr/login/Login.tmall?returnURL=http%3A%2F%2Fwww.11st.co.kr%2Fhtml%2Fmain.html&xfrom=")

eleUserMessage = driver.find_element_by_id("loginName")
eleUserMessage.clear()
eleUserMessage.send_keys("aaaaa")

eleUserMessage = driver.find_element_by_id("passWord")
eleUserMessage.clear()
eleUserMessage.send_keys("bbbb")


eleShowMsgBtn=driver.find_element_by_css_selector('.btn_login')

print(eleShowMsgBtn)

eleShowMsgBtn.click()

eleYourMsg=driver.find_element_by_id("display")
assert "Test Python" in eleYourMsg.text


time.sleep(5000)

driver.close()