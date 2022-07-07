from datetime import date


class Invoice:

    def __init__(self, name: str, surname: str, invoice_date: date, price: float):
        self.name = name
        self.surname = surname
        self.invoice_date = invoice_date
        self.price = price

