#Task:
# 1. Open page http://suninjuly.github.io/get_attribute.html.
# 2. Search picture element which depicts a treasure chest
# 3. Extract <valuex> atribute from this element, that is equal x
# 4. Calculate function(x)
# 4. Enter answer to the text field
# 5. Click checkbox "I'm the robot".
# 6. Click radiobutton "Robots rule!".
# 7. Click to the button Submit.

from selenium import webdriver
import time
import math

def calc(a):
  return str(math.log(abs(12*math.sin(int(a)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    storage = browser.find_element_by_css_selector("img#treasure")
    x = storage.get_attribute("valuex")
    y = calc(x)

    result = browser.find_element_by_css_selector("input#answer")
    result.send_keys(y)

    checkbox = browser.find_element_by_css_selector("input#robotCheckbox.check-input")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("input#robotsRule.check-input")
    radiobutton.click()

    submit = browser.find_element_by_css_selector("button.btn.btn-default")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
