from Pets import *
from PackPets import *
from Menu import *
from datetime import datetime
from AnimalRegister import *

animals_registry=AnimalRegister()
animals_registry.add(('Борька','осел',datetime(2019,12,1), ['упираться', 'везти']))
animals_registry.add(('Васька','кот',datetime(2018,11,15), ['мурлыкать', 'спать']))
animals_registry.add(('Сёмка','верблюд',datetime(2022,4,8), ['не пить', 'везти']))
#animals_registry.add(('Жучка','собака',datetime(2016,10,1), ['гавкать', 'плавать']))
animals_registry.add(('Жучка','собака',datetime(2016,10,1), ['гавкать', 'плавать']))
animals_registry.add(('Шторм','лошадь',datetime(2019,8,18), ['бегать галопом', 'брыкаться']))
animals_registry.add(('Понька','хомяк',datetime(2023,12,1), ['крутить колесо', 'прятать запасы']))
animals_registry.add(('Сонька','осел',datetime(2024,2,1), ['йакать', 'медленно идти']))
animals_registry.add(('Джек','верблюд',datetime(2017,12,1), ['садиться', 'долго идти']))
while True:
    match Menu.menu():
        case 1:
            animals_registry.add(Menu.for_one_menu())        
            print("\nЖивотное добавлено в реестр\n")            
        case 2: #2. Показать реестр
            print(f"В регистре находятся:\n{'*'*40}")
            if len(animals_registry) == 0:
                print("В реестре еще нет животных. Добавьте животных в реестр")
            else: print(*animals_registry, sep='\n')
            print('*'*40)
        case 3: #3. Обучить животное
            Menu.to_teach_animal_to_commands(animals_registry)            
        case 4: #4. Удалить животное из регистра
            del animals_registry[Menu.del_animal_from_register()]
        case 5: #5.Сохранить реестр в файл 
            Menu.print_register_to_file(animals_registry)
        case 6: #6. Выход из программы
            print("До свидания! Хорошего дня!")
            break
        case _: #В случае ввода неверного значения
            print ("Для продолжения, введите пункт меню от 1 до 6")
            