import configparser
import os

config_path = os.path.join(os.path.dirname(__file__), "../config.ini")

# Создайте объект ConfigParser и прочитайте конфигурацию
config = configparser.ConfigParser()
config.read(config_path)

# Получите параметры конфигурации
DB_URL = config.get('DBCONF', 'DB_URL')

print(DB_URL)