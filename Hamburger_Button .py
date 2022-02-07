
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

driver.find_element_by_class_name("burger-icon").click()


#My Axis Bank
driver.find_element_by_xpath("//h3[contains(text(),'My Axis Bank')]").click()
driver.find_element_by_xpath("//li[contains(text(),'Account Balance')]").click()
time.sleep(5)
driver.find_element_by_class_name("burger-icon").click()
driver.find_element_by_xpath("//li[contains(text(),'Mini Statement')]").click()
time.sleep(5)
driver.find_element_by_class_name("burger-icon").click()
driver.find_element_by_xpath("//li[contains(text(),'Credit Card Due Date')]").click()
time.sleep(5)
driver.find_element_by_class_name("burger-icon").click()
driver.find_element_by_xpath("//li[contains(text(),'Credit Card Due')]").click()
time.sleep(5)
driver.find_element_by_class_name("burger-icon").click()
driver.find_element_by_xpath("//li[contains(text(),'Total Credit Limit')]").click()
time.sleep(5)
driver.find_element_by_class_name("burger-icon").click()
driver.find_element_by_xpath("//li[contains(text(),'Available Credit Limit')]").click()
time.sleep(5)
#Transactions
driver.find_element_by_class_name("burger-icon").click()
driver.find_element_by_xpath("//h3[contains(text(),'Transactions')]").click()
driver.find_element_by_xpath("//li[contains(text(),'Transfer Fund')]").click()
time.sleep(5)
driver.find_element_by_class_name("burger-icon").click()
driver.find_element_by_xpath("//li[contains(text(),'Pay Credit Card Bill')]").click()

time.sleep(5)
#Service Requests
driver.find_element_by_class_name("burger-icon").click()
driver.find_element_by_xpath("//h3[contains(text(),'Service Requests')]").click()
driver.find_element_by_xpath("//li[contains(text(),'Order Cheque Book')]").click()
time.sleep(5)
driver.find_element_by_class_name("burger-icon").click()
driver.find_element_by_xpath("//li[contains(text(),'Block Card')]").click()
#close Button
driver.find_element_by_class_name("burger-icon").click()
time.sleep(2)
driver.find_element_by_css_selector("button[class='close-icon']").click()

print("Hamburger buttons are working fine >> Test pass !")

driver.close()
