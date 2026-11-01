def tampilkan_hasil(data):
	print("\nHASIL ANALISIS")
	print("-" * 30)

	print(f"Jumlah Data       : {data['jumlah_data']}")
	print(f"Rata-rata         : {data['rata_rata']:.2f}")
	print(f"Nilai Minimum     : {data['nilai_minimum']}")
	print(f"Nilai Maksimum    : {data['nilai_maksimum']}")
	print(f"Jumlah Lulus      : {data['jumlah_lulus']}")
	print(f"Jumlah Tidak Lulus: {data['jumlah_tidak_lulus']}")
