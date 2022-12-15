from os import system, name
import os.path

hint = ['Список команд:', 'Новая запись - 1 |',
    'Весь список - 2 |', 'Экспорт в  CSV - 3 |', 'Импорт из CSV - 4']

# очиста консоли
def Сlear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Добавление новой записи в list.txt
def Record(surname, name, first_name, telephone, postal_code, address):
    file = open('list.txt', 'a')
    lines = 0
    for line in open('list.txt'):
        lines += 1    
    file.write(
        str(f"\n{lines};{surname};{name};{first_name};{telephone};{postal_code};{address}"))
    file.close()

# форма добавления новой записи
def NewEntry():
    print(
        '------------------------------------------------------------------------------------------')
    print('Добовление новой записи в справочник:')
    print(
        '------------------------------------------------------------------------------------------')    
    surname = str(input('Фамилия: '))
    name = str(input('Имя: '))
    first_name = str(input('Отчество: '))
    telephone = str(input('Номер телефона (+7): '))
    postal_code = str(input('Почтовый индекс: '))
    address = str(input('Адрес: '))

    check_file = os.path.isfile('list.txt')
    if check_file == True: # проверка, существует ли файл list.txt
        Record(surname, name, first_name, telephone, postal_code, address)
    else:
        file = open('list.txt', 'w')
        file.write(
            str(f"id_line;surname;name;first_name;telephone;postal_code;address"))
        file.close()
        Record(surname, name, first_name, telephone, postal_code, address)

# Вывод справочника на экран
def WholeList():
    print('------------------------------------------------------------------------------------------')
    print('Весь телефонный справочник:')
    print('------------------------------------------------------------------------------------------')
    file = open('list.txt', 'r')
    file_text = ''.join(file)
    file_text = file_text.replace(';', ' ')
    print(file_text)
    file.close()

# Меню пользовательских команд
def Check(team):
    print('------------------------------------------------------------------------------------------')
    print(' '.join(hint))
    print('------------------------------------------------------------------------------------------')
    team = str(input('Введите команду: '))
    team = ''.join(i for i in team if i in '0123456789')
    if team == '0' or team == '1' or team == '2' or team == '3' or team == '4':
        team = int(team)
    else:
        team = 0    
    return team
# Экспорт телефонного справочника в export.csv
def Export():
    file_list = open('list.txt', 'r')
    file_export = open('export.csv', 'w')
    for line in file_list:
        file_export.write(str(line))
    file_list.close()
    file_export.close()
    print('ДАННЫЕ УСПЕШНО ЭКСПОРТИРОВАНЫ В ФАЙЛ EXPORT.CSV!')

 # Импорт в справочник list.txt из import_file.csv
def ImportCSV():
    file_export = open('import_file.csv', 'r')
    file_list = open('list.txt', 'a')
    lines = 0
    for line in file_export:
        if lines == 0:
            file_list.write(str(f"\n{line}"))
        else:
            file_list.write(str(line))
        lines += 1
    file_list.close()
    file_export.close()
    print('ДАННЫЕ УСПЕШНО ИМПОРТИРОВАНЫ В ФАЙЛ LIST.TXT!')