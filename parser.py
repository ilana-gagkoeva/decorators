class Parser:
    """ Парсер веб-сайта """
    DOMAIN = 'website'
    REMOVE_PARTS = ['www', 'ru']
    REPLACE_PARTS = {'.': '_'}

    @classmethod
    def get_filename(cls, url: str) -> str:
        """Получени имени файла, куда должны сохраняться спаршенные данные"""

        parts = url.split('/')
        for p in cls.REMOVE_PARTS:
            if p in parts:
                parts.remove(p)

        parts.append(cls.DOMAIN) # обращение к свойству класса


        filename = '_'.join(parts)
        for kp, vp in cls.REPLACE_PARTS.items(): # обращение к свойству класса
            filename = filename.replace(kp, vp)

        return filename
url = 'www.sportmaster.ru/catalog/muzhskaya_odezhda/kurtki/'
filename = Parser.get_filename(url)
print(filename)