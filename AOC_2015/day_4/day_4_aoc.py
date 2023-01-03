import hashlib

start_key = "yzbqklnj"

hash = hashlib.md5(start_key.encode())

print(hash.hexdigest())

adder = 0

while not hash.hexdigest().startswith("000000"):
    
    mod_key = start_key + str(adder)
    hash = hashlib.md5(mod_key.encode())
    adder += 1

print(hash.hexdigest())
print(mod_key)
    