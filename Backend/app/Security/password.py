from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

# Initialize password hasher with Argon2
password_hash = PasswordHash((Argon2Hasher(),))


def hash_password(password: str) -> str:
    """Hash a plain-text password using Argon2."""
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain-text password against a hashed password."""
    return password_hash.verify(plain_password, hashed_password)
