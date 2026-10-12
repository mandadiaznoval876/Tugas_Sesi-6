# Case 02 — Streaming Data Sensor IoT

## Masalah yang diselesaikan
Program mensimulasikan 10 pembacaan suhu sensor. Setiap suhu diproses satu per satu dan langsung diberi status Dingin, Normal, atau Panas.

## Konsep Python
- **Generator function:** `baca_sensor()` menggunakan `yield` untuk menghasilkan nilai bertahap.
- **Iterator pattern:** `next()` mengambil satu pembacaan pada satu waktu.
- **Efisiensi memori:** data tidak dikumpulkan ke dalam list hasil yang besar.

Batas kategori mengikuti soal: Dingin jika suhu < 20°C, Normal jika 20–30°C, dan Panas jika > 30°C.

## Cara menjalankan
```bash
python main.py
```

Bukti output terminal tersedia pada `output.png`.
