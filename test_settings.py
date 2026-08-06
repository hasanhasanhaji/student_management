from app.security.hashing import (
    hash_password,
    verify_password,
)

password = "123456"

hashed = hash_password(password)

print("Hash:")
print(hashed)

print()

print(
    verify_password(
        "123456",
        hashed,
    )
)