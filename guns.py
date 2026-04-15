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

class Pistol(Gun):
    """Пистолет"""
    
    @property
    def title(self):
        return 'Pistol'
        
    def shoot(self):
        super().shoot()

class Automat(Gun):
    """Автомат"""

    @property
    def title(self):
        return 'Automat'


    def shoot(self):
        super().shoot()


class MachineGun(Gun):
    """Пулемёт"""

    @property
    def title(self):
        return 'MachineGun'

    def shoot(self):
        super().shoot()

class SilencerDecorator(Gun):
    """Декоратор глушителя"""

class LightingDecorator(Gun):
    """Декоратор для фонарика"""

class AllGunSilencerDecorator(SilencerDecorator):
    @property
    def title(self):
        return self._gun.title
        
    def __init__(self, gun: Gun):
        self._gun = gun   
        
    def shoot(self):
        print('Надеваем глушитель...')
        self._gun.shoot()
        print('Снимаем глушитель...')
        
class PistolSilencerDecorator(SilencerDecorator):
    @property
    def title(self):
        return self._pistol.title
        
    def __init__(self, pistol: Pistol):
        self._pistol = pistol
        
    def shoot(self):
        print('Надеваем специальный глушитель для пистолетов...')
        self._pistol.shoot()
        print('Снимаем специальный глушитель для пистолетов...')

# создание пистолета, автомата, пулемёта
p = Pistol()
a = Automat()
mg = MachineGun()

# создание пистолета с глушителем
sp = AllGunSilencerDecorator(p)
# создание автомата с глушителем
sa = AllGunSilencerDecorator(a)
# создание пулемёта с глушителем
smg = AllGunSilencerDecorator(mg)

# создание пистолета со специальным глушителем для пистолетов
ssp = PistolSilencerDecorator(p)

# стрельба из оружия
for gun in [p, a, mg, sp, sa, smg, ssp]:
    gun.shoot()
    