from lesson_03.address import Address
from lesson_03.mailing import Mailing

from_address = Address("123456", "Москва", "Тверская", "15", "42")

to_address = Address("654321", "Санкт-Петербург", "Невский", "7", "18")

mail = Mailing(to_address, from_address, 350.50, "TRACK123456")

print(f"Отправление {mail.track} из "
      f"{mail.from_address.index}, {mail.from_address.city}, "
      f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")
