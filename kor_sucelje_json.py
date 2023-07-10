import os
import datetime
import json
import json


podaci={}
"""podaci={
    "admin": {
        "Ime": "ado",
        "Prezime": "admin",
        "Adresa": "aadmin",
        "OIB": "13245678912",
        "Uloga": "admin",
        "Sifra": "a1"
    }}"""

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
            continue
        uloga= input ('Označite ulogu kao admin ili user. ')
        if uloga != 'admin' and uloga != 'user':
            print('Pogrešno ste označili ulogu, pokušajte ponovno.')
            continue
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

  
"""def spremanje_podataka():
    try:
        with open('korisnici.json', 'a', encoding='utf-8') as json_file: #trebaš staviti append
            json.dump(podaci, json_file, indent=4)           
    except Exception as e:
        print(f'Dogodila se greska {e}')"""
        
def brisanje():
    prezime_b=input("Unesite prezime korisnika: ")

    if prezime_b not in podaci:
        print("Korisnik ne postoji")
        return
    del podaci[prezime_b]
    print("Korisnik je obrisan")
    
  
def promjena_podataka():
    prezime_p=input('Unesite prezime korisnika: ')
    if prezime_p in podaci:
        n_ime=input('Unesite novo ime: ')
        n_prezime=input('Unesite novo prezime: ')
        n_adresa=input('Unesite novu adresu: ')
        n_oib=input('Unesite novi oib: ')
        n_sifra=input('Unesite novu sifru: ')
        """podaci[prezime_p][ime]=n_ime
        podaci[prezime_p][prezime]=n_prezime
        podaci[prezime_p][adresa]=n_adresa
        podaci[prezime_p][oib]=n_oib
        podaci[prezime_p][sifra]=n_sifra"""
        #spremanje_podataka()
    else:
        print('Uneseni korisnik ne postoji. ')
        
def login():
    while True:
        prezime=input('Unesite prezime: ')
        sifra=input('Unesite sifru: ')
        
        with open('korisnici.json') as fr:
            korisnici=json.load(fr)
            
        if prezime in korisnici and sifra == korisnici[prezime]['Sifra']:
            print('Uspjesno ste se ulogirali')
            return True
        else:
            print('Neuspjesno ste se ulogirali')
        
def izbornik(prezime):
    if login():
        print('--- Dobrodošli u glavni izbornik: ---')
        print('1. Promjena podataka')
        print('2. Izlaz')
        if prezime == 'admin':
            print('3. Dodavanje korisnika')
            print('4. Brisanje korisnika')
        
                
while True:
    login()
    izbornik()
    izbor=input('Odaberite iz izbornika: ')
    
    if izbor == '1':
        promjena_podataka()
    elif izbor == '2':
        break
    elif izbor == '3':
        kreiranje_racuna()
    elif izbor == '4':
        brisanje()
    else:
        print('Pogrešan unos.')
            
    
#log in screen sa unosom password, provjera u odnosu na md5/sha2
#+++kategorija admin/user
#+++admin - novi korisnici, brisanje korisnika
#+++user vlastiti profil editira
#logout za sve


