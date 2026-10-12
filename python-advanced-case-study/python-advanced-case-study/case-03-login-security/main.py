"""Validasi akun dan pencatatan audit login."""

import re
from datetime import datetime
from functools import wraps


class User:
    """Model pengguna dengan validasi atribut username dan password."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9]{5,}", value):
            raise ValueError(
                "Username harus minimal 5 karakter dan hanya berisi huruf/angka."
            )
        self._username = value

    @property
    def password(self):
        # Password tidak ditampilkan secara langsung.
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or not re.fullmatch(r"(?=.*\d).{8,}", value):
            raise ValueError(
                "Password harus minimal 8 karakter dan mengandung setidaknya 1 angka."
            )
        self._password = value


def audit_log(function):
    """Decorator untuk mencatat hasil setiap percobaan login."""

    @wraps(function)
    def wrapper(username, password, *args, **kwargs):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            hasil = function(username, password, *args, **kwargs)
            print(f"[AUDIT] {waktu} | user={username!r} | BERHASIL")
            return hasil
        except (ValueError, PermissionError) as error:
            print(
                f"[AUDIT] {waktu} | user={username!r} | "
                f"DITOLAK | Alasan: {error}"
            )
            return False

    return wrapper


# Contoh data akun yang sudah terdaftar.
akun_terdaftar = {
    "Manda123": "Belajar123",
}


@audit_log
def login(username, password):
    """Memeriksa format kredensial dan mencocokkannya dengan data akun."""
    # Validasi tetap menggunakan RegEx meskipun akun tidak ditemukan.
    if not isinstance(username, str) or not re.fullmatch(r"[A-Za-z0-9]{5,}", username):
        raise ValueError(
            "Username harus minimal 5 karakter dan hanya berisi huruf/angka."
        )
    if not isinstance(password, str) or not re.fullmatch(r"(?=.*\d).{8,}", password):
        raise ValueError(
            "Password harus minimal 8 karakter dan mengandung setidaknya 1 angka."
        )

    # Buat objek User agar aturan enkapsulasi @property juga diterapkan.
    User(username, password)

    if username not in akun_terdaftar or akun_terdaftar[username] != password:
        raise PermissionError("Username atau password tidak cocok.")
    return True


def main():
    print("=" * 68)
    print("           SISTEM KEAMANAN AKUN & AUDIT LOG")
    print("=" * 68)

    print("\n1. Username tidak valid:")
    login("man@", "Belajar123")

    print("\n2. Password terlalu pendek:")
    login("Manda123", "abc1")

    print("\n3. Password tidak mengandung angka:")
    login("Manda123", "Belajarku")

    print("\n4. Login dengan kredensial benar:")
    if login("Manda123", "Belajar123"):
        print("Akses diberikan. Selamat datang, Manda123!")


if __name__ == "__main__":
    main()
