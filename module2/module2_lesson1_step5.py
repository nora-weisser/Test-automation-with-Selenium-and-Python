#Task:
# 1. Open page: http://suninjuly.github.io/math.html.
# 2. Read the value of variable x
# 3. Calculate function(x)
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
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("span#input_value")
    x = x_element.text
    y = calc(x)

    result = browser.find_element_by_css_selector("input#answer.form-control")
    result.send_keys(y)

    checkbox = browser.find_element_by_css_selector("input#robotCheckbox.form-check-input")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("input#robotsRule.form-check-input")
    radiobutton.click()

    submit = browser.find_element_by_css_selector("button.btn.btn-default")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
