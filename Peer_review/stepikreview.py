from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    first = browser.find_element_by_css_selector('div.first_block .form-control.first')
    first.send_keys("Name")
    last = browser.find_element_by_css_selector('div.first_block .form-control.second')
    last.send_keys("Last name")
    email = browser.find_element_by_css_selector('div.first_block .form-control.third')
    email.send_keys("Email@mail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(1)
    browser.quit()