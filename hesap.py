def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    if y != 0:
        return x / y
    else:
        return "Hata: Sıfıra bölme hatası!"

while True:
    print("Lütfen bir işlem seçin (+, -, *, /) veya 'q' çıkış yapmak için:")
    secim = input()
    
    if secim == 'q':
        break
    
    if secim in ('+', '-', '*', '/'):
        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
            
            if secim == '+':
                sonuc = topla(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")
            elif secim == '-':
                sonuc = cikar(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")
            elif secim == '*':
                sonuc = carp(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")
            elif secim == '/':
                sonuc = bol(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")
        except ValueError:
            print("Hata: Geçersiz bir giriş. Lütfen sayılar ve işlemi doğru formatta girin.")
    else:
        print("Hata: Geçersiz bir işlem seçtiniz. Lütfen tekrar deneyin.")