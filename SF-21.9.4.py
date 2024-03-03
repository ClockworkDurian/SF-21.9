class Customers:
    def __init__(self, first_name,second_name,city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance
        self.city=city

    def get_guest(self):
        return f'{self.first_name} {self.second_name},г. {self.city}'


costomer_1 = Customers('Кшиштов', 'Мнишек', 'Варшава',50)
costomer_2 = Customers('Васисуалий','Лоханкин','Крыжополь',40)
costomer_3 = Customers('Дементий','Брудастый','Глупов',30)

guest_list=[costomer_1,costomer_2,costomer_3]


for guest in guest_list:
    print(guest.get_guest())