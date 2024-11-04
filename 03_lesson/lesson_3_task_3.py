from Address import Address
from Mailing import Mailing

to_address = Address("12378", "Орел", "Комсомольская", "д.45", "кв.567")
from_address = Address("56789", "Москва", "Лесная", "д.56", "кв.3")
mailing = Mailing(to_address, from_address, 3500, "TRK12345")

output = (
 f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
 f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
 f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
 f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
print(output)
