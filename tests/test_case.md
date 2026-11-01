# Test Case Analisis Nilai Siswa

| ID | Fitur | Input | Expected | Actual | Status |
|----|--------|--------|---------|---------|---------|
| TC01 | Rata-rata | 70,80,90 | 80.0 | 80.0 | PASS |
| TC02 | Batas Lulus | 60 | Lulus | Lulus | PASS |
| TC03 | Input Invalid | abc | Pesan Error | Pesan Error | PASS |
| TC04 | Nilai Minimum | 70,80,90 | 70 | 70 | PASS |
| TC05 | Nilai Maksimum | 70,80,90 | 90 | 90 | PASS |