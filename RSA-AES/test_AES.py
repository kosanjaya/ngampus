from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import random
from sympy import isprime, gcd, mod_inverse
import base64
import tkinter
import os
import shutil


class Script:
    def generate_key_RSA(self, value):
        bit_length = value // 2
        p, q = None, None
        while p is None or q is None:
            candidate = random.getrandbits(bit_length)
            if isprime(candidate):
                if p is None:
                    p = candidate
                elif q is None:
                    q = candidate
                    break
        n = p * q
        phi_n = (p - 1) * (q - 1)

        e = random.randint(2, phi_n - 1)  # Memilih bilangan dari 2 hingga rentang totient - 1
        while gcd(e, phi_n) != 1:
            e = random.randint(2, phi_n - 1)
        d = mod_inverse(e, phi_n)

        e_bytes = e.to_bytes((e.bit_length()+7)//8, byteorder='big')
        d_bytes = d.to_bytes((d.bit_length()+7)//8, byteorder='big')
        n_bytes = n.to_bytes((n.bit_length()+7)//8, byteorder='big')

        pembatas = b'\A'
        
        public_key = e_bytes + pembatas + n_bytes
        private_key = d_bytes + pembatas + n_bytes

        encode_e = base64.b64encode(public_key)
        encode_d = base64.b64encode(private_key)

        with open('public-key.bin', 'wb') as f:
            f.write(encode_e)

        with open('private-key.bin', 'wb') as f:
            f.write(encode_d)

        tkinter.messagebox.showinfo(title='Berhasil', message='berhasil generate key')
        return encode_e, encode_d
    
    def generate_key_AES(self, bytes):
        key = get_random_bytes(bytes) # 16byte=128bit, 24,5byte=196bit ,32byte=256bit
        encode_key = base64.b64encode(key)
        return encode_key

    def encrypt_file(self, file, key):
        new_key = base64.b64decode(key)
        cipher_aes = AES.new(new_key, AES.MODE_EAX)
        
        _, ext = os.path.splitext(file)

        if ext == '.txt':
            with open(file, 'rb') as f:
                plaintext = f.read()
            cipher_text, tag = cipher_aes.encrypt_and_digest(plaintext)

            with open(f'enkripFile.txt', 'wb') as encrypt:
                [encrypt.write(x) for x in (cipher_aes.nonce, tag, cipher_text)]
        else:
            with open(file, 'rb') as f:
                plaintext = f.read()
            cipher_text, tag = cipher_aes.encrypt_and_digest(plaintext)

            with open(file + '.enc', 'wb') as encrypt:
                [encrypt.write(x) for x in (cipher_aes.nonce, tag, cipher_text)]

        with open('kunci-AES.bin', 'w') as kunci:
            kunci.write(key)

        tkinter.messagebox.showinfo(title='Berhasil', message='berhasil encrypt pesan')

    def decrypt_file(self, file, key):
        new_key = base64.b64decode(key)
        _, ext = os.path.splitext(file)

        with open(file, 'rb') as decrypt:
                nonce, tag, cipher_text = [decrypt.read(x) for x in (16, 16, -1)] #16 itu dari data nonce dan tag jadi gapapa
        decrypt_aes = AES.new(new_key, AES.MODE_EAX, nonce=nonce)

        if ext == '.txt':    
            try:
                decrypt_message = decrypt_aes.decrypt_and_verify(cipher_text, tag)
                result = decrypt_message.decode()
                with open('hasil-dekrip.txt', 'w') as w:
                    w.write(result)
                if tkinter.messagebox.askyesno(title='Berhasil', message='Baca file tidak kaka??'):
                    os.system('start hasil-dekrip.txt')
                else:
                    pass
            except UnicodeEncodeError as u:
                tkinter.messagebox.showerror(title=u, message='Pesan anda tidak memenuhi standart ASCII!')   

            except ValueError:
                tkinter.messagebox.showerror(title='ValueError', message='Pesan anda tidak Asli!')   
        else:
            decrypt_message = decrypt_aes.decrypt_and_verify(cipher_text, tag)
            decrypt_file = file.replace('.enc', '')

            with open(decrypt_file, 'wb') as w:
                w.write(decrypt_message)

            _, ext = os.path.splitext(decrypt_file)
            new_file_name = 'dekripINI' + ext
            shutil.copy(decrypt_file, new_file_name)
            os.system(f'start {new_file_name}')
            
    def encrypt_RSA(self, message, key_RSA):
        pembatas = b'\A'
        decode_key = base64.b64decode(key_RSA)
        e_decode,n_decode= decode_key.split(pembatas)

        e = int.from_bytes(e_decode, byteorder='big')
        n = int.from_bytes(n_decode, byteorder='big')

        with open(message, 'r') as f:
            baca = f.read()

        decode_key_AES = base64.b64decode(baca)
        convert_to_int = int.from_bytes(decode_key_AES, byteorder='big')
        AES_int = str(convert_to_int)

        result = []

        for i in range(0,len(AES_int),3):
            p = AES_int[i:i+3]
            c = pow(int(p), e, n)
            result.append(c)

        result_str = '\n'.join(map(str, result))

        with open('enkrip-aes-rsa.bin', 'w') as w:
            w.write(result_str)

        if tkinter.messagebox.askyesno(title='Berhasil', message='Baca file tidak kaka??'):
                os.system('start enkrip-aes-rsa.bin')
        else:
            pass

    def decrypt_RSA(self, cipher, key_private):
        pembatas = b'\A'
        decode_key = base64.b64decode(key_private)
        d_decode,n_decode= decode_key.split(pembatas)

        d = int.from_bytes(d_decode, byteorder='big')
        n = int.from_bytes(n_decode, byteorder='big')

        with open(cipher, 'r') as f:
            baca = f.read()
            items = baca.split('\n')
    
        key_int = ''
        for i in items:
            p = int(i)
            dekrip = pow(p, d, n)
            key_int += str(dekrip).zfill(3)

        result = int(key_int)
        key_bytes = result.to_bytes((result.bit_length()+7)//8, byteorder='big')
        encode_key = base64.b64encode(key_bytes)

        with open('hasil-dekrip-aes.bin', 'wb') as f:
            f.write(encode_key)
        if tkinter.messagebox.showinfo(title='Berhasil', message='lihat kunci AES tidak kaka??'):
            os.system('start hasil-dekrip-aes.bin')