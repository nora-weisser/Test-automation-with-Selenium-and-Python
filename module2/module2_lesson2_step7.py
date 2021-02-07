#Task:
# 1. Open the page http://suninjuly.github.io/file_input.html
# 2. Fill in the text fields: first name, last name, email
# 3. Upload file. The file must have a .txt extension and may be empty
# 4. Press the "Submit" button

from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("aaa@yandex.ru")

    txtfile = browser.find_element_by_name("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    txtfile.send_keys(file_path)

    submit = browser.find_element_by_css_selector("button.btn.btn-primary")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
