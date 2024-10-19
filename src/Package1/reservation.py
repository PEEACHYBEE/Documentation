import re
import print_methods

from prettytable import PrettyTable
from datetime import datetime, timedelta


file_path = 'transient_list.json'

def show_available_dates(transient):
    """

    @param transient:
    @return:
    """
    print(f"Name: {transient['name']}")
    print(f"Description: {transient['description']}")
    print(f"Please check available dates for {transient['name']}:")
    print()

    available_dates = [] # List holding available dates
    available_dates_table = PrettyTable()
    available_dates_table.field_names = ["ID", "Dates", "Status"]

    index = 0

    for date, details in transient['availability'].items():
        status = details['status'].upper()
        # Remove dates with "RESERVED" status
        if status != "RESERVED":
            index += 1
            available_dates_table.add_row([index, date, status])
            available_dates.append(date)

    # Notify user if there are no available dates in a transient
    if len(available_dates) == 0:
        print("This transient has no available dates.")
        return None

    print(available_dates_table)
    return set(available_dates)

def reserve_dates(transient, available_dates, transients):
    """

    @param transient:
    @param available_dates:
    @param transients:
    @return:
    """
    available_dates_list = list(available_dates)
    available_dates_list.sort()
    while True:
        ans_input = input("Would you like to reserve? (y/n) ").strip().lower()
        if ans_input in ["y", "yes"]:
            try:
                print()
                print("Reservation Form")

                client_name = input_name()

                date_from = available_dates_list[enter_choice(1, len(available_dates_list), "Enter ID to select reservation start date: ") - 1]
                date_to = available_dates_list[enter_choice(1, len(available_dates_list), "Enter ID to select reservation end date: ") - 1]

                number_of_people = input_number_of_people()

                # Validate date format
                try:
                    start_date = datetime.strptime(date_from, '%Y-%m-%d')
                    end_date = datetime.strptime(date_to, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue

                # Validate date range
                if start_date > end_date:
                    print("Error: Start date must be before or equal to end date.")
                    continue

                # Check if all dates in the range are available
                all_dates_available = True
                current_date = start_date
                while current_date <= end_date:
                    if current_date.strftime('%Y-%m-%d') not in available_dates:
                        all_dates_available = False
                        break
                    current_date += timedelta(days=1)

                if not all_dates_available:
                    print("Error: Some dates in the selected range are not available.")
                    continue

                # Calculate the number of nights client will stay
                num_nights = (end_date - start_date).days + 1

                pay_method = input_pay_method()

                price_per_head = transient["price_per_head"]
                total_cost = number_of_people * price_per_head * num_nights

                # Confirm reservation
                print_methods.show_reservation_details(client_name, date_from, date_to, pay_method, number_of_people, num_nights, price_per_head, total_cost)

                confirm = input_confirm()
                if confirm == "n":
                    continue

                # Update verified details on JSON
                current_date = start_date
                while current_date <= end_date:
                    date_key = current_date.strftime('%Y-%m-%d')
                    transient['availability'][date_key]['status'] = "RESERVED"
                    transient['availability'][date_key]['client_name'] = client_name
                    transient['availability'][date_key]['date_from'] = date_from
                    transient['availability'][date_key]['date_to'] = date_to
                    transient['availability'][date_key]['number_of_people'] = number_of_people
                    current_date += timedelta(days=1)

                # Save the updated data back to the JSON file
                from main import file_reader
                file_reader.save_json(transients,file_path)

                print()
                print("Reservation confirmed and saved.")
                print(f"Dear Mr./Ms. {client_name}, please proceed to {transient['location']} on {date_from} and enjoy your stay until {date_to}.")
                print("Thank you for trusting The Cozy Cabin.")
                break

            except ValueError:
                print("Invalid input. Please enter the number of people as an integer.")

        elif ans_input in ["n", "no"]:
            print()
            print("Returning to main menu.")
            return 0
        else:
            print("Invalid input. Please enter yes/no or y/n.")

def input_pay_method():
    """

    @return:
    """
    while True:
        print("\nAvailable Payment Methods")
        print("1. GCASH")
        print("2. PayMaya")
        pay_method = input("Select a payment method: ")
        if pay_method == "1":
            return "GCASH"
        elif pay_method == "2":
            return "PayMaya"
        else:
            print("\nInvalid! Please select one of the options.")

def input_name():
    """

    @return:
    """
    while True:
        client_name = input("Enter client name: ").strip()
        # Client name must not contain any integer
        if not re.match("^[A-Za-z\\s\\-]+$", client_name):
            print("Invalid name! Client name should not contain numbers or special characters. Please try again.")
        else:
            return client_name

def input_confirm():
    """

    @return:
    """
    while True:
        # Confirmation
        ans_input = input("Would you like to proceed? (y/n): ").strip().lower()
        if ans_input in ["y", "yes"]:
            return "y"
        elif ans_input in ["n", "no"]:
            return "n"
        else:
            print("Invalid input. Please enter yes/no or y/n.")

def input_number_of_people():
    """

    @return:
    """
    while True:
        number_of_people = (input("Enter number of people: ").strip())
        # Validates if input is integer
        if number_of_people.isdigit():
            number_of_people = int(number_of_people)
            if number_of_people > 0:
                return number_of_people
            else:
                print("Number of people must be greater than 0. Please try again.")
        else:
            print("Please enter a valid integer for number of people. Please try again.")

def enter_choice(min_num, max_num, message):
    """

    @param min_num:
    @param max_num:
    @param message:
    @return:
    """
    while True:
        try:
            choice = int(input(message))
            if choice < min_num or choice > max_num:
                print("Invalid Input. Please enter a number from ",min_num, "to", max_num)
            else:
                return choice
        except ValueError:
            print("Invalid Input. Please enter a valid number.")
