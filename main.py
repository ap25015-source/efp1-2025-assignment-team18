# main.py

from services import CustomerSupportSystem

def main():
    system = CustomerSupportSystem()
    print("Καλωσήρθατε στο σύστημα Yποστήριξης του Εξυπνου Δοκιμαστηρίου")

    barcode = input("barcode ρούχου: ")
    fitting_room_id = input("ID Δοκιμαστηρίου (1 ή 2):")
    loyalty_card_id= input("ID loyalty card (αν δεν έχετε, πατήστε Enter):")
    name = input("Όνομα πελάτη")
    phone = input("Τηλέφωνο Πελάτη")
    
    customer = system.find_or_create_customer(name, phone, loyalty_card_id)
    clothingitem = system.find_clothingitem_by_barcode (barcode)

    while True:
        print("\n--- Μενού ---")
        print("1. Παροχή Πληροφοριών Ρούχου")
        print("2. Υποστήριξη")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")

        if choice == "1":
            if clothingitem:
                print(f"Πληροφορίες: {clothingitem}")
            else:
                print("Το ρούχο με αυτό το barcode δεν βρέθηκε.")

        elif choice == "2":
            system.customerhelpservice (customer= customer, clothingitem= clothingitem, fittingroom= fitting_room_id)
            
        elif choice == "0":
            print("Έξοδος από το σύστημα. Αντίο!")
            break

        else:
            print("Μη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()