print("Bismillaahirrohmaanirrohiim...")
tor = True 
while tor:

  print("Pilih Item :\njumbo, besar, abd, sedang, kecil, mini, maryam")
  item = str(input('masukkan item : '))
  
  if item == 'jumbo':
    print("Tortilla Jumbo")
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
    print('Tortilla Besar')
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
    print ('Tortilla ABD')
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
    print('Tortilla Sedang')
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
    print('Tortilla Kecil')
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
   
  elif item== 'mini':

    print('Tortilla Mini')
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

    print('Maryam')
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