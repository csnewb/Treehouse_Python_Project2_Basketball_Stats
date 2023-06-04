import utilities


def main_menu(players, teams, assigned_teams):
    print("\n" * 3)
    print("What would you like to do?")
    menu_options = (
        "1 - Re-Assign Players to Teams",
        "2 - See All Players",
        "3 - See Teams",
        "4 - See Players Assigned to Teams",
        "5 - See Team Stats",
        "6 - Quit",)
    for ea in menu_options:
        print(f"    {ea}")

    choice = utilities.force_int("Choice:  ", 1, len(menu_options))
    if choice == 1:
        new_assigned_teams = reassign_teams(players, teams, show_work=True)
        main_menu(players, teams, new_assigned_teams)
    elif choice == 2:
        show_all_players(players)
    elif choice == 3:
        show_all_teams(teams)
    elif choice == 4:
        view_team_assignments(assigned_teams, teams)
    elif choice == 5:
        view_team_stats(assigned_teams, teams)
    else:
        quit()


def reassign_teams(players, teams, show_work=False):
    new_assigned_teams = utilities.balance_teams(players, teams, show_work)
    return new_assigned_teams


def show_all_players(players):
    print("\n" * 3)
    print("-"*35)
    print("---- ALL PLAYERS ----")
    for ea in players:
        for key, value in ea.items():
            print(f"{key}: {value}")
        print("\n")
    print("\n"*5)
    return


def show_all_teams(teams):
    print("\n" * 3)
    print("-" * 35)
    print("---- ALL TEAMS ----")
    for ea in teams:
        print(ea)
    print("\n" * 5)
    return


def view_team_assignments(assigned_teams, teams):
    print("\n" * 3)
    print("--- Viewing Team Assignments ---")
    print("What team you like to view assignments for?")
    for index, team in enumerate(teams):
        print(f"    {index + 1} - {team}")
    prompt = f"Choice (0 to cancel): "
    choice = utilities.force_int(prompt, 0, len(teams))

    if choice != 0:
        chosen_team = teams[choice - 1]
        print("\n" * 3)
        print(f"--- Showing players on team: {chosen_team} ---\n")
        for player in assigned_teams:
            if player["team"] == chosen_team:
                for key, value in player.items():
                    print(f"{key}: {value}")
                print("\n")
        print("\n" * 5)

    return


def view_team_stats(assigned_teams, teams):
    print("\n" * 3)
    print("--- Viewing Team Stats ---")
    print("What team you like to view stats for?")
    for index, team in enumerate(teams):
        print(f"    {index + 1} - {team}")
    prompt = f"Choice (0 to cancel): "
    choice = utilities.force_int(prompt, 0, len(teams))

    if choice != 0:
        team_roster = []
        chosen_team = teams[choice - 1]
        for player in assigned_teams:
            if player["team"] == chosen_team:
                team_roster.append(player)

        ##### Team Stats ####
        # Exceptional Requirements
        # Team's name
        # Total number of players on that team
        # The player names of that team (joined together as a comma-separated string not displayed as a List object.)
        # Total number of inexperienced players
        # Total number of experienced players
        # Average height of the team
        # The guardian names of all the players on the team (joined together as a comma-separated string not displayed as a List object).

        chosen_team = teams[choice - 1]
        num_players = len(assigned_teams)
        num_experienced = 0
        num_inexperienced = 0

        name_list = []
        height_list = []
        guardian_list = []
        for player in team_roster:
            name_list.append(player["name"])
            try:
                height_list.append(int(player["height"]))
            except:
                print(f"Exception: Unable to convert player {player['name']} height to int, removing from calculations")

            if player["experience"] == True:
                num_experienced += 1
            else:
                num_inexperienced += 1
            for ea in player["guardians"]:
                guardian_list.append(ea)

        player_names = ', '.join(name_list)
        guardian_names = ', '.join(guardian_list)
        avg_height = round(sum(height_list) / len(height_list), 1)
        avg_height_ft = int(avg_height // 12)
        avg_height_in = int(avg_height % 12)

        print("\n" * 3)
        print(f"--- Showing stats for team: {chosen_team} ---\n")
        print(f"Number of Players: {num_players}")
        print(f"Experienced: {num_experienced}  |  Inexperienced: {num_inexperienced}")
        print(f"Avg Player Height: {avg_height} inches ({avg_height_ft} feet, {avg_height_in} inches)")
        print(f"Players: {player_names}")
        print(f"Guardians: {guardian_names}")
        print("\n" * 5)
    else:
        return

    # recursively call View Team Stats to allow selecting other team
    view_team_stats(assigned_teams, teams)

    return

