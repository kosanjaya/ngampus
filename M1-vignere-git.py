def encrypt(plaintext, key):
    encrypted_text = ""
    key_index = 0
    
    for char in plaintext: #panjang plaintext
       
        shift = ord(key[key_index % len(key)]) - ord(' ') #loop key dan mengubah ke INT ord modulus panjang key
        shifted_char = chr((ord(char) - ord(' ') + shift) % 95 + ord(' '))
        encrypted_text += shifted_char
        key_index += 1
    
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    key_index = 0
    
    for char in ciphertext:
        shift = ord(key[key_index % len(key)]) - ord(' ')
        shifted_char = chr((ord(char) - ord(' ') - shift) % 95 + ord(' '))
        decrypted_text += shifted_char
        key_index += 1
    return decrypted_text

plaintext = input('masukan text: ')
key = input('masukan key: ')

encrypted_text = encrypt(plaintext, key)
print("Teks Terbuka:", plaintext)
print("Teks Sandi:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Teks Terbaca:", decrypted_text)