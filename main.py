# main.py

from services import SupportSystem


def main():
    system = SupportSystem()
    print("Καλωσήρθατε στο σύστημα Yποστήριξης του Εξυπνου Δοκιμαστηρίου")

    name = input("Όνομα πελάτη: ")
    fitting_room_id = input("ID Δοκιμαστηρίου:")

    customer = system.find_or_create_customer(name, fitting_room_id=)

    while True:
        print("\n--- Μενού ---")
        print("1. Προβολή διαθέσιμων μαθημάτων")
        print("2. Κράτηση μαθήματος")
        print("3. Προβολή κρατήσεων μου")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")

        if choice == "1":
            sessions = system.list_sessions()
            for s in sessions:
                print(s)

        elif choice == "2":
            sessions = system.list_sessions()
            for s in sessions:
                print(s)
            try:
                session_id = int(input("Δώσε id μαθήματος για κράτηση: "))
            except ValueError:
                print("Μη έγκυρο id.")
                continue

            booking = system.book_session(member, session_id)
            if booking:
                print("Η κράτηση ολοκληρώθηκε:")
                print(booking)

        elif choice == "3":
            bookings = system.bookings_for_member(member)
            if not bookings:
                print("Δεν έχετε κρατήσεις.")
            else:
                for b in bookings:
                    print(b)

        elif choice == "0":
            print("Έξοδος από το σύστημα. Αντίο!")
            break

        else:
            print("Μη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()