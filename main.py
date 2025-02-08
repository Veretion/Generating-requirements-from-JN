# Вставляем весь этот код в ячейку JN и запускаем, работает из коробки в каталог из которого открыт файл

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
for name, val in globals().items():
    if isinstance(val, type(sys)):
        lib_name = val.__name__.split('.')[0]
        if lib_name not in imported_libs:
            try:
                version = importlib.import_module(lib_name).__version__
                imported_libs[lib_name] = version
            except (ImportError, AttributeError):
                continue

# Запись в файл
with open(full_path, "w") as file:
    for lib, version in imported_libs.items():
        file.write(f"{lib}=={version}\n")

# Вывод пути, по которому был создан файл
print(f"Файл requirements.txt создан по пути: {os.path.abspath(full_path)}")
