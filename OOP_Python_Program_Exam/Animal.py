from abc import ABC
from datetime import  datetime

class Animal(ABC):
    
    def __init__(self,name, type_animal, birth_date, commands=None):
        
        self._name = name
        self._type = type_animal
        self._birth_date = birth_date
        self._commands=None
        if not commands:
            self._commands=[]
        else: self._commands=list(commands)
        
        
    def __str__(self):
        year_age=(datetime.now()-self._birth_date).days//365
        #дописать возраст в днях, если разница меньше месяца
        return f"Тип: {type(self).mro()[1].__name__}; Подтип: {self._type}; кличка: {self._name}; возраст: {year_age} лет(года); знает команды: {',  '.join(self._commands)}"
    def get_name(self):
        return self._name
    def get_type(self):
        return self._type
    def get_commands(self):
        return self._commands
    def set_commands(self,value):
        if value not in self._commands:
            self._commands.append(value) 
    def get_animal_list(self):
        return [type(self).mro()[1].__name__,self._type, self._name, self._birth_date, self._commands]