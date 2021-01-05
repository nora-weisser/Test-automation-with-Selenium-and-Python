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
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
