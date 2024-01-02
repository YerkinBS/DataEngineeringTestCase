# Погодная Аналитика

### Содержание

- [Погодная Аналитика](#погодная-аналитика)
    - [Описание](#описание)
    - [Структура Проекта](#структура-проекта)
        - [Сбор Данных](#сбор-данных)
        - [Анализ Данных](#анализ-данных)
        - [Результаты](#результаты)
    - [Визуализация Данных](#визуализация-данных)
        - [1. График Средней Температуры за Месяц](#1-график-средней-температуры-за-месяц)
        - [2. Гистограмма Дневной Температуры](#2-гистограмма-дневной-температуры)
        - [3. График Средней Температуры по Дням Недели](#3-график-средней-температуры-по-дням-недели)
        - [4. Суточные Тенденции Температуры](#4-суточные-тенденции-температуры)
        - [5. Дневная Температура vs Ночная Температура](#5-дневная-температура-vs-ночная-температура)
        - [6. Распределение Погодных Условий 1.0](#6-распределение-погодных-условий-10)
        - [7. Распределение Погодных Условий 2.0](#7-распределение-погодных-условий-20)
    - [Запуск Проекта](#запуск-проекта)

### Описание
Проект представляет собой увлекательное погружение в анализ погоды с использованием Selenium для сбора данных и библиотек Pandas и Matplotlib для визуализации. Отслеживайте среднюю температуру месяца, распределение дневных температур и другие погодные паттерны, создавая гармонию в визуализации погодных явлений.

### Структура Проекта
##### Сбор Данных

- `weather_parser.py`: Веб-скрипт, использующий библиотеку Selenium, для сбора данных о погоде за месяц с [Yandex Погода](https://yandex.kz/pogoda/month?lat=43.273564&lon=76.914851&via=hnav).

##### Анализ Данных

- `weather_analysis.ipynb`: Jupyter Notebook с использованием библиотек Pandas, Matplotlib и Seaborn для анализа собранных данных о погоде.

##### Результаты

- Файл `weather_data.csv` содержит собранные данные о погоде, включая дневные и ночные температуры, день недели и погодные условия.

### Визуализация Данных

##### 1. График Средней Температуры за Месяц
   - Интерактивный график, отображающий среднюю температуру на протяжении месяца.
   - Данные представлены для каждой даты в месяце с помощью точек.

##### 2. Гистограмма Дневной Температуры
   - Гистограмма, показывающая распределение дневных температур за месяц.
   - Данные разбиты на 10 бинов для наглядности.

##### 3. График Средней Температуры по Дням Недели
   - Столбчатая диаграмма, представляющая среднюю температуру по дням недели.
   - Дни недели расставлены в правильном порядке.

##### 4. Суточные Тенденции Температуры
   - График, отображающий изменения дневной и ночной температуры на протяжении месяца.
   - Данные представлены для каждой даты, отмечены цветами для дневной и ночной температуры.

##### 5. Дневная Температура vs Ночная Температура
   - Скаттер-плот, иллюстрирующий взаимосвязь между дневной и ночной температурой.
   - Каждая точка представляет конкретный день месяца.

##### 6. Распределение Погодных Условий 1.0
   - Круговая диаграмма, отображающая распределение различных погодных условий за месяц.
   - Процентное соотношение различных условий представлено на диаграмме.

##### 7. Распределение Погодных Условий 2.0
   - Столбчатая диаграмма, представляющая распределение различных погодных условий за месяц.
   - Количество дней для каждого условия отображено на диаграмме.

*Примечание: Все графики созданы с использованием библиотек Pandas и Matplotlib.*


### Запуск Проекта

1. Для запуска и визуализации кода требуются следующие библиотеки Python:

    - selenium
    - datetime
    - csv
    - re
    - jupyter
    - pandas
    - matplotlib
    - seaborn

    Вы можете установить их, выполнив следующие команды в вашем терминале:

    ```bash
    pip install *название библиотеки*
    ```
2. Запустите `weather_parser.py` для сбора данных.
3. Запустите `weather_analysis.ipynb` для анализа и визуализации данных.