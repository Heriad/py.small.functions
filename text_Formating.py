import datetime

list_names = ["Kamil", "zofia", "kamila", "Ania"]
list_amountes = [124.45111, 199.993, 110, 112.102]

message = """Witaj {name}!
Dziękujemy za dokonany przez Ciebie zakup z dnia {date}
Całkowita kwota do zapłaty wynosi: {price}$.\n"""

def make_message(names, amountes):
    if len(names) == len(amountes):
        i = 0
        
        today = datetime.date.today()
        text = '{today.day}/{today.month}/{today.year}'.format(today=today)

        for name in list_names:
            if name[0].islower():
                name = name.title()
            new_amount = "%.2f" %(amountes[i])
            new_message = message.format(
                name=name,
                date=today,
                price=new_amount
            )
            i += 1
            print(new_message)

make_message(list_names, list_amountes)
