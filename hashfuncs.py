import hashlib
import secrets

def generate_salt(length=16):
    return secrets.token_hex(length // 2)

def hash_with_salt(data, salt):
    data_with_salt = f"{salt}{data}"
    hashed_data = hashlib.sha256(data_with_salt.encode()).hexdigest()
    return hashed_data

def hash_data(data):
    salt = generate_salt()
    hashed_data = hash_with_salt(data, salt)
    return salt, hashed_data

def verify_hash(data, salt, hashed_data):
    return hash_with_salt(data, salt) == hashed_data

# Пример использования
original_data = "mydata"
salt, hashed_data = hash_data(original_data)
print("Salt:", salt)
print("Hashed Data:", hashed_data)

is_verified = verify_hash(original_data, salt, hashed_data)
print("Verification:", is_verified)