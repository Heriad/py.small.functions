list_names = ["Kamil", "Zofia", "Kamila", "Ania"]
list_amountes = [124.45111, 199.993, 110, 112.102]

# message = "Witaj {name}!\n" \
#           "Dziękujemy za zakup dnia: {date}\n" \
#           "Do zapłaty: {price}"

message = """Witaj {name}!
Dziękujemy za dokonany przez Ciebie zakup z dnia {date}
Całkowita kwota do zapłaty wynosi: {price}$.\n"""


def make_message(names, amountes):
    if len(names) == len(amountes):
        i = 0
        for name in list_names:
            new_amount = "%.2f" %(amountes[i])
            new_message = message.format(
                name=name,
                date="Some date",
                price=new_amount
            )
            i += 1
            print(new_message)


make_message(list_names, list_amountes)
