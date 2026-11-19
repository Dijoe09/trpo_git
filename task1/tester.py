# Импортируем твои классы и константы уровней из файла logger.py
from progat.trpo.task1.logger import console_log, txt_log, INFO, DEBUG, ERROR

def main():
    print("--- ЗАПУСК ТЕСТИРОВАНИЯ БИБЛИОТЕКИ ЛОГИРОВАНИЯ ---")
    
    # 1. Инициализируем консольный логгер
    # Он примет параметры приложения, но путь к файлу использовать не будет
    c_logger = console_log(
        name_app="tester", 
        path_log="Logs", 
        version_app="1.0.0", 
        log_name="console_version"
    )
    
    # 2. Инициализируем файловый логгер
    # В этот момент на диске должна создаться папка Logs и файл с шапкой
    f_logger = txt_log(
        name_app="tester", 
        path_log="Logs", 
        version_app="1.0.0", 
        log_name="file_version"
    )
    
    # 3. Тестируем вывод в консоль
    c_logger.write_console(INFO, "Приложение успешно запущено.")
    c_logger.write_console(DEBUG, "Проверка отладочного режима в консоли.")
    
    # 4. Тестируем вывод в файл
    f_logger.write_txt(INFO, "Начата попытка подключения к базе данных.")
    f_logger.write_txt(ERROR, "Не удалось подключиться к БД: Тайм-аут соединения.")
    
    # 5. Закрываем файл (запишется финальная строчка о закрытии)
    f_logger.close_file()
    
    print("\n--- ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ---")
    print("Проверь консоль выше и загляни в созданную папку 'Logs'!")

if __name__ == "__main__":
    main()
