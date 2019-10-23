class Phone(object):
    def __init__(self, phone_number):
        self.number = self.clear_number(phone_number)
        self.area_code = self.number[:3]
        self.exchance_code = self.number[3:]

    def clear_number(self, phone_number):
        num = ''.join(i for i in phone_number if i.isdigit())
        if num.startswith('1'):
            num = num[1:]
        if len(num) != 10:
            raise ValueError('Wrong phone number')
        if num[0] == '0' or num[0] == '1':
            raise ValueError(f'Area code can not starts with {num[0]}')
        if num[3] == '0' or num[3] == '1':
            raise ValueError(f'Exchance code can not start with {num[3]}')
        return num

    def pretty(self):
        return f'({self.area_code}) {self.exchance_code[:3]}-{self.exchance_code[3:]}'
