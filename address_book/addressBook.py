from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):       
        self.data[record.name.value] = record

    def find(self, name):        
        return self.data.get(name)

    def delete(self, name):
        removed_record = self.data.pop(name, None)
        if removed_record is None:
            print(f"Record with name {name} not found.")