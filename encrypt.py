from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

print('input message to be encrypted:')

message = input()
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)
print('encrypted successfully')

file = open('message.msg', 'wb')
file.write(encrypted)
file.close()

var = input()
if var == '':
    quit()



#   / \__
#  (    @\___
#  /         O
# /   (_____/
#/_____/   U