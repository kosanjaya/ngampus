import customtkinter as ctk
import tkinter as tk
from test_AES import Script


class MyApp(ctk.CTk):
    def  __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.backend = Script()
        self.bit = None
        self.bytes = None
        self.configure(fg_color='#484848')

        panjang_layar = self.winfo_screenwidth()
        lebar_layar = self.winfo_screenheight()
        x = (panjang_layar/2) - (size[0]/2)
        y = (lebar_layar/2) - (size[1]/2)
        self.geometry(f'{size[0]}x{size[1]}+{int(x)}+{int(y)}')
        self.wm_resizable(True,False)
        self.create_widgets()

    def create_widgets(self):
        frame1 = ctk.CTkFrame(self, width=545, height=395,fg_color='#D7D7D7')
        frame1.place(x=630,y=80)

        frame2 = ctk.CTkFrame(self,width=545, height=44,fg_color='#D7D7D7')
        frame2.place(x=28,y=20)

        frame3= ctk.CTkFrame(frame1,width=520, height=75,fg_color='#A4A4A4')
        frame3.place(x=13,y=50)

        frame4 = ctk.CTkFrame(self,width=559, height=395,fg_color='#D7D7D7')
        frame4.place(x=30,y=80)

        self.button1 = ctk.CTkButton(frame2,
                         width=105,
                         height=26, 
                         text='Pilih File',
                         font=('Open sans', 12, 'normal'),
                         fg_color='#5C9EDB', 
                         command= self.open_file)
        self.button1.place(x=420,y=8) 
    
        self.button2 = ctk.CTkButton(frame1,width=124, height=41,
                                                text="Encrypt",
                                                font=('Open sans', 19, 'normal'),
                                                fg_color='#D61C1C',
                                                border_color="white",                                      
                                                command=self.callback_encrypt_RSA)
        self.button2.place(x=145,y=345)
        

        self.button3 = ctk.CTkButton(frame1,width=124, height=41,
                                                text="Decrypt",
                                                font=('Open sans', 19, 'normal'),
                                                fg_color='#D61C1C',
                                                border_color="white",
                                                 command=self.callback_decrypt_RSA)
        self.button3.place(x=285,y=345)

        self.button4 = ctk.CTkButton(frame1,width=129,height=32,
                                                    text="Generate Key",
                                                    font=('Open sans',14, 'normal'),
                                                    fg_color='#DB5C5C',
                                                    border_color="white",
                                                    command=self.callback_key_RSA)
        self.button4.place(x=210,y=165)

        self.button5 = ctk.CTkButton(frame3,
                         width=105,
                         height=31.91, 
                         text='Choosen File',
                         font=('Open sans', 12, 'normal'),
                         fg_color='#DB5C5C', 
                         command= self.open_file2)
        self.button5.place(x=390,y=35) 

        self.button6 = ctk.CTkButton(frame4,width=124, height=41,
                                                text="Encrypt",
                                                font=('Open sans', 19, 'normal'),
                                                fg_color='#D61C1C',
                                                border_color="white",
                                                 command=self.callback_encrypt)
        self.button6.place(x=145,y=323)

        self.button7 = ctk.CTkButton(frame4,width=124, height=41,
                                                text="Decrypt",
                                                font=('Open sans', 19, 'normal'),
                                                fg_color='#D61C1C',
                                                border_color="white",
                                                command=self.callback_decrypt)
        self.button7.place(x=285,y=323)

        self.button8 = ctk.CTkButton(frame4,width=129,height=32,
                                                    text="Generate Key",
                                                    font=('Open sans',14, 'normal'),
                                                    fg_color='#DB5C5C',
                                                    border_color="white",
                                                    command= self.callback_key_AES)
        self.button8.place(x=215,y=120)


        label1 = ctk.CTkLabel(frame2,
                                text="Url Plain Text:",
                                font=('Open sans',15,'normal'),
                                text_color=('black','black'),
                                fg_color=('#D7D7D7'))
        label1.place(x=25,y=7)

        label2= ctk.CTkLabel(frame1,
                                text="Public Key",
                                font=('Open sans',16,'bold'),
                                text_color=('black','black'),
                                fg_color=('#D7D7D7'))
        label2.place(x=100,y=190)

        label2= ctk.CTkLabel(frame1,
                                text="Private Key",
                                font=('Open sans',16,'bold'),
                                text_color=('black','black'),
                                fg_color=('#D7D7D7'))
        label2.place(x=365,y=190)

        label3= ctk.CTkLabel(frame3,
                                text="URL AES Key",
                                font=('Open sans',13,'bold'),
                                text_color=('black','black'),
                                fg_color=('#A4A4A4'))
        label3.place(x=15,y=6)

        label3= ctk.CTkLabel(frame4,
                                text="AES[File Encryption]",
                                font=('Open sans',21,'bold'),
                                text_color=('black','black'),
                                fg_color=('#D7D7D7'))
        label3.place(x=165,y=15)

        label4= ctk.CTkLabel(frame1,
                                text="RSA[AES Key Encryption]",
                                font=('Open sans',21,'bold'),
                                text_color=('black','black'),
                                fg_color=('#D7D7D7'))
        label4.place(x=135,y=11)

        self.ent_file_AES= ctk.CTkEntry(frame2,width=280,fg_color=('white'),text_color=('black'))
        self.ent_file_AES.place(x=130,y=8)

        self.ent_public= ctk.CTkTextbox(frame1,width=257,height=104,fg_color=('white'),text_color=('black'))
        self.ent_public.place(x=15,y=225)

        self.ent_private= ctk.CTkTextbox(frame1,width=257,height=104,fg_color=('white'),text_color=('black'))
        self.ent_private.place(x=275,y=225)

        self.ent_key_AES= ctk.CTkEntry(frame3,width=350,fg_color=('white'),text_color=('black'))
        self.ent_key_AES.place(x=18,y=35)

        self.ent_AES= ctk.CTkTextbox(frame4,width=500,height=128,fg_color=('white'),text_color=('black'))
        self.ent_AES.place(x=28,y=165)

        self.combobox = ctk.CTkOptionMenu(frame1,font=('Open sans',12,'normal'),fg_color='#DB5C5C',width=150,height=26,
                                       values=["1024", "2048","4096"],
                                       command=self.callback_bit)
        self.combobox.place(x=20,y=140)
        self.combobox.set("Panjang Kunci RSA")  # set initial value
        
        self.combobox = ctk.CTkOptionMenu(frame4,font=('Open sans',12,'normal'),fg_color='#E4AD5A',width=150,height=26,
                                       values=["16", "24","32"],
                                       command=self.callback_bytes)
        self.combobox.place(x=20,y=80)
        self.combobox.set("Panjang Kunci AES (BYTES)")  # set initial value
    
    def callback_bit(self, value):
        self.bit = value

    def callback_bytes(self, value):
        self.bytes = value

    def open_file(self):
        file_name = tk.filedialog.askopenfilename() 
        self.ent_file_AES.delete(0,'end')
        self.ent_file_AES.insert(0,file_name)

    def open_file2(self):
        file_name = tk.filedialog.askopenfilename() 
        self.ent_key_AES.delete(0, 'end')
        self.ent_key_AES.insert(0, file_name)

    def callback_key_RSA(self):
        public_key, private_key= self.backend.generate_key_RSA(int(self.bit))
        self.ent_public.delete(1.0,'end')
        self.ent_private.delete(1.0,'end')
        self.ent_public.insert(1.0, public_key, 'end')
        self.ent_private.insert(1.0, private_key, 'end')

    def callback_key_AES(self):
        key = self.backend.generate_key_AES(int(self.bytes))
        self.ent_AES.delete(1.0, 'end')
        self.ent_AES.insert(1.0, key)

    def callback_encrypt(self):
        filename = self.ent_file_AES.get()
        key = self.ent_AES.get(1.0, 'end')
        self.backend.encrypt_file(filename,key)

    def callback_decrypt(self):
        filename = self.ent_file_AES.get()
        key = self.ent_AES.get(1.0, 'end')
        self.backend.decrypt_file(filename,key)

    def callback_encrypt_RSA(self):
        file = self.ent_key_AES.get()
        key = self.ent_public.get(1.0, 'end')
        self.backend.encrypt_RSA(file,key)

    def callback_decrypt_RSA(self):
        file = self.ent_key_AES.get()
        key = self.ent_private.get(1.0, 'end')
        self.backend.decrypt_RSA(file,key)       

app = MyApp('RSA', (1200,500))
app.mainloop()