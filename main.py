# Укажите полный путь до папки, где нужно сохранить файл requirements.txt
# Пример для Windows: save_path = r"C:\Users\Username\Project"
# Пример для Linux/Mac: save_path = "/home/username/project"
save_path = ""  # Оставьте пустым, чтобы сохранить в текущем каталоге

# Имя файла
file_name = "requirements.txt"
# ----------------------------

# Полный путь до файла
import os
full_path = os.path.join(save_path, file_name) if save_path else file_name

# Сбор импортированных библиотек
import sys
import importlib
imported_libs = {}

# Получаем список имён глобальных переменных перед началом итерации
global_names = list(globals().keys())

for name in global_names:
    val = globals().get(name)
    if isinstance(val, type(sys)):  # Проверяем, является ли значение модулем
        lib_name = val.__name__.split('.')[0]
        if lib_name not in imported_libs:
            try:
                version = importlib.import_module(lib_name).__version__
                imported_libs[lib_name] = version
            except (ImportError, AttributeError):
                continue

# Запись в файл
print(file_name, "Библиотеки:\n")
with open(full_path, "w") as file:
    for lib, version in imported_libs.items():
        print(f"{lib}=={version}")
        file.write(f"{lib}=={version}\n")
print()

# Вывод пути, по которому был создан файл
print(f"Файл requirements.txt создан по пути: {os.path.abspath(full_path)}")
