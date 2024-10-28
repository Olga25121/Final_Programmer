from datetime import datetime
import csv

class Menu():
    animal_class_types={'лошадь':'Horses', 'осел':'Donkeys', 'верблюд': 'Camels', 'кот': 'Cats', 'собака': 'Dogs', 'хомяк': 'Hamsters'}
    animal_class_types_declension={'лошадь':'лошади', 'осел': 'осла', 'верблюд': 'верблюда', 'кот': 'кота', 'собака': 'собаки', 'хомяк': 'хомяка'}
    @staticmethod
    def for_one_menu():
        while True:
            name=input("Введите имя животного => ").strip()
            if name.isalpha():
                break
            print("Неверный формат имени")
        
        animal_type=Menu.choose_animal_type()

        while True:
            try:
                data = input('Введите дату рождения в формате ДД.ММ.ГГГГ =>')
                birth_date= datetime.strptime(data,'%d.%m.%Y')
                break
            except ValueError:
                print('Введенная дата не является корректной, попробуйте еще раз')
        input_command= input("Перечислите команды, которые животные могут выполнять (через запятую),\nили пропустите ввод, чтобы оставить поле пустым => ")
        if input_command.strip()=='':
            commands = None
        else: commands=[i.strip() for i in input_command.split(',')]
        return name, animal_type, birth_date, commands
    @staticmethod
    def choose_animal_type():
        animal_type=None
        while True:
            match int(input(f"""
        Выберите тип животного:
        1.лошадь
        2.осел
        3.верблюд
        4.кот
        5.собака
        6.хомяк
        {'*'*40}
        введите номер => """)):
                case 1:
                    animal_type='лошадь'
                    break
                case 2:
                    animal_type='осел'
                    break
                case 3:
                    animal_type='верблюд'
                    break
                case 4:
                    animal_type='кот'
                    break
                case 5:
                    animal_type='собака'
                    break
                case 6:
                    animal_type='хомяк'
                    break
                case _:
                    print("Выберите из предложенных вариантов")
        return animal_type
    @staticmethod
    def menu():
        print(f"\nВы работаете с реестром домашних животных.\nВыберите пункт меню:\n{'*'*40}", end='')
        print('''
    1.Добавить в реестр новое животное\n
    2.Показать реестр\n
    3.Обучить животное новой команде\n
    4.Удалить животное из реестра\n
    5.Сохранить реестр в файл\n
    6.Выйти из реестра'''+'\n'+'*'*40+'\n')
        
        while True:
            input_command=input("Пункт меню => ")
            if input_command.strip().isdigit() and 1<=int(input_command)<=6:
                return int(input_command)
    @staticmethod
    def to_teach_animal_to_commands(register):
        name=input("Введите имя животного => ")
        animal_type=Menu.choose_animal_type()
        commands = [i.strip() for i in input("Введите команду или список команд через запятую => ").strip().split(',')]
        if not commands:
            print('Поле с командами не может быть пустым')
            return
        count=0
        for animal in register.get_reestr_list():
            if animal.__class__.__name__ == Menu.animal_class_types[animal_type]:
                count+=1
                if animal.get_name().lower() == name.strip().lower():
                        for command in commands:
                            animal.set_commands(command)
                        print("\nКоманды добавлены\n")
                        return 
        print(f'\n{Menu.animal_class_types_declension[animal_type].capitalize()} с таким имененм не найдено.\nСначала добавьте животное или проверьте имя\n')
    @staticmethod
    def del_animal_from_register():
        name=input("Введите имя животного => ")
        animal_type=Menu.choose_animal_type()
        return name, animal_type
    @staticmethod
    def print_register_to_file(animal_register):
        with open("My animal's register.csv", 'w', encoding='utf-8') as file:
            columns=['Тип', 'Подтип','Имя животного', 'Дата рождения', 'Команды, которые умеет выполнять животное']
            writer = csv.writer(file)
            writer.writerow(columns)                 # запись заголовков
            for animal in animal_register:                         # запись строк
                 writer.writerow(animal.get_animal_list())
        print("Данные записаны в файл My animal's register.csv")