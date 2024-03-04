import math

def main():
    try:
        gaji = float(input("Masukkan gaji tahunan Anda: "))
        gaji_bulanan = math.ceil(gaji / 12)
        print("Gaji bulanan Anda:", gaji_bulanan)
    except ValueError:
        print("Silahkan masukkan gaji yang valid.")

if __name__ == "__main__":
    main()