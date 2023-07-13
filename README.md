# Проект: Получение данных о компаниях и вакансиях с сайта hh.ru

## Описание проекта

В рамках данного проекта мы получаем данные о компаниях и вакансиях с сайта hh.ru с использованием их публичного API и библиотеки `requests`. Затем мы проектируем таблицы в базе данных PostgreSQL для хранения полученных данных и загружаем данные в эти таблицы.

## Основные шаги проекта

1. Получение данных с сайта hh.ru: Мы используем публичное API hh.ru и библиотеку `requests` для получения данных о компаниях и вакансиях.
2. Выбор интересующих компаний: Мы выбираем не менее 10 интересных компаний, от которых мы будем получать данные о вакансиях по API.
3. Проектирование таблиц в базе данных: Мы спроектируем таблицы в базе данных PostgreSQL для хранения полученных данных о компаниях и вакансиях. Для работы с базой данных мы будем использовать библиотеку `psycopg2`.
4. Загрузка данных в базу данных: Мы реализуем код, который заполняет созданные таблицы в базе данных PostgreSQL данными о компаниях и вакансиях.
5. Создание класса `DBManager`: Мы создаем класс `DBManager`, который предоставляет методы для работы с данными в базе данных.

## Класс DBManager

```python
import psycopg2
from psycopg2.errors import UniqueViolation
from src.config import config

class DBManager:
    def __init__(self, database_name):
        self.params = config()
        self.params.update({'dbname': database_name})
        self.conn = psycopg2.connect(**self.params)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        # Метод для получения списка компаний и количества вакансий у каждой компании
        ...

    def get_all_vacancies(self):
        # Метод для получения списка всех вакансий с указанием компании, названия вакансии, зарплаты и ссылки на вакансию
        ...

    def get_avg_salary(self):
        # Метод для получения средней зарплаты по вакансиям
        ...

    def get_vacancies_with_higher_salary(self):
        # Метод для получения списка вакансий с зарплатой выше средней
        ...

    def get_vacancies_with_keyword(self, keyword):
        # Метод для получения списка вакансий, содержащих заданное ключевое слово в названии
        ...

    def insert_vacancies(self, vacancies):
        # Метод для добавления вакансий в базу данных
        ...

    def insert_employers(self, employers):
        # Метод для добавления компаний в базу данных
        ...

    def close_connection(self):
        # Метод для закрытия соединения с базой данных
        ...