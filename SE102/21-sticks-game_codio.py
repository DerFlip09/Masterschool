START_MESSAGE = "{} Sticks in the pile\n"


def get_player_list() -> list:
    """
    Prompts for player names and returns them as a list.

    :returns: List of player names.
    """
    player1 = input("Enter name player1: ")
    player2 = input("Enter name player2: ")
    return [player1, player2]


def get_sticks(player: str) -> int:
    """
    Prompts the given player to take 1-3 sticks.

    :param player: The current player's name.
    :returns: The number of sticks taken by the player.
    """
    while True:
        sticks = int(input(f"{player} takes: "))
        if not 1 <= sticks <= 3:
            print("Please enter a number between 1-3!")
            continue
        return sticks


def bot_turn(sticks: int) -> int:
    """
    Determines the bot's move to leave a multiple of 4 sticks.

    :param sticks: Current number of sticks in the pile.
    :returns: Number of sticks taken by the bot.
    """
    for number in range(1, 4):
        if (sticks - number) % 4 == 0:
            print(f"Bot takes: {number}")
            return number


def print_status(player_on_turn: str, sticks: int) -> bool:
    """
    Prints the current status of the game.

    :param player_on_turn: The player who just took a turn.
    :param sticks: Remaining sticks in the pile.
    :returns: True if the game is over, otherwise False.
    """
    if sticks <= 0:
        print("0 sticks in the pile.\n")
        print(f"{player_on_turn} wins!")
        return True
    print(f"{sticks} sticks in the pile")
    return False


def pvp_game():
    """
    Runs a player vs. player game mode with 21 sticks.
    """
    players = get_player_list()
    sticks = 21
    print(START_MESSAGE.format(sticks))
    player_on_turn = ""
    while sticks > 0:
        for player in players:
            player_on_turn = player
            sticks -= get_sticks(player)
            status = print_status(player_on_turn, sticks)
            if status:
                break


def pve_game():
    """
    Runs a player vs. environment (bot) game mode with 21 sticks.
    """
    player = input("Enter player name: ")
    sticks = 21
    print(START_MESSAGE.format(sticks))
    while sticks > 0:
        # Bot's turn
        bot_sticks = bot_turn(sticks)
        sticks -= bot_sticks
        status = print_status("Bot", sticks)
        if status:
            break
        # Player's turn
        player_sticks = get_sticks(player)
        sticks -= player_sticks
        print_status(player, sticks)


def main():
    """
    Main game loop to select and start a game mode.
    """
    game_modes = {1: pvp_game, 2: pve_game, 3: None}
    while True:
        try:
            game_mode = int(input("1. PvP\n2. PvE\n3. Exit\nWhich game mode do you want to play (1, 2 or 3)? "))
        except ValueError:
            print("Please enter 1, 2 or 3!")
        if game_mode == 3:
            print("Good Bye!")
            break
        if game_mode in game_modes.keys():
            game_modes[game_mode]()
            break


if __name__ == "__main__":
    main()
