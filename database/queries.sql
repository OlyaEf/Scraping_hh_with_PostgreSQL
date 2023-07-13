-- Получает список всех компаний и количество вакансий у каждой компании:
SELECT employers.name, COUNT(vacancies.id) AS vacancies_count
FROM employers
LEFT JOIN vacancies ON employers.id = vacancies.employer_id
GROUP BY employers.name;

-- Получает список всех вакансий с указанием названия компании, названия вакансии, зарплаты и описание вакансию:
SELECT e.name, v.name, v.salary_from, v.description
FROM vacancies v
INNER JOIN employers e on v.employer_id = e.id;

-- Получает среднюю зарплату по вакансиям:
SELECT round(AVG(CAST(vacancies.salary_from AS FLOAT))) AS average_salary
FROM vacancies;

-- Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям:
SELECT *
FROM vacancies
WHERE CAST(vacancies.salary_from AS numeric) > (SELECT round(AVG(CAST(vacancies.salary_from AS FLOAT))) FROM vacancies);

-- Получает список всех вакансий, в названии которых содержатся переданные в метод слова:
SELECT *
FROM vacancies
WHERE LOWER(vacancies.name) LIKE LOWER('%python%');

