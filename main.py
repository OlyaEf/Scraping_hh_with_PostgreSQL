from database.db_manager import DBManager


def main():
    # Создаем экземпляр класса DBManager
    db_manager = DBManager("db_vacancies_hh")

    while True:
        print("Выберите действие:")
        print("1. Получить список всех компаний и количество вакансий у каждой компании")
        print("2. Получить список всех вакансий")
        print("3. Получить среднюю зарплату по вакансиям")
        print("4. Получить список вакансий с зарплатой выше средней")
        print("5. Получить список вакансий по ключевому слову")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            # Получить список всех компаний и количество вакансий
            companies_vacancies = db_manager.get_companies_and_vacancies_count()
            print("Список компаний и количество вакансий:")
            for company, count in companies_vacancies:
                print(f"Компания: {company}, Количество вакансий: {count}")
            print()

        elif choice == "2":
            # Получить список всех вакансий
            all_vacancies = db_manager.get_all_vacancies()
            print("Список всех вакансий:")
            for company, vacancy, salary_from, alternate_url in all_vacancies:
                print(f"Компания: {company}, Вакансия: {vacancy}, Зарплата: {salary_from}, URL: {alternate_url}")
            print()

        elif choice == "3":
            # Получить среднюю зарплату по вакансиям
            avg_salary = db_manager.get_avg_salary()
            print(f"Средняя зарплата: {round(avg_salary)}")
            print()

        elif choice == "4":
            # Получить список вакансий с зарплатой выше средней
            high_salary_vacancies = db_manager.get_vacancies_with_higher_salary()
            print("Список вакансий с зарплатой выше средней:")
            for vacancy in high_salary_vacancies:
                print(vacancy)  # Предполагается, что vacancy - это кортеж с данными вакансии
            print()

        elif choice == "5":
            # Получить список вакансий по ключевому слову
            keyword = input("Введите ключевое слово: ")
            keyword_vacancies = db_manager.get_vacancies_with_keyword(keyword)
            print(f"Список вакансий с ключевым словом '{keyword}':")
            for vacancy in keyword_vacancies:
                print(vacancy)  # Предполагается, что vacancy - это кортеж с данными вакансии
            print()

        elif choice == "0":
            # Выход из программы
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")

    # Закрываем соединение с базой данных
    db_manager.close_connection()


if __name__ == "__main__":
    main()
