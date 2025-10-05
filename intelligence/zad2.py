from random import randrange
import math
import numpy as np
import matplotlib.pyplot as plt

castle = randrange(50, 340)
print(castle)
v0 = 50
h = 100
g = 9.81
hit = False

last_alpha_deg = None
last_time = None
last_d = None

while not hit:
    alpha_deg = float(input("Podaj kąt α (w stopniach): \n"))

    alpha = math.radians(alpha_deg)
    s = v0 * math.sin(alpha)
    d = (v0 * math.cos(alpha) / g) * (s + math.sqrt(s ** 2 + 2 * g * h))
    t = (s + math.sqrt(s ** 2 + 2 * g * h)) / g

    print(f'{d} \n')

    if abs(d - castle) <= 5:
        hit = True
        last_alpha_deg = alpha_deg
        last_time = t
        last_d = d

print("Hit")

alpha = math.radians(last_alpha_deg)
t_vals = np.linspace(0, last_time, 400)
x_vals = v0 * np.cos(alpha) * t_vals
y_vals = h + v0 * np.sin(alpha) * t_vals - 0.5 * g * t_vals**2
y_vals = np.maximum(y_vals, 0.0)

plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, linewidth=2)
plt.grid(True)
plt.xlabel("Odległość [m]")
plt.ylabel("Wysokość [m]")
plt.title(f"Trajektoria pocisku (α = {last_alpha_deg:.2f}°, zasięg ≈ {last_d:.2f} m)")
plt.xlim(left=0)
ymax = max(y_vals) * 1.1 if len(y_vals) > 0 else h * 1.1
plt.ylim(bottom=0, top=ymax)
plt.tight_layout()
plt.savefig("trajektoria.png", dpi=200)
plt.close()



# code by AI I think its pretty the same


import math
import numpy as np
import matplotlib.pyplot as plt
from random import randrange


def compute_distance(v0: float, alpha_deg: float, h: float, g: float = 9.81) -> tuple[float, float]:
    """Oblicza odległość (zasięg) i czas lotu dla danego kąta."""
    alpha = math.radians(alpha_deg)
    s = v0 * math.sin(alpha)
    d = (v0 * math.cos(alpha) / g) * (s + math.sqrt(s**2 + 2 * g * h))
    t = (s + math.sqrt(s**2 + 2 * g * h)) / g
    return d, t


def simulate_trajectory(v0: float, alpha_deg: float, h: float, t_max: float, g: float = 9.81):
    """Generuje punkty (x, y) trajektorii."""
    alpha = math.radians(alpha_deg)
    t_vals = np.linspace(0, t_max, 400)
    x_vals = v0 * np.cos(alpha) * t_vals
    y_vals = h + v0 * np.sin(alpha) * t_vals - 0.5 * g * t_vals**2
    y_vals = np.maximum(y_vals, 0)
    return x_vals, y_vals


def main():
    castle = randrange(50, 340)
    print(f"🏰 Odległość do zamku: {castle} m\n")

    v0 = 50  # prędkość początkowa
    h = 100  # wysokość początkowa
    g = 9.81

    last_alpha_deg = None
    last_time = None
    last_d = None

    while True:
        try:
            alpha_deg = float(input("Podaj kąt α (w stopniach): "))
        except ValueError:
            print("❌ Podaj poprawną liczbę.")
            continue

        d, t = compute_distance(v0, alpha_deg, h, g)
        print(f"➡️  Zasięg: {d:.2f} m")

        if abs(d - castle) <= 5:
            print("\n🎯 TRAFIONY ZAMEK!\n")
            last_alpha_deg, last_time, last_d = alpha_deg, t, d
            break
        elif d < castle:
            print("🟡 Za krótko — spróbuj większy kąt.\n")
        else:
            print("🔵 Za daleko — spróbuj mniejszy kąt.\n")

    # Rysowanie wykresu
    x_vals, y_vals = simulate_trajectory(v0, last_alpha_deg, h, last_time, g)

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label=f"Trajektoria (α = {last_alpha_deg:.1f}°)")
    plt.axvline(castle, color="red", linestyle="--", label="Zamek")
    plt.scatter([last_d], [0], color="green", zorder=5, label="Trafienie")

    plt.grid(True, linestyle="--", alpha=0.7)
    plt.xlabel("Odległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.title("Symulacja lotu pocisku")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
