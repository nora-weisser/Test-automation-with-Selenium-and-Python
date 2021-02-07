#Task:
# 1. Open the page http://SunInJuly.github.io/execute_script.html.
# 2. Read value for variable x.
# 3. Calculate a mathematical function of x.
# 4. Scroll down the page.
# 5. Enter your answer in the text box.
# 6. Select the checkbox "I'm the robot".
# 7. Toggle the radiobutton "Robots rule!"
# 8. Click on the "Submit" button.

from selenium import webdriver
import time
import math


def calc(a):
  return str(math.log(abs(12*math.sin(int(a)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_value.text

    y = str(calc(x))

    placeholder = browser.find_element_by_css_selector("input#answer.form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", placeholder)
    placeholder.send_keys(y)

    checkbox = browser.find_element_by_css_selector("input#robotCheckbox.form-check-input")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("input#robotsRule.form-check-input")
    radiobutton.click()

    submit = browser.find_element_by_css_selector("button.btn.btn-primary")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
