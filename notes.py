####
##  с сохранением, чтением, добавлением, редактированием и удалением заметок.
##  содержать идентификатор, заголовок, тело заметки и дату/время создания или
##  последнего изменения заметки
##  формате json или csv формат
####

def prn_cmd():
    print ("Список команд:")
    print("  add   - Добавить новую заметку")
    print("  ls    - Показать все заметки или фильтровать по дате")
    print("  edt   - Редактировать заметку")
    print("  rm   - Удалить заметку по ID")
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