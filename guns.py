from abc import ABC, abstractmethod


class Gun(ABC):
    """Абстрактное оружие, которое умеет стрелять"""
    
    @property
    @abstractmethod
    def title(self):
        pass
    
    @abstractmethod
    def shoot(self):
        class_name = self.title
        print('Shoot from {}'.format(class_name))