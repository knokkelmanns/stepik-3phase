# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")
    driver.get(link)

    input1 = driver.find_element_by_xpath("/html/body/div/form/div/input[1]").send_keys('Вася')
    input2 = driver.find_element_by_xpath("/html/body/div/form/div/input[2]").send_keys('Кика')
    input3 = driver.find_element_by_xpath("/html/body/div/form/div/input[3]").send_keys('test@test.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '0mb-file.txt')
    input4 = driver.find_element_by_xpath("// *[@id='file']").send_keys(file_path)

    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
