class Customer: # Represents a customer
    def __init__(self, customer_id: int, fitting_room_id: int, loyalty_card_id: int, request_support: str):
        self.customer_id = customer_id
        self.fitting_room_id = fitting_room_id
        self.loyalty_card_id=loyalty_card_id 
        self.request_support= request_support

    def __str__(self) -> str: # String representation of the customer
        return f"{self.customer_id}: {self.fitting_room_id} {self.loyalty_card_id} {self.request_support}"


class Employee: # Represents an Employee
    def __init__(self, employee_id: int, availability: str):
        self.employee_id = employee_id
        self.availability = availability
       

    def is_available(self) -> bool:
        # TODO: επιστρέψτε True αν υπάρχει διαθεσιμότητα  υπαλλήλου
        return self.availability

    #ίσως το χρειαστούμε
    def add_participant(self) -> None:
        # TODO: αυξήστε τον αριθμό συμμετεχόντων κατά 1
        self.current_participants += 1

    def __str__(self) -> str: # String representation of the class session
        return (f"{self.session_id}: {self.title} "
                f"({self.date} {self.time}) "
                f"[{self.current_participants}/{self.capacity}]")


#μπορεί να το χρειαστούμε
    def __str__(self) -> str:
        return (f"Booking {self.booking_id} - {self.member.name} "
                f"-> {self.session.title} ({self.session.date} {self.session.time})")
    
class ClothingItem: # Represents a garment
    def __init__(self, clothingitem_id:int, barcode: int, description: str, brand: str, photos: list, available_colours: str, price: float):
        self.clothingitem_id= clothingitem_id
        self.barcode = barcode
        self.description = description
        self.brand = brand 
        self.photos = photos
        self.available_colours = available_colours
        self.price = price

