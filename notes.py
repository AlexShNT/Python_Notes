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
    try:
        date_filter = input("Введите дату (YYYY-MM-DD) для фильтрации или оставьте пустым для вывода всех: ").strip()
        notes = load_notes()
        
        if date_filter:
            try:
                filter_date = datetime.strptime(date_filter, '%Y-%m-%d').date()
                notes = [note for note in notes if datetime.strptime(note[DATE_NOTE], '%Y-%m-%d %H:%M:%S').date() == filter_date]
            except ValueError:
                print("Неверный формат даты. Показаны все заметки.")
        
        if notes:
            print("ID|   Заголовок   | Текст заметки | Время последнего изменения ")
            print("--------------------------------------------------------------------------------")
            for note in notes:
                if note[ID_NOTE] == 0: continue
                print(f"{note[ID_NOTE]}). {note[TITLE_NOTE][:10] + '...' if len(note[TITLE_NOTE]) > 10 else (note[TITLE_NOTE] + ' ' * (13 - len(note[TITLE_NOTE])))} | " +
                      f"{note[BODY_NOTE][:10] + '...' if len(note[BODY_NOTE]) > 10 else note[BODY_NOTE] + ' ' * (13 - len(note[BODY_NOTE]))} | (Последнее изменение: {note[DATE_NOTE]}) |")
        else:
            print('Нет доступных заметок.')
    except Exception as e:
        print(f"Ошибка при выводе списка заметок: {e}")


def add_note():
    try:
        notes = load_notes()

        noteCount = int(notes[0][TITLE_NOTE])

        note = {
            ID_NOTE: noteCount + 1,
            TITLE_NOTE: input("Введите заголовок заметки: "),
            BODY_NOTE: input("Введите текст заметки: "),
            DATE_NOTE: datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        notes[0][TITLE_NOTE] = str(noteCount + 1)

        notes.append(note)
        save_notes(notes)
        print(f'Заметка успешно добавлена!')
    except Exception as e:
        print(f"Ошибка при добавлении заметки: {e}")

def read_note():
    try:
        note_id = int(input("Введите ID заметки для чтения: "))
        notes = load_notes()
        for note in notes:
            if note[ID_NOTE] == note_id:
                print(f"ID: {note[ID_NOTE]}")
                print(f"Заголовок: {note[TITLE_NOTE]}")
                print(f"Тело: {note[BODY_NOTE]}")
                print(f"Последнее изменение: {note[DATE_NOTE]}")
                return
        print(f'Заметка с ID {note_id} не найдена.')
    except ValueError:
        print("Ошибка: ID заметки должно быть числом.")
    except Exception as e:
        print(f"Ошибка при чтении заметки: {e}")

def remove_note():
    try:
        note_id = int(input("Введите ID заметки для удаления: "))
        if note_id <= 0: return
        notes = load_notes()
        notes = [note for note in notes if note[ID_NOTE] != note_id]
        save_notes(notes)
        print(f'Заметка с ID {note_id} успешно удалена!')
    except ValueError:
        print("Ошибка: ID заметки должно быть числом.")
    except Exception as e:
        print(f"Ошибка при удалении заметки: {e}")   

def edit_note():
    try:
        note_id = int(input("Введите ID заметки для редактирования: "))
        notes = load_notes()
        for note in notes:
            if note[ID_NOTE] == note_id:                 
                note[TITLE_NOTE] = input(f"Введите новый заголовок заметки (текущий: {note[TITLE_NOTE]}): ") or note[TITLE_NOTE]
                note[BODY_NOTE] = input(f"Введите новое тело заметки (текущее: {note[BODY_NOTE]}): ") or note[BODY_NOTE]
                note[DATE_NOTE] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                save_notes(notes)
                print(f'Заметка с ID {note_id} успешно обновлена!')
                return
        print(f'Заметка с ID {note_id} не найдена.')
    except ValueError:
        print("Ошибка: ID заметки должно быть числом.")
    except Exception as e:
        print(f"Ошибка при редактировании заметки: {e}")   


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
    print(' ')
    prn_cmd()

    while True:

        try:
            command = input("\nВведите команду (f1: список команд): ").strip().lower()
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