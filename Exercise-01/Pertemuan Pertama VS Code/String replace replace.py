from tracemalloc import start


start
tulisan_1= "nama saya agung, saya tinggal di kota surakarta adalah kota di jateng"
print(tulisan_1)
tulisan_1 = tulisan_1.replace('agung','henry')
tulisan_1 = tulisan_1.replace('kota surakarta','kota bogor')
tulisan_1 = tulisan_1.replace('jateng','bogor')
print(tulisan_1)