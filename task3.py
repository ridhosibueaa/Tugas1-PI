def main():
    try:
        angka = float(input("Masukkan angka: "))
        if angka < 100:
            print("Kecil")
        elif angka <= 200:
            print("Sedang")
        else:
            print("Besar")
    except ValueError:
        print("Silahkan masukkan angka yang valid.")

if __name__ == "__main__":
    main()