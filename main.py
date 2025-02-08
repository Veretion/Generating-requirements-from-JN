# Вставляем весь этот код в ячейку JN и запускам
import sys
import importlib

# Функция для получения списка всех импортированных библиотек
def get_imported_libraries():
    imported_libs = {}
    for name, val in globals().items():
        if isinstance(val, type(sys)):  # Проверяем, является ли объект модулем
            lib_name = val.__name__.split('.')[0]  # Получаем имя библиотеки
            if lib_name not in imported_libs:
                try:
                    # Получаем версию библиотеки
                    version = importlib.import_module(lib_name).__version__
                    imported_libs[lib_name] = version
                except (ImportError, AttributeError):
                    # Если версию получить не удалось, пропускаем
                    continue
    return imported_libs

# Получаем список импортированных библиотек
imported_libs = get_imported_libraries()

# Записываем их в файл requirements.txt
with open("requirements.txt", "w") as file:
    for lib, version in imported_libs.items():
        file.write(f"{lib}=={version}\n")

# Выводим содержимое файла для проверки
with open("requirements.txt", "r") as file:
    print(file.read())
