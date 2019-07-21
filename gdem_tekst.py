from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

browser = webdriver.Chrome() 
browser.get("http://suninjuly.github.io/explicit_wait2.html")

bot = browser.find_element_by_id("book")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR"))
		
bot.click()


#Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле.
#Не забудьте добавить этот код в начало вашего скрипта:
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
#Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
x = x_element.text
y = calc(x)


input = browser.find_element_by_id("answer")
input.send_keys(y)

browser.find_element_by_id("solve").click()




