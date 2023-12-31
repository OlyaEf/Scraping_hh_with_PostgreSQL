import time

from database.query import create_tables
from loaders.data_loader import load_data
from src.config import config


def created_db_insert_tables():
    params = config(filename='../src/database.ini')
    db_hh = 'db_vacancies_hh'

    # Выбор конкретных 10 компаний
    selected_employers = [
        'ГК Innostage',
        'Яндекс',
        'Тензор',
        'ПИКАССО',
        'vk',
        'Циан',
        'Тинькофф',
        'BRANDPOL',
        'DIMEDIA',
        'ООО ВЗОР',
        'ООО Электронная медицина'
    ]

    # Создание таблиц в БД
    create_tables(db_hh, params)

    time.sleep(2)  # Задержка в секунду

    # Заполнение таблиц данными о выбранных компаниях и их вакансиях
    load_data(selected_employers, db_hh)


if __name__ == '__main__':
    created_db_insert_tables()
