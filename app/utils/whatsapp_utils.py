from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def send_whatsapp_message(contact, message):
    driver = webdriver.Chrome()  # You may need to adjust this based on your browser and WebDriver location
    driver.get("https://web.whatsapp.com/")
    
    time.sleep(10)  # Wait for the user to scan the QR code manually or use a library for QR code automation
    
    search_box = driver.find_element("xpath", "//div[@contenteditable='true']")
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    
    time.sleep(2)
    
    message_box = driver.find_element("xpath", "//div[@contenteditable='true']")
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    
    time.sleep(2)
    
    driver.quit()
