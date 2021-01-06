from selenium import webdriver
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def calc(a):
  return str(math.log(abs(12*math.sin(int(a)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button#book.btn.btn-primary")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = str(calc(x))

    placeholder = browser.find_element_by_css_selector("input#answer.form-control")
    placeholder.send_keys(y)

    submit = browser.find_element_by_css_selector("button#solve.btn.btn-primary")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
