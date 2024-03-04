def main():
    total_sum = 0
    while True:
        try:
            angka = int(input("Masukkan angka (-1 sampai selesai): "))
            if angka == -1:
                break
            total_sum += angka
        except ValueError:
            print("Silahkan masukkan bilangan bulat positif.")

    print("Jumlah semua angka yang dimasukkan andalah:", total_sum)

if __name__ == "__main__":
    main()