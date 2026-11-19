import datetime, os

INFO = 'Инфо'
DEBUG = 'Отладка'
ERROR = 'Ошибка'

class singlton:
    _txt_logger = None
    
    def __new__(cls, *args, **kwargs):
        if cls._txt_logger is None:
            cls._txt_logger = super().__new__(cls)
            cls._txt_logger._initialized = False
        return cls._txt_logger


class logger:
    def __init__(self, name_app, path_log, version_app, log_name):
        self.name_app = name_app
        self.path_log = path_log
        self.version_app = version_app
        self.log_name = log_name
        

class console_log(logger):
    def on_message(self, ready_str):
        print(ready_str)

    def write_console(self, level, message):
        str_log = super().text_logger(level,message)
        print(str_log)

class txt_log(singlton, logger):    
    def __init__(self, name_app, path_log, version_app, log_name):
        if self._initialized:
            return
        super().__init__(name_app, path_log, version_app, log_name)
        os.makedirs(self.path_log, exist_ok=True)
        current_time = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S')
        filename = f'{self.name_app}_{current_time}.log'
        full_path = os.path.join(self.path_log, filename)
        self.file = open(full_path, 'a', encoding='utf-8')
        self.file.write(f"Лог создан [{full_path}]:[{self.name_app}]\n")
        self.file.write(f"Версия приложения: {self.version_app}\n")
    
        self._initialized = True
    
    def on_message(self, ready_str):
        self.file.write(f'{ready_str}\n')
        self.file.flush()

        
    def close_file(self):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.file.write(f'Файл логов закрыт в {current_time}')
        self.file.close()
        
class LogBuilder:
    def __init__(self):
        self.log_type = ""
        self.content = ""

    def set_type(self, log_type):
        self.log_type = log_type
        return self

    def set_content(self, msg):
        self.content = msg
        return self

    def build(self):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        return f'[{current_time}] [{self.log_type}]: {self.content}'        


def create_log(log_type, name_app, path_log, version_app, log_name):
    if log_type == "console":
        return console_log(name_app, path_log, version_app, log_name)
    elif log_type == "txt":
        return txt_log(name_app, path_log, version_app, log_name)
    else:
        raise ValueError(f"Неизвестный тип: {log_type}")



handler = create_log("txt", "MyApp", "./logs", "1.0.0", "main_log")

def info(msg):
    output = LogBuilder().set_type("Инфо").set_content(msg).build()
    handler.on_message(output)

def debug(msg):
    output = LogBuilder().set_type("Отладка").set_content(msg).build()
    handler.on_message(output)

def error(msg):
    output = LogBuilder().set_type("Ошибка").set_content(msg).build()
    handler.on_message(output)



info("Работает? Работает!")
debug("Вот такая фигня, собачка")
error("Критическая ошибка! Просроченные ")

handler.close_file()
        
        
        



