import json


class Hotel:
    def __init__(self, name, address, phone_number, email, r, filename="guest_details.json"):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.room = r
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Load room and student data from the file or initialize default."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # Default data if file is not found
            return {
                'rooms': {
                    'Deluxe': [10, 0],  # [Total, Occupied]
                    'Luxury': [4, 0],
                    'Basic': [7, 0]
                },
                'guests': []
            }

    def save_data(self):
        """Save the current data to the file."""
        with open(self.filename, "w") as file:
            json.dump(self.data, file)

    def display_guest_details(self):
        print("\n Guest Details:")
        for guest in self.data['guests']:
            print(f"Name: {guest['name']}, Address: {guest['address']}, "
                  f"Phone: {guest['phone_number']}, Email: {guest['email']}, Room: {guest['room']}")

    def room_availibility(self):
        print("\nAvailable Rooms:")
        for room_t, count in self.data['rooms'].items():
            print(f"{room_t}: {count[1]} occupied out of {count[0]} total.")

    def add_guest(self, name, address, phone_number, email, room_type, room_count):
        if room_type in self.data['rooms']:
            total, occupied = self.data['rooms'][room_type]
            if occupied + room_count <= total:
                self.data['rooms'][room_type][1] += room_count
                self.data['guests'].append({
                    'name': name,
                    'address': address,
                    'phone_number': phone_number,
                    'email': email,
                    'room': f"{room_type} ({room_count})"
                })
                self.save_data()
                print(f"Guest {name} successfully added and assigned {room_count} {room_type}(s).")
            else:
                print(f"Not enough {room_type}s available! Only {total - occupied} left.")
        else:
            print("Invalid room type.")

    def search_guest(self, guest_name):
        for guest in self.data['guests']:
            if guest['name'].lower() == guest_name.lower():
                print(f"\nGuest Found: Name: {guest['name']}, Address: {guest['address']}, "
                      f"Phone: {guest['phone_number']}, Email: {guest['email']}, Room: {guest['room']}")
                return
        print("Guest not found.")

    def cancel_booking(self, guest_name, room_count):
        for guest in self.data['guests']:
            if guest['name'].lower() == guest_name.lower():
                room_type = guest['room'].split()[0]
                room_count = int(guest['room'].split()[1].strip('()'))
                self.data['rooms'][room_type][1] -= room_count
                self.data['guests'].remove(guest)
                print(f"Guest {guest['name']} successfully cancelled and assigned {room_count} {room_type}(s).")
                self.save_data()
                return
        print("Guest not found.")



def main():
    Hote = Hotel(name='', address='', phone_number='', email='', r='', filename='guest_details.json')

    while True:
        print("\n ___@_Welcome to Karan Paradise_@___")
        print("1. Add Guest Details")
        print("2. Display All Bookings")
        print("3. Search Guest by Name")
        print("4. Display Room Availability")
        print("5. Exit")
        print("6. Cancel Booking")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter guest name: ")
            address = input("Enter guest address: ")
            phone_number = input("Enter guest phone number: ")
            email = input("Enter guest email: ")
            Hote.room_availibility()
            room_type = input("Enter room type (Deluxe/Luxury/Basic): ")
            room_count = int(input("Enter number of rooms to reserve: "))
            Hote.add_guest(name, address, phone_number, email, room_type, room_count)

        elif choice == "2":
            Hote.display_guest_details()

        elif choice == "3":
            guest_name = input("Enter guest name to search: ")
            Hote.search_guest(guest_name)

        elif choice == "4":
            Hote.room_availibility()

        elif choice == "6":
            guest_name = input("Enter guest name to cancel: ")
            room_count = int(input("Enter number of rooms to cancel: "))
            Hote.cancel_booking(guest_name, room_count)    

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()
