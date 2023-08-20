import configparser
import os

config_path = os.path.join(os.path.dirname(__file__), "../config.ini")

# Создайте объект ConfigParser и прочитайте конфигурацию
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8-sig')

# Получите параметры конфигурации
DB_URL = config.get('DBCONF', 'DB_URL')
DB_HASH_URL = config.get('DBSALTCONF', 'DB_URL')

