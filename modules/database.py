"""
Модуль Manager содержит класс для управления заметками в базе данных.

Автор: cryptocoding
Дата создания: 03.03.2024
"""
import sqlite3


class Manager:
    '''
    Класс для управления заметками в базе данных.
    '''
    def __init__(self):
        db_path = r'db\database.db'
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        if not self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='notes'").fetchone():
            self.create_table()

    def create_table(self):
        '''
        Метод для создания таблицы "notes" в базе данных SQLite.
        '''
        self.cursor.execute('''CREATE TABLE notes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                text TEXT NOT NULL
                            )''')
        self.conn.commit()

    def add_note(self, title, text):
        '''
        Метод для добавления новой заметки в базу данных.
        :param title: Заголовок заметки
        :param text: Содержание заметки
        '''
        self.cursor.execute('INSERT INTO notes (title, text) VALUES (?, ?)', (title, text))
        self.conn.commit()
        return 'Заметка успешно добавлена!'

    def get_all_notes(self):
        '''
        Метод для добавления новой заметки в базу данных.

        Параметры:
        title (str): Заголовок заметки.
        text (str): Содержание заметки.
        '''
        self.cursor.execute("SELECT id, title FROM notes")
        return self.cursor.fetchall()

    def get_info_notes(self, note_id):
        '''
        Метод для получения содержания заметки по её ID.
        Возвращает текст заметки или None, если заметка не найдена.
        '''
        self.cursor.execute("SELECT text FROM notes WHERE id = ?", (note_id,))
        return self.cursor.fetchone()

    def delete_note(self, note_id):
        '''
        Метод для удаления заметки по её ID из базы данных.
        '''
        self.cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
        self.conn.commit()

    def search_notes(self, keyword):
        '''
        Метод для поиска заметки по её ID.
        '''
        self.cursor.execute("SELECT id, title FROM notes WHERE text LIKE ?", ('%'+keyword+'%',))
        return self.cursor.fetchall()
