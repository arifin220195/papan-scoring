
tor = True 
while tor:
    print("Bismillaahirrahmaanirrahiim...")
    print("Pilih Item :\njumbo, besar, abd, sedang, kecil, mini, maryam")
    item = str(input('masukkan item : '))
  
    if item == 'jumbo':
        print("\n======================\n")
        print('==  Tortilla Jumbo  ==')
        print("\n======================\n")
        pack = 20
        keranjang = int(input('Jml Keranjang : '))
        sisa = int(input('Sisa : '))
        sortir = int(input('Sortir : '))
        total = (keranjang*pack)+sisa
        plus_Sortir = total + sortir
        print("\n======================\n")
        print('TOTAL JUMBO: ', total, 'pack')
        print('PLUS SORTIR : ', plus_Sortir, 'pack')
        print("\n======================\n") 

    elif item == 'besar':
        print("\n======================\n")
        print('==  Tortilla Besar  ==')
        print("\n======================\n")
        pack = 25
        keranjang = int(input('Jml Keranjang : '))
        sisa = int(input('Sisa : '))
        sortir = int(input('Sortir : '))
        total = (keranjang*pack)+sisa
        plus_Sortir = total + sortir
        print("\n======================\n")
        print('TOTAL BESAR: ', total, 'pack')
        print('PLUS SORTIR : ', plus_Sortir, 'pack')
        print("\n======================\n")

    elif item =='abd':
        print("\n======================\n")
        print('==  Tortilla ABD  ==')
        print("\n======================\n")
        pack = 50
        keranjang = int(input('Jml Keranjang : '))
        sisa = int(input('Sisa : '))
        sortir = int(input('Sortir : '))
        total = (keranjang*pack)+sisa
        plus_Sortir = total + sortir
        print("\n======================\n")
        print('TOTAL ABD: ', total, 'pack')
        print('PLUS SORTIR : ', plus_Sortir, 'pack')
        print("\n======================\n")
    elif item == 'sedang':
        print("\n======================\n")
        print('==  Tortilla Sedang  ==')
        print("\n======================\n")
        pack = 25
        keranjang = int(input('Jml Keranjang : '))
        sisa = int(input('Sisa : '))
        sortir = int(input('Sortir : '))
        total = (keranjang*pack)+sisa
        plus_Sortir = total + sortir
        print("\n======================\n")
        print('TOTAL SEDANG: ', total, 'pack')
        print('PLUS SORTIR : ', plus_Sortir, 'pack')
        print("\n======================\n")
  
    elif item == 'kecil':
        print("\n======================\n")
        print('==  Tortilla Kecil  ==')
        print("\n======================\n")
        pack = 33
        keranjang = int(input('Jml Keranjang : '))
        sisa = int(input('Sisa : '))
        sortir = int(input('Sortir : '))
        total = (keranjang*pack)+sisa
        plus_Sortir = total + sortir
        print("\n======================\n")
        print('TOTAL KECIL: ', total, 'pack')
        print('PLUS SORTIR : ', plus_Sortir, 'pack')
        print("\n======================\n")
   
    elif item == 'mini':
        print("\n======================\n")
        print('==  Tortilla Mini  ==')
        print("\n======================\n")
        pack = 40
        keranjang = int(input('Jml Keranjang : '))
        sisa = int(input('Sisa : '))
        sortir = int(input('Sortir : '))
        total = (keranjang*pack)+sisa
        plus_Sortir = total + sortir
        print("\n======================\n")
        print('TOTAL MINI: ', total, 'pack')
        print('PLUS SORTIR : ', plus_Sortir, 'pack')
        print("\n======================\n")

    elif item == 'maryam':
        print("\n======================\n")
        print('==  Maryam  ==')
        print("\n======================\n")
        pack = 50
        keranjang = int(input('Jml Keranjang : '))
        sisa = int(input('Sisa : '))
        sortir = int(input('Sortir : '))
        total = (keranjang*pack)+sisa
        plus_Sortir = total + sortir
        print("\n======================\n")
        print('TOTAL MARYAM: ', total, 'pack')
        print('PLUS SORTIR : ', plus_Sortir, 'pack')
        print("\n======================\n")

    else:
        print ('ALHAMDU LILLAAH WES MARI')
        break