"""Simulasi streaming data suhu sensor IoT dengan generator."""

def baca_sensor(jumlah=10):
    """Menghasilkan suhu satu per satu, tanpa membuat list besar."""
    suhu_sensor = [18.5, 19.8, 20.0, 22.4, 25.7, 29.9, 30.0, 31.2, 34.6, 37.8]
    for suhu in suhu_sensor[:jumlah]:
        yield suhu


def kategori_suhu(suhu):
    if suhu < 20:
        return "Dingin"
    if suhu <= 30:
        return "Normal"
    return "Panas"


def main():
    print("=" * 46)
    print("       STREAMING DATA SENSOR IoT")
    print("=" * 46)
    print(f"{'No.':<5}{'Suhu (°C)':<15}{'Status'}")
    print("-" * 46)

    # Iterator dikonsumsi satu per satu; tidak dikonversi menjadi list.
    sensor = baca_sensor()
    nomor = 0
    while True:
        try:
            suhu = next(sensor)
        except StopIteration:
            break
        nomor += 1
        print(f"{nomor:<5}{suhu:<15.1f}{kategori_suhu(suhu)}")

    print("-" * 46)
    print("Selesai: 10 pembacaan diproses secara bertahap.")


if __name__ == "__main__":
    main()
