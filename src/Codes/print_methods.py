# Function to display the transient table
from prettytable import PrettyTable


def show_transient_table(transients):
    """Display a table of transients.

    Args:
        transients (list): A list of transient dictionaries containing their details.

    Returns:
        None
    """
    main_table = PrettyTable()
    main_table.field_names = ["ID", "Name", "Address", "Price/Head", "Contact"]

    for transient in transients:
        main_table.add_row(
            [transient["id"], transient["name"], transient["location"],
             f"₱{transient['price_per_head']}", transient["contact"]])

    print(main_table)


def show_reservation_details(client_name, date_from, date_to, pay_method, number_of_people, num_nights, price_per_head, total_cost):
    """Display the details of a reservation.

    Args:
        client_name (str): The name of the client making the reservation.
        date_from (str): The start date of the reservation.
        date_to (str): The end date of the reservation.
        pay_method (str): The payment method used for the reservation.
        number_of_people (int): The number of people for the reservation.
        num_nights (int): The number of nights for the stay.
        price_per_head (float): The cost per person per night.
        total_cost (float): The total cost of the reservation.

    Returns:
        None
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
