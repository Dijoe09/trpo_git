import datetime, os

INFO = 'Инфо'
DEBUG = 'Отладка'
ERROR = 'Ошибка'


class logger:
    def __init__(self, name_app, path_log, version_app, log_name):
        self.name_app = name_app
        self.path_log = path_log
        self.version_app = version_app
        self.log_name = log_name
        
    def text_logger(self,level, message,):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        return f'[{current_time}] [{level}]: {message}'
    
class console_log(logger):
    def write_console(self, level, message):
        str_log = super().text_logger(level,message)
        print(str_log)

class txt_log(logger):
    def __init__(self, name_app, path_log, version_app, log_name):
        super().__init__(name_app, path_log, version_app, log_name)
        os.makedirs(self.path_log, exist_ok=True)
        current_time = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S')
        filename = f'{self.name_app}_{current_time}.log'
        full_path = os.path.join(self.path_log, filename)
        self.file = open(full_path, 'a', encoding='utf-8')
        self.file.write(f"Лог создан [{full_path}]:[{self.name_app}]\n")
        self.file.write(f"Версия приложения: {self.version_app}\n")
    
    def write_txt(self, level, message):
        str_log = super().text_logger(level,message)
        self.file.write(f'{str_log}\n')
        
    def close_file(self):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.file.write(f'Файл логов закрыт в {current_time}')
        self.file.close()
        

        
        
        



