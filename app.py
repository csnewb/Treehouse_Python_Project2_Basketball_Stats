import menu
import settings
import utilities


def main_loop():
    TEAMS = utilities.import_teams()
    PLAYERS = utilities.import_players()
    clean_players = utilities.clean_player_data(PLAYERS)
    assigned_teams = menu.reassign_teams(clean_players, TEAMS, show_work=False)
    print(settings.greeting)
    while True:
        menu.main_menu(clean_players, TEAMS, assigned_teams)


if __name__ == "__main__":
    main_loop()
