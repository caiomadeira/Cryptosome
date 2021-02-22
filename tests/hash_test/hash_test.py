import hashlib

file = open("test.txt", "rb")
data = file.read()
data_2 = hashlib.md5(data).hexdigest()
print(data_2[1:33])
print(len(data_2))

