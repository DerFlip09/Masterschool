import json
import matplotlib.pyplot as plot
import plotly.express as px
import pandas as pd


def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


SHIPS = load_data("ship-data_codio.json")["data"]


def initialize_CLI():
    """
    Creates the main Command Line Interface, and runs till the User type in "stop"
    """
    print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
    while True:
        command = input("").strip()
        if command == "stop":
            break
        if command.startswith("top_countries"):
            try:
                command, num_countries = command.split()
                int_num_countries = int(num_countries)
                print(COMMAND_LIST[command + " <num_countries>"](int_num_countries))
            except ValueError as e:
                print(f"{e}")
        else:
            try:
                print(COMMAND_LIST[command]())
            except KeyError:
                print(f"Unknown command {command}")


def get_command_list():
    """
    Returns a string of all commands in the dispatcher dictionary
    """
    return "Available commands: \n" + "\n".join(COMMAND_LIST.keys())


def get_countries():
    """
    Returns a string of all countries inside the given data
    """
    countries = []
    for ship in SHIPS:
        countries.append(ship["COUNTRY"])
    return "\n".join(sorted(set(countries)))


def count_by_key(key: str):
    """
    returns a list of tuples which are sorted by appearances of the key.
    tuples first item is the key and the second item its count
    """
    counted_values = {}
    for ship in SHIPS:
        if ship[key] not in counted_values:
            counted_values[ship[key]] = 1
        else:
            counted_values[ship[key]] += 1
    return sorted(counted_values.items(), key=lambda k: k[1], reverse=True)


def get_top_countries(num_countries: int):
    """
    returns a string of countries which appears the most inside the range of the given number
    """
    top_countries = count_by_key("COUNTRY")[:num_countries]
    converted_list_of_top_countries = []
    for country, appearance in top_countries:
        converted_list_of_top_countries.append(f"{country} {appearance}")
    return "\n".join(converted_list_of_top_countries)


def get_ships_type():
    """
    returns a string of ship types and the count of appearances
    """
    ships_and_types = count_by_key("TYPE_SUMMARY")
    converted_list_of_ships_and_types = []
    for ship_type, appearance in ships_and_types:
        converted_list_of_ships_and_types.append(f"{ship_type} {appearance}")
    return "\n".join(converted_list_of_ships_and_types)


def get_ships_with_name():
    """
    searches through the data and returns any ship which relates to the given substring
    """
    ship_name = input("Give me a name (or a part of it): ")
    list_of_ships_with_name = []
    for ship in SHIPS:
        if ship_name.lower() in ship["SHIPNAME"].lower():
            list_of_ships_with_name.append(ship["SHIPNAME"])
    return "\n".join(list_of_ships_with_name)


def create_histogram(list_of_ships: list, list_of_speeds: list):
    """
    returns the figure and the axis object of a histogram
    """
    figure, axes = plot.subplots(figsize=(100, 20))
    bars = axes.bar(list_of_ships, list_of_speeds, color="skyblue")
    for bar in bars:
        axes.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + .2,
            f"{bar.get_height()}",
            ha="center",
            color="black",
            rotation=60,
            fontsize=6
        )
    plot.xticks(range(len(list_of_ships)), list_of_ships, rotation=90, ha="center")
    axes.set_title("Speed of Ships")
    axes.set_xlabel("Shipnames")
    axes.set_ylabel("Speed")
    plot.tight_layout()
    return figure, axes


def make_speed_histogram_file():
    """
    Creates a file containing a histogram that shows the distribution of ships according to their speed
    and returns a confirmation string
    """
    speed_by_ship_names = {}
    for ship in SHIPS:
        speed_by_ship_names[ship["SHIPNAME"]] = float(ship["SPEED"])
    sorted_ships = sorted(speed_by_ship_names.items(), key=lambda item: item[1])
    list_of_ships = [ship[0] for ship in sorted_ships]
    list_of_speeds = [ship[1] for ship in sorted_ships]
    figure, axes = create_histogram(list_of_ships, list_of_speeds)
    plot.savefig("speed_histogram.jpg")
    return "file speed_histogram.jpg was successfully created"


def get_ship_data_for_map():
    """
    Returns a dictionary of necessary data to draw a map
    """
    ship_data = {"Shipname": [ship["SHIPNAME"] for ship in SHIPS],
                 "Country": [ship["COUNTRY"] for ship in SHIPS],
                 "Longitude": [ship["LON"] for ship in SHIPS],
                 "Latitude": [ship["LAT"] for ship in SHIPS]}
    return ship_data


def draw_a_map_of_positions():
    """
    draws a map and opens the map inside the browser
    """
    ship_data = get_ship_data_for_map()
    dataframe = pd.DataFrame(ship_data)
    map_plot = px.scatter_geo(dataframe,
                              lon="Longitude",
                              lat="Latitude",
                              hover_name="Shipname",
                              hover_data="Country",
                              title="Ship Locations")
    map_plot.show()
    return "Map was drawn"


COMMAND_LIST = {"help": get_command_list,
                "stop": None,
                "show_countries": get_countries,
                "top_countries <num_countries>": get_top_countries,
                "ships_by_type": get_ships_type,
                "search_ship": get_ships_with_name,
                "speed_histogram": make_speed_histogram_file,
                "draw_map": draw_a_map_of_positions}


def main():
    """
    the main function to start the command line interface
    """
    initialize_CLI()


if __name__ == "__main__":
    main()
