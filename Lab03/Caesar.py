class Caesar:
    def __init__(self, key=0):
        self.__key = key
    def get_key(self):
        return self.__key
    def set_key(self, key):
        self.__key = key
    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext.lower():
            if char.isalpha():
                shifted = chr((ord(char) - 97 + self.__key) % 26 + 97)
                ciphertext += shifted
            else:
                ciphertext += chr((ord(char) + self.__key) % 128)
        return ciphertext
    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext.lower():
            if char.isalpha():
                shifted = chr((ord(char) - 97 - self.__key) % 26 + 97)
                plaintext += shifted
            else:
                plaintext += chr((ord(char) - self.__key) % 128)
        return plaintext
cipher = Caesar(3)
print(cipher.encrypt("hello WORLD"))
print(cipher.decrypt("khoor zruog!"))
cipher.set_key(6)
print(cipher.encrypt("zzz"))
print(cipher.decrypt("fff"))
cipher.set_key(-6)
print(cipher.encrypt("fff"))