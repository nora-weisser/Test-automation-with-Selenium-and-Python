#Task: Write code that implements the following scenario:
# 1. Open the page http://suninjuly.github.io/selects1.html
# 2. Calculate the sum of the given numbers
# 3. Select in the drop-down list a value equal to the calculated amount
# 4. Press the "Submit" button

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element_by_css_selector("span#num1.nowrap")
    x = int(x_value.text)

    y_value = browser.find_element_by_css_selector("span#num2.nowrap")
    y = int(y_value.text)

    result = str(int(x) + int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)

    submit = browser.find_element_by_css_selector("button.btn.btn-default")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
