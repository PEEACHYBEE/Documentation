# Function to display the transient table
from prettytable import PrettyTable


def show_transient_table(transients):
    """

    @param transients:
    @return:
    """
    main_table = PrettyTable()
    main_table.field_names = ["ID", "Name", "Address", "Price/Head", "Contact"]

    for transient in transients:
        main_table.add_row(
            [transient["id"], transient["name"], transient["location"],
             f"₱{transient['price_per_head']}", transient["contact"]])

    print(main_table)

def show_reservation_details(client_name, date_from, date_to, pay_method, number_of_people, num_nights, price_per_head, total_cost):
    """

    @param client_name:
    @param date_from:
    @param date_to:
    @param pay_method:
    @param number_of_people:
    @param num_nights:
    @param price_per_head:
    @param total_cost:
    @return:
    """
    print()
    print("Reservation Details")
    print(f"Client Name: {client_name}")
    print(f"Reservation From: {date_from}")
    print(f"Reservation To: {date_to}")
    print(f"Payment method: {pay_method}")
    print(f"Number of People: {number_of_people}")
    print(
        f"Calculating cost for {number_of_people} people staying {num_nights} night/s at ₱{price_per_head} per person...")
    print("Total cost: ₱", total_cost, sep="")