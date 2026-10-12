# Case 03 — Sistem Keamanan Akun & Audit Log

## Masalah yang diselesaikan
Program memvalidasi format username dan password, memeriksa kecocokan akun, serta mencatat waktu, username, status, dan alasan penolakan untuk setiap percobaan login.

## Aturan validasi
- Username minimal 5 karakter dan hanya huruf/angka.
- Password minimal 8 karakter dan mengandung setidaknya satu angka.
- Pemeriksaan format menggunakan modul `re`.

## Konsep Python
- **OOP dan `@property`:** class `User` mengatur akses dan validasi atribut username/password.
- **RegEx:** `re.fullmatch()` memeriksa format kredensial.
- **Decorator:** `audit_log` membungkus fungsi login dan mencatat hasil otomatis.
- **Closure:** fungsi `wrapper` di dalam decorator menyimpan akses ke fungsi login yang dibungkus.

Akun demo yang digunakan: `Manda123` dengan password `Belajar123`. Ini hanya data contoh untuk tugas, bukan kredensial akun nyata.

## Cara menjalankan
```bash
python main.py
```

Bukti output terminal tersedia pada `output.png`.
