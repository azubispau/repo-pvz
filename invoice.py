from datetime import date

DATA_FILE = "duomenys.txt"


class Invoice:

    def __init__(self, name: str, surname: str, invoice_date: date, price: float):
        self.name = name
        self.surname = surname
        self.invoice_date = invoice_date
        self.price = price

    def get_formatted_data(self):
        return ";".join([self.name, self.surname, str(self.invoice_date), self.price])


def add_new_invoice(invoice: Invoice):
    with open(DATA_FILE, "w") as f:
        f.write(invoice.get_formatted_data())
