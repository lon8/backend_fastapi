DB_CONFIG = { # Вносим сюда свои данные
    "host": "localhost", 
    "user": "root", 
    "password": "132465-Cs",
    "database": "hashes",
    "port": "3306"
}


DB_HASH_URL = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"