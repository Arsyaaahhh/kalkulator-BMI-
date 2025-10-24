
print("Perhitungan BMI")
print("--------------------------------------")

berat_badan = float(input("Masukkan berat badan anda(kg) : ")) #user akan memasukkan 
tinggi_badan = float(input("Masukkan tinggi badan anda(meter) : ")) #jadikan 1 float dan input lebih simpel dan auto konversi integer ke float

BMI = berat_badan/(tinggi_badan**2)

berat_ideal = dict()
berat_ideal['minimum'] = 18.5*(tinggi_badan**2)
berat_ideal['maksimal'] = 25*(tinggi_badan**2)

print("\n--------------------------------------")
print(f"Nilai BMI anda adalah {BMI:.2f} kg/m^2")
print("BMI ideal adalah 18.5 - 25 kg")
print(f"berat ideal anda {berat_ideal['minimum']:.2f}kg - {berat_ideal['maksimal']:.2f}kg")


if BMI < 18.5 :
    kategori = "Kekurangan berat badan cuy"
elif 18.5 <= BMI <= 25:
    kategori = "Normal cihuy"
elif 25 <= BMI <= 30:
    kategori = "Kelebihan jir"
if BMI > 30:
    kategori = "Apalah"

print(kategori)

print("\nThank you for using this program :)")

