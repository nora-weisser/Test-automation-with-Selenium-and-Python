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
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
