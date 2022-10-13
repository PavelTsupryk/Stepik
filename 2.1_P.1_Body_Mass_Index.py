# Вес человека:
weight = float(input())
# Рост человека:
height = float(input())
BodyMassIndex = weight/(height ** 2)
if BodyMassIndex <= 18.5:
    # Under weight
    print("Недостаточная масса")
elif BodyMassIndex >= 25:
    # Over weight
    print("Избыточная масса")
else:
    # Optimal weight
    print("Оптимальная масса")
# print(BodyMassIndex)
