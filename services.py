from models import Customer, Employee, ClothingItem, FittingRoom, NotificationMessage, CustomerHelpService


class CustomerSupportSystem:
    def __init__(self):
        self.customers: list[Customer] = [] # List to store customers
        self.employees: list[Employee] = [] # List to store employees
        self.clothingitems: list[ClothingItem] = [] # List to store clothingitems
        self.fittingrooms: list[FittingRoom] = [] # List to store fittingrooms
        self.notificationmessages: list[NotificationMessage]=[] # List to store notificationmessages
        self.customerhelpservices: list[CustomerHelpService]=[] # List to store customerhelpservice

        self._next_customer_id = 1 # Internal counter for customer IDs
        self._next_employee_id = 1 # Internal counter for employee IDs
        self._next_clothingitem_id = 1 # Internal counter for clothingitem IDs
        self._next_fitting_room_id= 1 # Internal counter for fitting room IDs
        self._next_notification_message_id= 1 # Internal counter for notification message IDs
        self._next_customer_help_service_id= 1 # Internal counter for customer help service IDs

        self._seed_demo_data() 

    def _seed_demo_data(self) -> None:
        #Δημιουργεί 2 έτοιμους υπαλλήλους, ρούχα, πελάτες για τις δοκιμές.
        self.add_employee("Maria", "6973703687", False)
        self.add_employee("Spyros", "6985367592", True)
        self.add_clothingitem("5296347", "t-shirt", "benetton", "red","25")
        self.add_clothingitem("2579321", "tracksuit", "adidas", "blue", "50")
        self.add_customer("GR-LOYAL-100234", "Maria","6973658923")
        self.add_customer("GR-LOYAL-100569", "Theoni", "6982456781")
        self.add_fittingroom(1)
        self.add_fittingroom(2)
        self.add_notificationmessage(1, "yes")
        self.add_notificationmessage(2, "no")

        
    # ------- clothingitems ---------

    def add_clothingitem(self, barcode: int, description: str, brand: str, available_colours: str, price:float ) -> ClothingItem:
        clothingitem =ClothingItem(self._next_clothingitem_id, barcode, description, brand, available_colours, price)
        self.clothingitems.append(clothingitem) # Add clothingitems to the list
        self._next_clothingitem_id += 1 # Increment clothingitem ID for next clothingitem
        return clothingitem

    def list_clothingitems(self) -> list[ClothingItem]:
        return self.clothingitems # Return the list of clothingitems

    def find_clothingitem_by_barcode(self, barcode: int) -> ClothingItem | None:
        for s in self.clothingitems:
            if s.barcode == barcode: # Match found
                return s # Return the clothingitem
        return None # No match found

    # ------- customers with loyalty card ---------

    def add_customer(self, name: str, phone_number: int, loyalty_card_id: str) -> Customer:
        customer = Customer (self._next_customer_id, name, phone_number, loyalty_card_id)
        self.customers.append(customer) # Add customer to the list
        self._next_customer_id +=1 # Increment customer ID for next customer
        return customer

    def find_or_create_customer(self, name: str, phone_number: int, loyalty_card_id:str) -> Customer:
        for m in self.customers:
            if m.loyalty_card_id == loyalty_card_id:
                return m
        new_customer = Customer(self._next_customer_id, name, phone_number, loyalty_card_id)
        self.customers.append(new_customer)
        self._next_customer_id += 1
        return new_customer

    # ------- employees ---------

    def add_employee(self, name: str, phone_number: int, availability: bool) -> Employee:
        employee = Employee (self._next_employee_id, availability, name, phone_number)
        self.employees.append(employee) # Add employee to the list
        self._next_employee_id += 1 # Increment employee ID for next employee
        return employee

    def find_and_assign_employee(self) -> int:
        for employee in self.employees:
            # Έλεγχος αν ο υπάλληλος είναι διαθέσιμος
            if employee.is_available():
                # 1. Στέλνουμε το SMS στον υπάλληλο
                print(f"Στάλθηκε SMS στον υπάλληλο με ID: {employee.get_id()}")
                
                # 2. Αλλάζουμε τη διαθεσιμότητα σε False (δεν είναι πλέον διαθέσιμος ο υπάλληλος)
                employee.availability = False
                
                # 3. Επιστρέφουμε το ID του πρώτου διαθέσιμου υπαλλήλου 
                return employee.get_id()
         
    # Αν η λούπα τελειώσει και δεν βρεθεί διαθέσιμος υπάλληλος
        print("Δεν βρέθηκε διαθέσιμος υπάλληλος.")
        return None 
    
    def add_fittingroom(self, fittingroom: int) -> FittingRoom:
        fittingroom = FittingRoom (self._next_fitting_room_id)
        self.fittingrooms.append(fittingroom) # Add fitting room  to the list fittingroom
        self._next_fitting_room_id += 1 # Increment fitting room ID for next fittingroom
        return fittingroom     

    def add_notificationmessage(self, notificationmessage: int, sms:str) -> NotificationMessage:
        notificationmessage = NotificationMessage (self._next_notification_message_id, sms)
        self.notificationmessages.append(notificationmessage) # Add notification message to the list notificationmessage
        self._next_notification_message_id += 1 # Increment notification message ID for next notification message
        return notificationmessage      
    
    def customerhelpservice(self, customer: Customer, clothingitem: ClothingItem, fittingroom: FittingRoom) -> CustomerHelpService:     

         # 1. Βρίσκουμε διαθέσιμο υπάλληλο
         available_emp = None 
         for employee in self.employees:
            if employee.is_available ():
                available_emp = employee
                break

         if available_emp is None:
            print("Δεν βρέθηκε διαθέσιμη βοήθεια.")
            return None #ΕΔΩ σταματάει σωστά αν όλοι είναι False
        
        #2 Βρίσκουμε το δοκιμαστήριο
         fittingroom = None
         for r in self.fittingrooms:
            if r.fitting_room_id:
                fittingroom= r
                break # Μόλις το βρούμε, σταματάμε το ψάξιμο

        # Δημιουργούμε την υπηρεσία βοήθειας
         customerhelpservice= CustomerHelpService(self._next_customer_help_service_id, customer, employee, clothingitem, fittingroom)
         self.customerhelpservices.append(customerhelpservice) # Add customer help service to the list 
         self._next_customer_help_service_id += 1 # Increment customer help service ID for next customer help service

        # O Υπάλληλος ολοκλήρωσε την βοήθεια και το πρόγραμμα κλείνει
         available_emp.availability = False
         print(f"Στάλθηκε SMS στον υπάλληλο {available_emp.name} (ID: {available_emp.employee_id})")
         print("Help Succeeded!")
         return customerhelpservice
    