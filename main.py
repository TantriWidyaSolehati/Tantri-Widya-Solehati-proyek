from src.input_data import input_nilai
from src.proses import ringkasan
from src.output import tampilkan_hasil


def main():
	print("=" * 40)
	print("PROGRAM ANALISIS NILAI SISWA")
	print("=" * 40)

	nilai = input_nilai()

	hasil = ringkasan(nilai)

	tampilkan_hasil(hasil)


if __name__ == "__main__":
	main()
