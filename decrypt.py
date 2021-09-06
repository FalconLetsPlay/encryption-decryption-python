from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

file = open('message.msg', 'rb')
message = file.read()
file.close()

f = Fernet(key)
decrypted = decrypted = f.decrypt(message)

original_message = decrypted.decode()
print(original_message)

var = input()
if var == '':
    quit()