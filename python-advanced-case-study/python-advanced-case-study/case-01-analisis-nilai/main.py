"""Analisis nilai akhir dan pemeringkatan mahasiswa."""

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 82, "uts": 78, "uas": 84},
    {"nama": "Eka", "nim": "230105", "tugas": 76, "uts": 88, "uas": 90},
]

# List comprehension untuk menghitung nilai akhir setiap mahasiswa.
mahasiswa_dengan_nilai = [
    {
        **m,
        "nilai_akhir": round(
            m["tugas"] * 0.30 + m["uts"] * 0.30 + m["uas"] * 0.40, 2
        ),
    }
    for m in data_mahasiswa
]

# sorted() dengan lambda mengurutkan nilai akhir dari tertinggi ke terendah.
ranking = sorted(
    mahasiswa_dengan_nilai,
    key=lambda mahasiswa: mahasiswa["nilai_akhir"],
    reverse=True,
)

berprestasi = [
    mahasiswa for mahasiswa in ranking if mahasiswa["nilai_akhir"] > 80
]

print("=" * 58)
print("             ANALISIS NILAI MAHASISWA")
print("=" * 58)
print("\nRANKING MAHASISWA")
for nomor, m in enumerate(ranking, start=1):
    print(
        f"{nomor}. {m['nama']:<10} NIM: {m['nim']} | "
        f"Tugas: {m['tugas']:>3} | UTS: {m['uts']:>3} | "
        f"UAS: {m['uas']:>3} | Akhir: {m['nilai_akhir']:>5.2f}"
    )

print("\nMAHASISWA BERPRESTASI (nilai akhir > 80)")
for m in berprestasi:
    print(f"- {m['nama']} ({m['nim']}): {m['nilai_akhir']:.2f}")

terbaik = ranking[0]
print("\nMAHASISWA TERBAIK")
print(f"Nama       : {terbaik['nama']}")
print(f"NIM        : {terbaik['nim']}")
print(f"Nilai akhir: {terbaik['nilai_akhir']:.2f}")
