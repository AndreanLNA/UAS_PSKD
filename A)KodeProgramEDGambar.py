# Import library
import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES //import AES

# Generate nilai kunci atau Key
def getKey(keysize):
    key = os.urandom(keysize)
    return key


def getIV(blocksize):
    iv = os.urandom(blocksize)
    return iv

# program enkripsi foto
def encrypt_image(filename, key, iv):
    BLOCKSIZE = 16  # Panjang blok dari key yang digunakan
    encrypted_filename = "Hasil_Enkripsi_" + filename   #menentukan nama file yang telah dienkripsi

    with open(filename, "rb") as file1:
        data = file1.read()
        
        # Penggunaan AES
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))

        with open(encrypted_filename, "wb") as file2:
            file2.write(ciphertext)
    return encrypted_filename

#Program deskripsi foto dari hasil enkripsi di atas
def decrypt_image(filename, key, iv):
    BLOCKSIZE = 16
    decrypted_filename = "Hasil_Deskripsi_" + filename     #menentukan nama file yang telah di deskripsi

    with open(filename, "rb") as file1:
        data = file1.read()

        cipher2 = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher2.decrypt(data), BLOCKSIZE)

        with open(decrypted_filename, "wb") as file2:
            file2.write(decrypted_data)

    return decrypted_filename

 
KEYSIZE = 16  # Key yang digunakan
BLOCKSIZE = 16   # Panjang blok dari key yang digunakan
filename = "Andrean.JPG"        #Memasukkan nama foto yang akan dienkripsi

key = getKey(KEYSIZE)   # Variabel untuk mengambil dari nilai KEYSZISE
iv = getIV(BLOCKSIZE)   # Variabel untuk mengambil dari nilai BLOCKSIZE

encrypted_filename = encrypt_image(filename, key, iv)
decrypted_filename = decrypt_image(encrypted_filename, key, iv)
