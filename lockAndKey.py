## This program allows you to encrypt and decrypt text using the following encryption techniques/ciphers:
##    'Affine Cipher', 'Autokey Cipher', 'Caesar Cipher', 'Hill Cipher', 'Multiplicative Cipher', 'Vignere Cipher'
## using tkinter GUI. Written in Python 3.6
##
## Here is the naming scheme of variables used:
##    DK  - Decryption Key                eg: 'entryDK' will be the name of the entry box that stores the Decryption key
##    EK  - Encryption Key                eg: 'entryEK' will be the name of the entry box that stores the Encryption key    
##    EPT - Encryption PlainText          eg: 'entryEPT' will be the name of the entry box that stores the plaintext to be encrypted
##    DPT - Decryption PlainText          eg: 'entryDPT' will be the name of the entry box that stores the plaintext after Decryption
##    ECT - Encryption PlainText          eg: 'entryECT' will be the name of the entry box that stores the ciphertext after encryption
##    DCT - Decryption CipherText         eg: 'entryDCT' will be the name of the entry box that stores the ciphertext to be Decrypted
## Currently Implemented ciphers - 'Caesar Cipher'
    
from tkinter import *
from tkinter import ttk

class mainWindow:
    
    def __init__(self,master):
        cipher='temp'
        self.master=master
        master.title('Lock And Key')
        self.var = StringVar(master)
        self.listOfCiphers=['Select a cipher',
                            'Affine Cipher',
                            'Autokey Cipher',
                            'Caesar Cipher',
                            'Hill Cipher',
                            'Multiplicative Cipher',
                            'Vignere Cipher']
        self.var.set(' Click to select Cipher from this list')
        self.optionCiphers=ttk.OptionMenu(master, self.var, *self.listOfCiphers, command=self.selectedOption)
        self.optionCiphers.pack()
        #print(self.optionCiphers.config(self.listOfCiphers))

        self.labelED=Label(master, text='Encryption:')
        self.labelED.pack()

        self.labelEK=Label(master, text="Enter the key")
        self.labelEK.pack()

        self.entryEK=Entry(master)
        self.entryEK.pack()

        self.labelEPT= Label(master, text='Enter plaintext')
        self.labelEPT.pack()

        self.entryEPT=Entry(master)
        self.entryEPT.pack()

        self.ebtn=ttk.Button(master,text='Encrypt', command=lambda:self.encrypt(cipher))
        self.ebtn.pack()

        self.labelECT = Entry(master)
        self.labelECT.configure(state="readonly")
        self.labelECT.pack()
        #end of encryption
        self.labelBlank=Label(master,text=" ")
        self.labelBlank.pack()
        #start of decryption
        self.labelD=Label(master, text='Decryption:')
        self.labelD.pack()

        self.labelDK=Label(master, text="Enter the key")
        self.labelDK.pack()

        self.entryDK=Entry(master)
        self.entryDK.pack()

        self.labelDPT= Label(master, text='Enter cipher text')
        self.labelDPT.pack()

        self.entryDPT=Entry(master)
        self.entryDPT.pack()

        self.dbtn=ttk.Button(master,text='Decrypt', command=lambda:self.decrypt(cipher))
        self.dbtn.pack()

        self.labelDCT = Entry(master)
        self.labelDCT.configure(state="readonly")
        self.labelDCT.pack()

    def selectedOption(self,option):
        self.cipher=option
        
    def caesar(self,key,plaintext):
        key=int(key)
        alphabets="abcdefghijklmnopqrstuvwxyz"
        #listPT=list(plaintext)
        #listAlpha=list(alphabets)
        cipherText=[0]*len(plaintext)
        for i in range(0, len(plaintext)):
            if plaintext[i] == ' ':
                print('im retarded')
                cipherText[i] = '_'
            else:
                cipherText[i]=alphabets[(alphabets.index(plaintext[i])+key)%26]
        return cipherText

    def decryptCaesar(self,key,ciphertext):
        key=int(key)
        alphabets="abcdefghijklmnopqrstuvwxyz"
        #listCT=list(ciphertext)
        #listAlpha=list(alphabets)
        plainText=[0]*len(ciphertext)
        for i in range(0, len(ciphertext)):
            if ciphertext[i] == ' ':
                plainText[i] = '_'
            else:
                plainText[i]=alphabets[(alphabets.index(ciphertext[i])-key)%26]
        return plainText

    def encrypt(self,cipher):
        if self.cipher == 'Caesar Cipher':
            ct=self.caesar(self.entryEK.get(), self.entryEPT.get())
        self.labelECT.config(state='normal')
        self.labelECT.delete(0, END)
        self.labelECT.insert(0, ct)
        self.labelECT.config(state='readonly')
        
    def decrypt(self, cipher):
        if self.cipher =='Caesar Cipher':
            pt=self.decryptCaesar(self.entryDK.get(), self.entryDPT.get())
        self.labelDCT.config(state='normal')
        self.labelDCT.delete(0, END)
        self.labelDCT.insert(0, pt)
        self.labelDCT.config(state='readonly')
        

   


root=Tk()
mainWindow(root)
root.mainloop()



            


