import math

def main():
    try:
        angka = int(input("Masukkan bilangan bulat: "))
        hasil = angka / 3
        hasil_format = "{:.3f}".format(hasil)
        print("hasil:", hasil_format)
    except ValueError:
        print("Silahkan masukkan bilangan bulat yang valid.")

if __name__ == "__main__":
    main()