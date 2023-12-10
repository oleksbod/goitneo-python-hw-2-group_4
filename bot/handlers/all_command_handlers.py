from decorators.errorsHandler import input_error 

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Conatct '{name}' exist!"
    contacts[name] = phone
    return "Contact added."

@input_error
def update_contact(args, contacts):
    name, phone = args
    phone = contacts[name]
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) > 1:
        raise IndexError
    name = args[0]
    phone = contacts[name]
    return phone
    
def show_all(contacts):
    if len(contacts) == 0:
        print("Where are no data")
        
    for key, value in contacts.items():
        print(f"{key}: {value}\n")