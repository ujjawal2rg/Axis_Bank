
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Edge(executable_path="C:\Driver\edgedriver.exe")
driver.get("https://axazuatchatbotui.azurewebsites.net/")
driver.refresh()


driver.maximize_window()

print('page title is',driver.title)
print('Page Url',driver.current_url)
expectedTitle ='Axis Bank Virtual Assistant'
actualTitle = driver.title

print(actualTitle)

if expectedTitle==actualTitle:
    print('passed!')
else:
    print('Failed!')

driver.implicitly_wait(10)



driver.find_element_by_xpath("//div[contains(text(),'Transfer Money')]").click()
time.sleep(3)

driver.find_element_by_xpath("//button[contains(text(),'Transfer Money')]").click()
time.sleep(5)

#Debit Card
driver.find_element_by_xpath("//button[contains(text(),'Debit Card')]").click()
time.sleep(5)

#arrows-container
driver.find_element_by_xpath("//div[@class='arrows-container']/div[2]").click()

driver.find_element_by_xpath("//button[contains(text(),'Credit Card')]").click()
time.sleep(5)

#arrows-container
driver.find_element_by_xpath("//div[@class='arrows-container']/div[2]").click()
driver.find_element_by_xpath("//button[contains(text(),'Account Balance')]").click()
time.sleep(5)
#arrows-container
driver.find_element_by_xpath("//div[@class='arrows-container']/div[2]").click()
driver.find_element_by_xpath("//button[contains(text(),'Mini Statement')]").click()
time.sleep(5)
#arrows-container
driver.find_element_by_xpath("//div[@class='arrows-container']/div[2]").click()
driver.find_element_by_xpath("//button[contains(text(),'Cheque Services')]").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='arrows-container']/div[2]").click()
driver.find_element_by_xpath("//button[contains(text(),'ATM Locator')]").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='arrows-container']/div[2]").click()
driver.find_element_by_xpath("//button[contains(text(),'Branch Locator')]").click()

print("BottomSlider_Buttons are working fine >> Test pass !")

#driver.close()
