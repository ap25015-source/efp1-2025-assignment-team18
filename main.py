# main.py

from services import CustomerSupportSystem


def main():
    system = CustomerSupportSystem()
    print("Καλωσήρθατε στο σύστημα Yποστήριξης του Εξυπνου Δοκιμαστηρίου")

    barcode = input("barcode: ")
    fitting_room_id = input("ID Δοκιμαστηρίου:")
    loyalty_card_id= input("ID loyalty card:")

    CustomerSupportSystem = system.find_or_get_help(fitting_room_id, barcode, loyalty_card_id)

    while True:
        print("\n--- Μενού ---")
        print("1. Παροχή Πληροφοριών Ρούχου")
        print("2. Υποστήριξη")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")

        if choice == "1":
            barcode = system.clothingitem_by_id()
            for s in barcode:
                print(s)

        elif choice == "2":
            fitting_room_id = system.customerhelpservice()
            for s in fitting_room_id:
                print(s)
            
        elif choice == "0":
            print("Έξοδος από το σύστημα. Αντίο!")
            break

        else:
            print("Μη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()