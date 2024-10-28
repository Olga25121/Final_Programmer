from PackPets import *;
from Pets import *

class AnimalRegister():
    
    def __init__(self):
        self._reestr_list=[]    
    def add(self, data):
        for animal in self._reestr_list:
            if animal.get_name() == data[0] and animal.get_type()==data[1]:
                print(f'\n{data[1].capitalize()} с таким именем уже существует\n')
                return
    
        match data[1]:
            case "верблюд":
                self._reestr_list.append(Camels(data[0],data[1],data[2],data[3]))                    
            case 'кот':
                self._reestr_list.append(Cats(data[0],data[1],data[2],data[3]))                    
            case "лошадь":
                self._reestr_list.append(Horses(data[0],data[1],data[2],data[3]))                    
            case "хомяк":
                self._reestr_list.append(Hamsters(data[0],data[1],data[2],data[3]))                    
            case "собака":
                self._reestr_list.append(Dogs(data[0],data[1],data[2],data[3]))
            case "осел":
                self._reestr_list.append(Donkeys(data[0],data[1],data[2],data[3])) 
    def __iter__ (self):
        yield from self._reestr_list
    def __len__(self):
        return len(self._reestr_list)
    def get_reestr_list(self):
        return self._reestr_list
    def __delitem__(self, data):
        for i,animal in enumerate(self._reestr_list):
            if animal.get_name().lower() == data[0].lower() and animal.get_type()==data[1]:
                del self._reestr_list[i]
                print('Животное удалено из реестра')
                return
        print('Такого животного нет в реестре')
    

    
        
            
        