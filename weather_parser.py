from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import csv
import re

URL = 'https://yandex.kz/pogoda/month?lat=43.273564&lon=76.914851&via=hnav'

def format_date(date):
    try:
        date = date.split()
        day, month = date[0], date[1]
        month_mapping = {
            'января': 1,
            'февраля': 2,
            'марта': 3,
            'апреля': 4,
            'мая': 5,
            'июня': 6,
            'июля': 7,
            'августа': 8,
            'сентября': 9,
            'октября': 10,
            'ноября': 11,
            'декабря': 12
        }
        month = month_mapping[month]
        return datetime.now().replace(month=month, day=int(day)).strftime('%d.%m')
    except Exception as e:
        print(f'Error formatting date: {e}')
        return None


driver = webdriver.Chrome()
driver.get(URL)

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "climate-calendar__cell")))

calendar__cells = driver.find_elements(By.CLASS_NAME, "climate-calendar__cell")
weather_data = []

for cell in calendar__cells:
    try:
        overall_info = driver.execute_script("return arguments[0].innerText;", cell.find_element(By.CLASS_NAME, "a11y-hidden")) 
        date = re.search(r'(\d{1,2}\s[а-я]+)', overall_info).group(1)
        day_temp = re.search(r'днём,\s*(-?\d+)\s*°', overall_info).group(1)
        night_temp = re.search(r'ночью,\s*(-?\d+)\s*°', overall_info).group(1)
        week_day = re.search(r'([а-я]+)\.', overall_info).group(1)
        weather_condition = re.search(r'ночью,\s*(-?\d+)\s*°;\s*(.+)$', overall_info).group(2).capitalize()

        weather_data.append({
            'Дата': format_date(date),
            'Дневная температура': day_temp,
            'Ночная температура': night_temp,
            'День недели': week_day,
            'Погодные условия': weather_condition
        })
    except Exception as e:
        print(f'Error: {e}')

csv_file = 'weather_data.csv'
fieldnames = ['Дата', 'Дневная температура', 'Ночная температура', 'День недели', 'Погодные условия']

with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(weather_data)
    print('~' * 50)
    print(f'Файл {csv_file} успешно создан!')
    print('~' * 50)

driver.quit()