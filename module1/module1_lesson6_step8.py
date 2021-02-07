#Task: write program which allows you to register oon web-site http://suninjuly.github.io/registration1.html. Use assert for checking of message about successful rregistration

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # This code filles in all fields
    input1 = browser.find_element_by_css_selector("div.first_block>div.form-group.first_class>input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block>div.form-group.second_class>input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block>div.form-group.third_class>input.form-control.third")
    input3.send_keys("aaa@yandex.ru")

    # Send form
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

    # Check that we could register
    # waiting for page downloading
    time.sleep(1)

    # look for element, which contain text
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # using assert check that expected text is equal to text on web-site page
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()