

class Address:
    def __init__(self, street, number, flat_number, city, zip_code):
        self.street = street
        self.number = number
        self.flat_number = flat_number
        self.city = city
        self.zip_code = zip_code
        self.vowels = 'aeiouy'
        self.count_vowels = 0
        self.check_string()

    def create_string(self):
        return self.street + self.number + self.city

    def check_vowels(self, letter):
        if letter in self.vowels:
            return True
        return False

    def check_string(self):
        string_to_check = self.create_string().lower()
        for letter in string_to_check:
            if self.check_vowels(letter):
                self.count_vowels += 1



list_of_address = [
        Address(
            "Serniczkowa",
            "4B",
            2,
            "Krakow",
            "02-326"
        ),
        Address(
            "Pierniczkowa",
            "289A",
            55,
            "Gdansk",
            "02-326"
        ),
        Address(
            "Barszczykowa",
            "234",
            5,
            "Rzeszow",
            "37-326"
        ),
        Address(
            "Uszkowa",
            "43H",
            5,
            "Wroclaw",
            "02-326"
        ),
        Address(
            "Cukierkowa",
            "23I",
            5,
            "Poznan",
            "02-326"
        )
    ]
santa_bill_list = [(x.count_vowels*2) for x in list_of_address]
santa_bill = sum(santa_bill_list)
print(f'Santa has to pay {santa_bill} zl')