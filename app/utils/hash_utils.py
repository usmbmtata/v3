# app/utils/hash_utils.py
import bcrypt

def hash_aadhaar_number(aadhaar_number):
    # Generate a salt and hash the Aadhaar number using bcrypt
    salt = bcrypt.gensalt()
    hashed_aadhaar = bcrypt.hashpw(aadhaar_number.encode(), salt)
    return hashed_aadhaar.decode()  # Convert bytes to string for storage
