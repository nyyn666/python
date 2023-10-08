try:
    with open('dane1.txt', 'r') as file:
        numbers = [float(line.strip()) for line in file]

def pobierz_jeden_wiersz_jedna_wartosc(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            zawartosc = plik.read()
            return float(zawartosc)
    except FileNotFoundError:
        print(f"Plik '{nazwa_pliku}' nie istnieje.")
    except ValueError:
        print("Błąd: Nie można przekonwertować wartości na liczbę.")

# Przykład użycia
nazwa_pliku = "dane1.txt"
wartosc = pobierz_jeden_wiersz_jedna_wartosc(nazwa_pliku)
print(f"Wartość z pliku: {wartosc}")
##############################
##############################
##############################
def pobierz_jeden_wiersz_wiele_wartosci(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            zawartosc = plik.readline().split()
            return [float(x) for x in zawartosc]
    except FileNotFoundError:
        print(f"Plik '{nazwa_pliku}' nie istnieje.")
    except ValueError:
        print("Błąd: Nie można przekonwertować wartości na liczby.")

# Przykład użycia
nazwa_pliku = "dane2.txt"
wartosci = pobierz_jeden_wiersz_wiele_wartosci(nazwa_pliku)
print(f"Wartości z pliku: {wartosci}")
##############################
##############################
##############################
def podstawowa_analiza(liczby):
    if not liczby:
        return None

    min_wartosc = min(liczby)
    max_wartosc = max(liczby)
    srednia = sum(liczby) / len(liczby)
    ilosc_parzystych = sum(1 for x in liczby if x % 2 == 0)
    ilosc_nieparzystych = len(liczby) - ilosc_parzystych
    liczby_wieksze_od_sredniej = sum(1 for x in liczby if x > srednia)
    liczby_mniejsze_od_sredniej = sum(1 for x in liczby if x < srednia)
    ilosc_pierwszych = sum(1 for x in liczby if jest_pierwsza(x))

    return {
        "Min": min_wartosc,
        "Max": max_wartosc,
        "Średnia": srednia,
        "Parzyste": ilosc_parzystych,
        "Nieparzyste": ilosc_nieparzystych,
        "Liczby większe od średniej": liczby_wieksze_od_sredniej,
        "Liczby mniejsze od średniej": liczby_mniejsze_od_srednia,
        "Liczby pierwsze": ilosc_pierwszych
    }

# Przykład użycia
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wyniki = podstawowa_analiza(liczby)
for klucz, wartosc in wyniki.items():
    print(f"{klucz}: {wartosc}")
##############################
##############################
##############################
    import math

def oblicz_nwd(a, b):
    while b:
        a, b = b, a % b
    return a

# Przykład użycia
a = 48
b = 18
nwd = oblicz_nwd(a, b)
print(f"NWD({a}, {b}) = {nwd}")
##############################
##############################
##############################
def lider_zbioru(liczby):
    if not liczby:
        return None
    licznik = {}
    for liczba in liczby:
        if liczba in licznik:
            licznik[liczba] += 1
        else:
            licznik[liczba] = 1
    lider = max(licznik, key=licznik.get)
    ilosc_wystapien = licznik[lider]
    return {
        "Lider zbioru": lider,
        "Ilość wystąpień lidera": ilosc_wystapien
    }

# Przykład użycia
liczby = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
wynik = lider_zbioru(liczby)
for klucz, wartosc in wynik.items():
    print(f"{klucz}: {wartosc}")
##############################
##############################
##############################
def ilosc_palindromow_dziesietnie(liczby):
    if not liczby:
        return 0
    ilosc = 0
    for liczba in liczby:
        if jest_palindromem(str(int(liczba))):
            ilosc += 1
    return ilosc

# Funkcja pomocnicza do sprawdzania, czy ciąg znaków jest palindromem
def jest_palindromem(tekst):
    return tekst == tekst[::-1]

# Przykład użycia
liczby = [121, 123, 1331, 22, 555]
ilosc = ilosc_palindromow_dziesietnie(liczby)
print(f"Ilość liczb palindromowych dziesiętnie: {ilosc}")
#######
#######
#######
def ilosc_palindromow_dwojkowo(liczby):
    if not liczby:
        return 0
    ilosc = 0
    for liczba in liczby:
        if jest_palindromem(bin(int(liczba))[2:]):
            ilosc += 1
    return ilosc

# Przykład użycia
liczby = [9, 10, 15, 18, 31]
ilosc = ilosc_palindromow_dwojkowo(liczby)
print(f"Ilość liczb palindromowych dwójkowo: {ilosc}")