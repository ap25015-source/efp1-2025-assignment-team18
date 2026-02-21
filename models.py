class Customer: # Represents a customer
    def __init__(self, customer_id: int, name: str, phone_number: int, loyalty_card_id: int):
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.loyalty_card_id=loyalty_card_id 

    def __str__(self) -> str: # String representation of the customer
        return f"{self.customer_id}: {self.loyalty_card_id} {self.name} {self.phone_number}" 

class FittingRoom: # Represents a fitting room
    def __init__(self, fitting_room_id: int):
        self.fitting_room_id = fitting_room_id

    def get_id(self) -> int:
     #Returns the ID of the fitting room.
        return self.fitting_room_id   
        

class Employee: # Represents an Employee
    def __init__(self, employee_id: int, availability: bool, name: str, phone_number: int):
        self.employee_id = employee_id
        self.availability = availability
        self.name = name
        self.phone_number = phone_number

    def is_available(self) -> bool:
        # TODO: επιστρέψτε True αν υπάρχει διαθεσιμότητα  υπαλλήλου
        return self.availability
    
    def get_id(self) -> int:
        # Επιστρέφει το ID του υπαλλήλου
        return self.employee_id


class ClothingItem: # Represents a garment
    def __init__(self, clothingitem_id:int, barcode: int, description: str, brand: str, photos: list, available_colours: str, price: float):
        self.clothingitem_id= clothingitem_id
        self.barcode = barcode
        self.description = description
        self.brand = brand 
        self.photos = photos
        self.available_colours = available_colours
        self.price = price

    def get_id(self) -> int:
        # Επιστρέφει το ID του ρούχου
        return self.clothingitem_id
    
class NotificationMessage: # Represents a notification message
    def __init__(self, notification_message_id: int, sms: str):
        self.notification_message_id= notification_message_id
        self.sms= sms
  
    def get_id(self) -> int:
        # Επιστρέφει το ID του μυμήματος για βοήθεια
        return self.clnotification_message_id
    
class CustomerHelpService: # Represents helpservice offered to customer 
    def __init__(self,customer_help_service_id:int, customer: Customer, employee: Employee,clothingitem: ClothingItem, fittingroom: FittingRoom):
        self.customer_help_service_id= customer_help_service_id
        self.customer=customer
        self.employee=employee
        self.clothingitem=clothingitem
        self.fittingroom=fittingroom
