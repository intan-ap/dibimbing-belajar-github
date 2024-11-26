import csv

def read_csv_file(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            print("Isi file CSV:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    read_csv_file("username.csv")
