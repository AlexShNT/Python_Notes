####
##  с сохранением, чтением, добавлением, редактированием и удалением заметок.
##  содержать идентификатор, заголовок, тело заметки и дату/время создания или
##  последнего изменения заметки
##  формате json или csv формат
####

import json
import os
from datetime import datetime

FILE_NAME = 'notes.json'
ID_NOTE = 'id'
TITLE_NOTE = 'title'
BODY_NOTE = 'body' 
DATE_NOTE = 'date'


def load_notes():   
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Ошибка при чтении файла заметок")
    return []

def save_notes(notes):  
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(notes, file, indent=4)
    except IOError:
        print("Ошибка при сохранении в файл")

# ------------------------------------------------------

def list_notes():
    notes = load_notes()

    print(noteCount)
    for note in notes[1:]:
                print(f"{note[ID_NOTE]}) {note[TITLE_NOTE]} | {note[BODY_NOTE][:10] + '...' if len(note[BODY_NOTE]) > 10 else note[BODY_NOTE]} | (Последнее изменение: {note[DATE_NOTE]})")


def add_note():
    try:
        # title = input("Введите заголовок заметки: ")
        # body = input("Введите текст заметки: ")
        notes = load_notes()

        noteCount = int(notes[0][TITLE_NOTE])

        note = {
            'id': noteCount + 1,
            'title': input("Введите заголовок заметки: "),
            'body': input("Введите текст заметки: "),
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        notes[0][TITLE_NOTE] = str(noteCount + 1)

        notes.append(note)
        save_notes(notes)
        print(f'Заметка успешно добавлена!')
    except Exception as e:
        print(f"Ошибка при добавлении заметки: {e}")




def prn_cmd():
    print ("Список команд:")
    print("  add   - Добавить новую заметку")
    print("  ls    - Показать все заметки или фильтровать по дате")
    print("  edt   - Редактировать заметку")
    print("  rm    - Удалить заметку по ID")
    print("  pr    - Показать заметку по ID")
    print("  f1    - Показать эту справку")
    print("  ex    - Выйти из программы")


def main():
    print ("Программа для создания, просмотра и редактирования заметок (ДЗ)")

    while True:
        prn_cmd()
        try:
            command = input("\nВведите команду: ").strip().lower()
            if command == 'add':
                add_note()
            elif command == 'pr':
                read_note()
            elif command == 'ls':
                list_notes()
            elif command == 'edt':
                edit_note()
            elif command == 'rm':
                remove_note()
            elif command == 'f1':
                prn_cmd()
            elif command == 'ex':
                print("Выход из программы.")
                break
            else:
                print(f"Неизвестная команда: {command}. Введите 'help' для списка команд.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")





if __name__ == "__main__":
    main()