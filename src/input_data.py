def input_nilai():
	"""
	Meminta pengguna memasukkan beberapa nilai siswa.
	Pisahkan nilai dengan koma.
	Contoh: 70,80,90
	"""

	while True:
		try:
			data = input("Masukkan nilai siswa (pisahkan dengan koma): ")

			nilai = [int(x.strip()) for x in data.split(",")]

			if len(nilai) == 0:
				print("Data tidak boleh kosong.")
				continue

			return nilai

		except ValueError:
			print("Input tidak valid! Masukkan angka saja.")
