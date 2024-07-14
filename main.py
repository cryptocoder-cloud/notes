"""
Модуль содержит функции для управления заметками.

Автор: cryptocoding
Дата создания: 03.03.2024
"""
import os
import sys

from modules.database import Manager

manager = Manager()


def clear_console():
    '''
    Функция для очистки консоли.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def close_script():
    '''
    Функция для завершения скрипта.
    '''
    sys.exit()


def main():
    '''
    Функция для основного меню программы.
    '''
    while True:
        clear_console()
        print('''Выбирете действие:
    1. Добавить заметку
    2. Поиск заметок
    3. Список всех заметок

    4. Выйти
    ''')

        while True:
            try:
                answer = int(input('>>>'))
                if answer < 1 or answer > 4:
                    raise ValueError
                break  # Выход из цикла при корректном вводе
            except ValueError:
                print('Укажите правильное значение.')

        function_dict = {
            1: add_note,
            2: search_notes,
            3: find_all_notes,
            4: close_script,
        }

        choose_function = function_dict.get(answer)
        if choose_function:
            choose_function()
        else:
            print('Неправильный выбор. Повторите попытку.')


def add_note():
    '''
    Функция для добавления новой заметки.
    '''
    clear_console()
    title = input('Укажите заголовок: ')
    text = input('Укажите содержание заметки:\n')
    if not title or not text:
        return
    print(manager.add_note(title, text))


def search_notes():
    '''
    Функция для поиска и просмотра заметок по ключевому слову.
    '''
    clear_console()
    keyword = input('Укажите ключевое слово: ')
    search_results = manager.search_notes(keyword)

    if search_results:
        print(f"Результаты поиска по ключевому слову '{keyword}':\n")
        for note_id, note_title in search_results:
            print(f"{note_id}. Заголовок: {note_title}")

        while True:
            number_notes = input('\nУкажите номер заметки для просмотра содержания, 0 для выхода в меню\n>>>')
            if number_notes == '0':
                return

            try:
                number = int(number_notes)
                text = manager.get_info_notes(number)
                clear_console()
                try:
                    print(text[0])
                except TypeError:
                    print('Неправильный выбор. Повторите попытку.')
                    return

                answer = input('\n1. Удалить заметку\n2. Вернуться в меню\n>>>')
                if answer == '1':
                    manager.delete_note(number)
                return
            except ValueError:
                print('Укажите правильное значение.')
    else:
        input('По данному ключевому слову заметок не найдено.\nНажмите любую клавишу для продолжения...')


def find_all_notes():
    '''
    Функция для отображения всех заметок и просмотра содержания определенной заметки.
    '''
    clear_console()
    all_notes = manager.get_all_notes()

    for note_id, note_title in all_notes:
        print(f"{note_id}. {note_title}")

    while True:
        number_notes = input('\nУкажите номер заметки для просмотра содержания, 0 для выхода в меню\n>>>')
        if number_notes == '0':
            return

        try:
            number = int(number_notes)
            text = manager.get_info_notes(number)
            clear_console()
            try:
                print(text[0])
            except TypeError:
                print('Неправильный выбор. Повторите попытку.')
                return

            while True:
                answer = input('\n1. Удалить заметку\n2. Вернуться в меню\n>>>')
                if answer in ['1', '2']:
                    break
                else:
                    print('Укажите правильное значение.')

            if answer == '1':
                manager.delete_note(number)
            return
        except ValueError:
            print('Укажите правильное значение.')


if __name__ == "__main__":
    main()
