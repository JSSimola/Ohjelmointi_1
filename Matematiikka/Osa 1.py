import numpy as np

print("Tehtävä 1")

print("T1")
print(f"a): {np.degrees(2.493)}")
print(f"b): {np.degrees(0.911)}")
print("----------")

print("T2")
print(f"a): {np.radians(137.7)}")
print(f"b): {np.radians(62.3)}")
print("----------")

print("T3")
kulmat = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
for i in kulmat:
    print(np.radians(i))
print("--------")
print("Tehtävä 2")

print(f"{np.hypot(1.6, 2.3)} m")
