# 
# 
# pip install jinja2
# pip install pyyaml
#
# 

from jinja2 import Environment, FileSystemLoader
import subprocess
import yaml  # pip install pyyaml
from datetime import datetime

# Текущая дата и время
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Формат: 2025-11-04 15:30:45


# 1. Загружаем данные из YAML-файла
with open("data.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

# 2. Добавляем текущую дату и время в данные
data["current_datetime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data["date_short"] = datetime.now().strftime("%Y-%m-%d")  # Краткая дата
data["time"] = datetime.now().strftime("%H:%M:%S")        # Время


# 2. Настройка окружения Jinja2
env = Environment(loader=FileSystemLoader('.'))
env.filters['shell'] = lambda cmd: subprocess.check_output(cmd, shell=True, text=True).strip()

# 3. Загружаем и рендерим шаблон
template = env.get_template("template.sh.j2")
rendered_script = template.render(**data)

# 4. Выводим и сохраняем результат
print("Сгенерированный скрипт:")
print(rendered_script)

with open("output.sh", "w", encoding="utf-8") as file:
    file.write(rendered_script)

