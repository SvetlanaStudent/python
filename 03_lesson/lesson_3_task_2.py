
from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79123456789")),
catalog.append(Smartphone("Apple", "iPhone 14", "+79123456567")),
catalog.append(Smartphone("Google", "Pixel 6", "+79124579656")),
catalog.append(Smartphone("OnePlus", "OnePlus 9", "+79123456517")),
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79123450567"))

for phone in catalog:
    print(f"Марка:{phone.brand},модель:{phone.model},номер телефона:{phone.phone_number}")
