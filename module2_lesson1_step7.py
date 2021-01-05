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
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
