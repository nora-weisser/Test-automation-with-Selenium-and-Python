#Task:
# 1. Open the page http://suninjuly.github.io/redirect_accept.html
# 2. Press the button
# 3. Switch to new tab
# 4. Pass the captcha for the robot and get the answer number

from selenium import webdriver
import time
import math

def calc(a):
  return str(math.log(abs(12*math.sin(int(a)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = str(calc(x))

    placeholder = browser.find_element_by_css_selector("input#answer.form-control")
    placeholder.send_keys(y)

    submit = browser.find_element_by_css_selector("button.btn.btn-primary")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
