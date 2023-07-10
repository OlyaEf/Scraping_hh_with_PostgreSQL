from src.hh_api import HeadHunterAPI
from database.db_manager import DBManager


def load_data(selected_employers):
    hh = HeadHunterAPI()
    db_manager = DBManager()

    for employer_name in selected_employers:
        employer = hh.get_employer(employer_name)
        employer_id = employer.id

        vacancies = hh.get_vacancy(employer_id)
        db_manager.insert_vacancy(vacancies)

    db_manager.close_connection()
