import os
import json
import print_methods
from menu import Menu

file_path = 'transient_list.json'

class file_reader:
    @staticmethod
    def load_json(file_path):
        """Load a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            list: The data loaded from the JSON file, or an empty list if an error occurred.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not a valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file '{file_path}' is not a valid JSON.")
        return []

    @staticmethod
    def save_json(transients, file_path):
        """Save data to a JSON file.

        Args:
            transients (list): The data to save.
            file_path (str): The path to the JSON file.

        Returns:
            None

        Raises:
            Exception: If there is an error saving the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(transients, file, indent=4)
            print(f"Data successfully saved to '{file_path}'")
        except Exception as e:
            print(f"Error saving to '{file_path}': {e}")


class Main:
    def __init__(self, file_path):
        """Initialize the Main class.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            None
        """
        self.file_path = file_path
        self.transients = file_reader.load_json(self.file_path)

    def run(self):
        """Run the main application logic.

        Returns:
            None
        """
        try:
            terminal_width = os.get_terminal_size().columns
        except OSError:
            terminal_width = 110

        # Print title
        print("The Cozy Cabin".center(terminal_width))
        print("Where Every Stay Feels Like Home".center(terminal_width))

        # Show the table
        print_methods.show_transient_table(self.transients)

        menu = Menu(self.transients)
        menu.display_menu()

        self.save_data()

    def save_data(self):
        """Save the current state of transients to a JSON file.

        Returns:
            None
        """
        file_reader.save_json(self.transients, self.file_path)

if __name__ == "__main__":
    app = Main(file_path)
    app.run()
