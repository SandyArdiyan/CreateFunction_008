#prak 3 no
def konversi_suhu(nilai, satuan):

    if satuan == 'C':
        # Konversi dari Celsius ke Fahrenheit
        return (nilai * 9/5) + 32
    elif satuan == 'F':
        # Konversi dari Fahrenheit ke Celsius
        return (nilai - 32) * 5/9
    else:
        return "Satuan tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."
# Menggunakan fungsi konversi suhu
suhu_c = 25
suhu_f = konversi_suhu(suhu_c, 'C')
print(f"{suhu_c}°C = {suhu_f}°F")

suhu_f = 77
suhu_c = konversi_suhu(suhu_f, 'F')
print(f"{suhu_f}°F = {suhu_c}°C")