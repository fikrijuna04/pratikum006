from view.view_nilai import cari, cetak, header, notoption
from view.input_nilai import inputan, edit, delete
header()


while True:
    c = input(" [(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar ] :  ")

    if c.lower() == 'k':
        print(".:TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI:.")
        ext = input("\nPress ENTER to exit")
        if ext == '':
            break
        else:
            break

    elif c.lower() == 'l':
        cetak()

    elif c.lower() == 't':
        inputan()

    elif c.lower() == 'u':
        edit()

    elif c.lower() == 'c':
        cari()

    elif c.lower() == 'h':
        delete()

    else:
        notoption()
