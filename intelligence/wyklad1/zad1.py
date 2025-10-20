import datetime
import math

name = input("Name: ")
date = input("Year format year-month-day: ")
days = (datetime.datetime.now() - datetime.datetime(*map(int, date.split("-")))).days
map_dict = {
    "Physical wave": lambda d: round(math.sin((2 * math.pi / 23) * d), 2),
    "Emotional wave": lambda d: round(math.sin((2 * math.pi / 28) * d), 2),
    "Intellectual wave": lambda d: round(math.sin((2 * math.pi / 33) * d), 2),
}
print(f"Hello {name}, days {days}")

for key, func in map_dict.items():
    value = func(days)
    print(f"{key}: {value}")
    if value > 0.5:
        print(f"Congratulation {key}")
    else:
        print("Oh man")
        if func(days + 1) > value:
            print("Dont worry")

# point c: 10 minutes I guess

# point d:

try:
    name = input("Enter your name: ").strip()
    date_str = input("Enter your birth date (YYYY-MM-DD): ").strip()
    birth_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
except ValueError:
    print("❌ Invalid date format. Please use YYYY-MM-DD.")
    raise

days = (datetime.datetime.now() - birth_date).days
print(f"\nHello {name}! You have lived for {days} days.\n")

waves = {
    "Physical wave": lambda d: round(math.sin((2 * math.pi / 23) * d), 2),
    "Emotional wave": lambda d: round(math.sin((2 * math.pi / 28) * d), 2),
    "Intellectual wave": lambda d: round(math.sin((2 * math.pi / 33) * d), 2),
}

for wave_name, calc in waves.items():
    value = calc(days)
    print(f"{wave_name}: {value:+.2f}")

    if value > 0.5:
        print(f"🎉 Congratulations! Your {wave_name.lower()} is strong today.")
    else:
        print("😕 Oh man...")
        if calc(days + 1) > value:
            print("📈 But it's improving tomorrow!")

    print("-" * 40)

# point e: 1 minute

from datetime import date


def oblicz_biorytmy(t):
    fizyczny = math.sin(2 * math.pi * t / 23)
    emocjonalny = math.sin(2 * math.pi * t / 28)
    intelektualny = math.sin(2 * math.pi * t / 33)
    return fizyczny, emocjonalny, intelektualny


def interpretuj_biorytm(wartosc, nazwa, t):
    jutro = math.sin(2 * math.pi * (t + 1) / {"fizyczny": 23, "emocjonalny": 28, "intelektualny": 33}[nazwa])

    print(f"{nazwa.capitalize()} biorytm: {wartosc:.3f}")
    if wartosc > 0.5:
        print(f"Świetnie! Twój {nazwa} biorytm jest dziś wysoki! 💪")
    elif wartosc < -0.5:
        print(f"Niestety, Twój {nazwa} biorytm jest dziś niski 😞")
        if jutro > wartosc:
            print("Nie martw się. Jutro będzie lepiej! 🌤️")
        else:
            print("Wytrzymaj, to chwilowe. Odpocznij dziś trochę. 🌙")
    else:
        print(f"Twój {nazwa} biorytm jest dziś w normie. Zachowaj równowagę. ⚖️")
    print()


def main():
    print("=== Kalkulator biorytmów ===")
    imie = input("Podaj swoje imię: ")
    rok = int(input("Podaj rok urodzenia (np. 2000): "))
    miesiac = int(input("Podaj miesiąc urodzenia (1-12): "))
    dzien = int(input("Podaj dzień urodzenia (1-31): "))

    data_urodzenia = date(rok, miesiac, dzien)
    dzis = date.today()
    roznica = (dzis - data_urodzenia).days

    print(f"\nCześć, {imie}! Dziś jest {dzis}.")
    print(f"To Twój {roznica} dzień życia! 🎂\n")

    fiz, emo, intel = oblicz_biorytmy(roznica)

    interpretuj_biorytm(fiz, "fizyczny", roznica)
    interpretuj_biorytm(emo, "emocjonalny", roznica)
    interpretuj_biorytm(intel, "intelektualny", roznica)


if __name__ == "__main__":
    main()