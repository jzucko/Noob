import os
import datetime
import json
#import korisno

def kreiranje_racuna():
    podaci={}
    counter=1
    while True:
        ime=input('Unesite ime osobe: ')
        prezime=input('Unesite prezime osobe: ')
        adresa= input('Unesite ulicu, postanski broj i grad: ')
        OIB= input ('Unesite OIB: ')
        if len(OIB) == 11:
            print('Unijeli ste OIB s dovoljnim brojem znakova.')
        else:
            print('OIB mora imati točno 11 znakova, pokušajte ponovno. ')
            return
        uloga= input ('Označite ulogu kao admin ili user. ')
        while uloga != 'admin' and uloga != 'user':
            print('Pogrešno ste označili ulogu, pokušajte ponovno.')
        sifra=input('Unesite željenu šifru: ')
        print('Uspješno ste pohranili podatke.')
              
        podaci[counter]={
                    'Ime':ime,
                    'Prezime':prezime,
                    'Adresa':adresa,
                    'OIB':OIB,
                    'Uloga':uloga,
                    'Sifra':sifra
                    } 
        counter+=1
        
        try:
            with open('korisnici.json', 'w', encoding='utf-8') as json_file:
                json.dump(podaci, json_file, indent=4)           
        except Exception as e:
            print(f'Dogodila se greska {e}')
            
        if input('Unesite x za izlaz. ')=='x':
            break
        
kreiranje_racuna()
    
#log in screen sa unosom password, provjera u odnosu na md5/sha2
#kategorija admin/user
#admin - novi korisnici, brisanje korisnika
#user vlastiti profil editira
#logout za sve
