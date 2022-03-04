from selenium import webdriver

import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # search button
    button = browser.find_element_by_tag_name("button")
    button.click()

    # switch to alert
    alert = browser.switch_to.alert
    alert.accept()

    # присваиваем значение в переменную
    x = int(browser.find_element_by_xpath("//span[@id='input_value']").text)

    # считаем
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    # input data
    input = browser.find_element_by_xpath("//input[@class='form-control']")
    input.send_keys(y)

    # инициализируем кнопку
    button = browser.find_element_by_tag_name("button")

    # zhmyak
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()