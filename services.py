from models import Customer, Employee, ClothingItem


class SupportSystem
    def __init__(self):
        self.customers: list[customer] = [] # List to store customers
        self.employees: list[Employee] = [] # List to store employees
        self.clothingitems: list[ClothingItem] = [] # List to store clothingitems

        self._next_customer_id = 1 # Internal counter for customer IDs
        self._next_employee_id = 1 # Internal counter for employee IDs
        self._next_clothingitem_id = 1 # Internal counter for clothingitem IDs

        self._seed_demo_data() 

    def _seed_demo_data(self) -> None:
        """Δημιουργεί 2-3 έτοιμους υπαλλήλους για τις δοκιμές."""
        self.add_employee("Maria", "6973703687")
        self.add_employee("Spyros", "6985367592")
        self.add_clothingitem("benetton", "5296347", "κόκκινο", "t-shirt","25", url="https://www.kathararoucha.gr/gynaikeio-aplo-mplouzaki/to-kokkino/2XL/?gad_source")
        self.add_clothingitem("adidas", "2579321", "μπλε", "φορμα", "50", url="https://www.aboutyou.gr/p/adidas-sportswear/panteloni-formas-essentials-26229905?vid")
        self.add_customer("GR-LOYAL-100234", "Maria","6973658923")
        self.add_customer("GR-LOYAL-100569", "Theoni", "6982456781")
 
    # ------- clothingitems ---------

    def add_clothingitem(self, barcode: int, description: str, brand: str, photos:list, available_colours: str, price:float ) -> ClassSession:
        clothingitem =clothingitem(self._next_clothingitem_id, barcode, description, brand, photos, available_colours, price)
        self.clothingitems.append(clothingitem) # Add clothingitems to the list
        self._next_clothingitem_id += 1 # Increment clothingitem ID for next clothingitem
        return clothingitem

    def list_clothingitems(self) -> list[clothingitem]:
        return self.clothingitems # Return the list of clothingitems

    def find_clothingitem_by_id(self, clothing_id: int) -> clothingitem | None:
        for s in self.clothingitems:
            if s.clothingitem_id == clothing_id: # Match found
                return s # Return the clothingitem
        return None # No match found

    # ------- customers with loyalty card ---------

    def find_or_create_customer(self, name: str, phone_number: int, loyalty_card:str) -> Customer:
        for m in self.customers:
            if m.loyalty_card == loyalty_card:
                return m
        customer = Customer(self._next_customer_id, name, phone_number, loyalty_card)
        self.customers.append(customer)
        self._next_customer_id += 1
        return customer

    # ------- employees ---------

    def employee_availability(self, employee_id: int) -> Employee | None:
        employee = self.find_employee_by_id(employee_id)
        if employee is None: # TODO: ελέγξτε αν  υπάρχει διαθέσιμος υπάλληλος
            print("Δεν βρέθηκε διαθέσιμος υπάλληλος με αυτο το id.") 
            return None 

        # TODO: ελέγξτε αν υπάρχει διαθέσιμος υπάλληλος
        if not employee.is_available(): # Check for available employees
            print("Δεν είναι διαθέσιμος.") # Print message if full
            return None

        # TODO: αυξήστε συμμετέχοντες και δημιουργήστε Booking αντικείμενο
        session.add_participant() # Increment participants
        booking = Booking(self._next_booking_id, member, session) # Create booking
        self.bookings.append(booking) # Add booking to the list
        self._next_booking_id += 1 # Increment booking ID
        return booking

    def bookings_for_member(self, member: Member) -> list[Booking]:
        # TODO: επιστρέψτε λίστα bookings για αυτό το μέλος
        return [b for b in self.bookings if b.member == member]