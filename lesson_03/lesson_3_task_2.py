from lesson_03.smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79001234567"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79007654321"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79009876543"))
catalog.append(Smartphone("Google", "Pixel 8", "+79001112233"))
catalog.append(Smartphone("OnePlus", "12", "+79004445566"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
