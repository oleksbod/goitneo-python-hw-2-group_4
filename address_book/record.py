from name import Name
from phone import Phone 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):        
        if not list(filter(lambda p: p.value == phone, self.phones)):
            self.phones.append(Phone(phone))
        else:
            print(f"Phone number {phone} already exists for {self.name.value}.")

    def remove_phone(self, phone):       
        self.phones = list(filter(lambda p: p.value != phone, self.phones))

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        print(f"Phone number {old_phone} not found for {self.name.value}.")

    def find_phone(self, phone):       
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"