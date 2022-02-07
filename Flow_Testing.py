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

#arrows-container
driver.find_element_by_xpath("//div[@class='arrows-container']/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@class='arrows-container']/div[2]").click()
driver.find_element_by_xpath("//button[contains(text(),'Account Balance')]").click()
time.sleep(3)
driver.find_element_by_class_name("action-buttons").click()
time.sleep(5)
driver.find_element_by_id("username").send_keys("906260641")
driver.find_element_by_id("password").send_keys("d#demo123")
time.sleep(30)
print("wait for flow testing !!")

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

driver.find_element_by_id("msg-input").send_keys("find ATM")
driver.find_element_by_class_name("send-btn").click()  #Send Location

#driver.find_element_by_xpath("//button[contains(text(),'Send Location')]").click()


time.sleep(15)


driver.find_element_by_id("msg-input").send_keys("FIND BRANCH")
driver.find_element_by_class_name("send-btn").click()

#driver.find_element_by_xpath("//button[contains(text(),'Send Location')]").click()


#Amount=driver.find_element_by_xpath("").text()
#print("Amount:",Amount)


print(" IN  This we test the flow >> "
      "Account balance, "
      "Mini statement, "
      "Find branch , "
      "Find ATM, "
      "Credit card due,"
      "Credit TOTAL Limit,"
      "Available Credit Limit  >>")
#