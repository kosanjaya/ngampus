import numpy as np
import string

abjad_obj = string.ascii_uppercase + ' '

def check_key(cekKey):
    det = (cekKey[0] * cekKey[3] - cekKey[1] * cekKey[2])
    if det == 0:
        print('Hasil determinan key tidak boleh 0')
        return False
    else:
        for i in range(1, 27):
            if (det * i % 27) == 1:
                print('Key Anda bisa digunakan...')
                return True
        else:
            print('Tidak ada hasil yang di modulus 26 yang menghasilkan invers.')
            return False


def encrypt_decrypt_hill(plaintext, key, key_r=None):
    text = []
    
    key_array = np.array(key)
    matriks = np.reshape(key_array, (2,2)) # 2 x 2 matriks nya
    
    for j in plaintext.upper(): # convert text to interger
        new = abjad_obj.find(j) 
        text.append(new)
        
    if len(text) % len(matriks) != 0: # Menambah nilai ke list plaintext
        minus_list = len(matriks) - len(text) % len(matriks)
        for i in range(minus_list):
            p = abjad_obj.find('Z')
            text.append(p)
    
    text_array = np.array(text)
    text_matrix = np.reshape(text_array,(-1,2))
    hasil_int = []
    for a in range(len(text_matrix)):
        for b in range(len(matriks)):
            new_text = 0
            for c in range(len(matriks[0])):
                new_text += (text_matrix[a][c] * matriks[c][b]) # Tambahkan hasil perkalian ke hasil sebelumnya
            new_text %= 27
            hasil_int.append(new_text)     
    hasil_str = ''
    for z in hasil_int:
        h = abjad_obj[z]
        hasil_str = hasil_str + h

    while hasil_str.endswith('Z'):
        hasil_str = hasil_str[:-1]
    print('Hasil enkripsi cypher hill: ', hasil_str)
    
    if key_r is not None:
        new_key_r = int(key_r)
        encrypt(hasil_str, new_key_r)

def invers_matrix(cipher, key):
    det = (key[0]*key[3]) - (key[1]*key[2])
    new_key = () # buat tuple cukk nampung data 
    for i in range(1000):
        if (det * i % 27) == 1:
            k1 = (key[3] * i)%27
            k2 = (-key[1] * i)%27
            k3 = (-key[2] * i)%27
            k4 = (key[0] * i)%27
            k5 = k1,k2,k3,k4
            new_key += k5 
            break
    encrypt_decrypt_hill(cipher, new_key)

def encrypt(text, key):
    rail = [['\n' for i in range(len(text))]
                for j in range(key)]
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    
    print('hasil super enkripsi:',"" . join(result))


def decrypt(cipher, key, key_h):
    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
    
    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1    
        if dir_down:
            row += 1
        else:
            row -= 1
    
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    row, col = 0, 0
    result = []
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    dekrip1 = "".join(result)
    # print('ini decrypt rail',dekrip1)
    invers_matrix(dekrip1, key_h)

while True:
    cek = input('Masukan key yang ingin di coba (format = 1,2,3,4): ')
    key = tuple(map(int, cek.split(',')))
    if check_key(key):
        break

while True:
    pilih = int(input('\n1.(enkrip)\n2.(dekrip)\n: '))
    if pilih == 1:
        plain = input('Masukan text : ').upper()
        if all(char in abjad_obj for char in plain):
            input_key_hill = input('Masukkan Key (format = 1,2,3,4) : ')
            input_key_r = input('masukkan key transposisi rail fence: ')
            key = tuple(map(int, input_key_hill.split(','))) #convert to tuple
            encrypt_decrypt_hill(plain, key, input_key_r)
        else:
            print('Hanya alphabet dulu ya...')
            break
            
    elif pilih == 2:
        text = input('Masukan text : ').upper()
        if all(char in abjad_obj for char in text):
            input_key_h = input('Masukkan Key (format = 1,2,3,4) : ')
            input_key_r = int(input('masukkan key transposisi rail fence: '))
            key = tuple(map(int, input_key_h.split(','))) #convert to tuple
            decrypt(text, input_key_r, key)
        else:
            print('Alphabet dulu ya...')
            break
        
    else :
        print("Input Invalid!!!\n")
        
