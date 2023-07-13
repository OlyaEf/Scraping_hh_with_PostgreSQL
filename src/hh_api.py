from dataclasses import dataclass
from typing import Any, List, Dict
import requests


@dataclass
class Employer:
    id: int
    name: str
    url: str


@dataclass
class Vacancy:
    id: int
    employer_id: int
    name: str
    salary_from: int
    salary_to: int
    description: str
    requirement: str
    area: str
    alternate_url: str


class HeadHunterAPI:
    vacancies_url = 'https://api.hh.ru/vacancies'
    employers_url = 'https://api.hh.ru/employers'

    def __init__(self, keyword: str = None) -> None:
        self.params: Dict[str, Any] = {
            'area': '113',
            'text': keyword,
            'search_field': 'company_name',
            'per_page': 100,
            'page': 0,
            'only_with_vacancies': True
        }
        self._headers: Dict[str, str] = {'User-Agent': 'HH-User-Agent'}
        self.list_of_vacancies: List[Vacancy] = []
        self.list_of_employers: List[Employer] = []

    def get_request(self, url: str) -> List[Dict[str, Any]]:
        response = requests.get(url, params=self.params, headers=self._headers)
        return response.json()['items']

    def created_vacancy(self, vacancies: list):
        self.list_of_vacancies = [
            Vacancy(
                id=vacancy['id'],
                employer_id=vacancy.get('employer', {}).get('id'),
                name=vacancy['name'],
                salary_from=vacancy['salary']['from'] if vacancy['salary'] else None,
                salary_to=vacancy['salary']['to'] if vacancy['salary'] else None,
                description=vacancy['snippet']['responsibility'] if vacancy['snippet']['responsibility'] else 'no data',
                requirement=vacancy['snippet']['requirement'] if vacancy['snippet']['requirement'] else 'no data',
                area=vacancy['area']['name'],
                alternate_url=vacancy['alternate_url']
            )
            for vacancy in vacancies
        ]

        return self.list_of_vacancies

    def created_employer(self, vacancies: list):
        ids = []
        for employer in vacancies:
            if employer['employer']['id'] not in ids:
                ids.append(employer['employer']['id'])
                self.list_of_employers.append(
                    Employer(
                        id=int(employer['employer']['id']),
                        name=employer['employer']['name'],
                        url=employer['employer']['alternate_url']
                    )
                )

        return self.list_of_employers

    def get_vacancies_by_employer_name(self, employer_name: str):
        self.params['text'] = employer_name
        vacancies_json = self.get_request(self.vacancies_url)

        return vacancies_json
