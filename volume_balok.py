class VolumeBalok:
    __instance = None

    def __init__(self, panjang, lebar, tinggi):
        if VolumeBalok.__instance is not None:
            raise Exception("Hanya diizinkan memiliki satu objek VolumeBalok")
        VolumeBalok.__instance = self
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    @staticmethod
    def get_instance():
        if VolumeBalok.__instance is None:
            VolumeBalok.__instance = VolumeBalok(0, 0, 0)
        return VolumeBalok.__instance

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi


# Contoh penggunaan
volume_balok = VolumeBalok.get_instance()
volume_balok.panjang = 3
volume_balok.lebar = 4
volume_balok.tinggi = 5

hasil_volume = volume_balok.hitung_volume()

print(f"Panjang balok: {volume_balok.panjang} m")
print(f"Lebar balok: {volume_balok.lebar} m")
print(f"Tinggi balok: {volume_balok.tinggi} m")
print(f"Volume balok: {hasil_volume} m^3")
