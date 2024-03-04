def main():
    try:
        angka = int(input("Masukkan angka: "))
        if angka < 1:
            print("Silahkan masukkan bilangan bulat positif.")
            return
        
        total_sum = sum(range(1, angka + 1))
        print("Jumlah semua nilai dari 1 hingga", angka, "adalah:", total_sum)
    except ValueError:
        print("Silahkan masukkan bilangan bulat.")

if __name__ == "__main__":
    main()