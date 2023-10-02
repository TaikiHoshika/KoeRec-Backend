import bcrypt

password = b"p@ssw0rd"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print(hashed.decode())