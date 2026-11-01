BATAS_LULUS = 60


def hitung_rata_rata(nilai):
	if not nilai:
		return 0

	return sum(nilai) / len(nilai)


def status_lulus(nilai, batas=BATAS_LULUS):
	return [x for x in nilai if x >= batas]


def ringkasan(nilai):
	return {
		"jumlah_data": len(nilai),
		"rata_rata": hitung_rata_rata(nilai),
		"nilai_minimum": min(nilai),
		"nilai_maksimum": max(nilai),
		"jumlah_lulus": len(status_lulus(nilai)),
		"jumlah_tidak_lulus": len(nilai) - len(status_lulus(nilai))
	}
