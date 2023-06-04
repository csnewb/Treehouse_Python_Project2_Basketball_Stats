import random
import constants


def import_players():
    PLAYERS = []
    for ea in constants.PLAYERS:
        PLAYERS.append(ea)
    return PLAYERS


def import_teams():
    TEAMS = []
    for ea in constants.TEAMS:
        TEAMS.append(ea)
    return TEAMS


def clean_player_data(PLAYERS):
    clean_players = []
    for ea in PLAYERS:

        name = ea["name"]
        guardians = ea["guardians"]
        experience = ea["experience"]
        height = ea["height"]

        clean_height = height.split(" ")[0]
        try:
            clean_height = int(clean_height)
        except:
            print(f"Exception: Unable to convert player {ea['name']} height to integer")

        if experience.lower() == "yes":
            experience_bool = True
        elif experience.lower() == "no":
            experience_bool = False
        else:
            print(f"invalid player experience for {ea['name']} defaulting to False")
            experience_bool = False

        clean_guardians = guardians.split("and")
        clean_guardians = [ea.lstrip() for ea in clean_guardians]

        clean_stats = {
            'name': name,
            'guardians': clean_guardians,
            'experience': experience_bool,
            'height': clean_height,
        }

        clean_players.append(clean_stats)

    return clean_players


def balance_teams(clean_players, teams, show_work=False):
    all_assigned_teams = []

    shuffled_list = clean_players.copy()
    random.shuffle(shuffled_list)
    experienced_players = [ea for ea in shuffled_list if ea["experience"] == True]
    inexperienced_players = [ea for ea in shuffled_list if ea["experience"] == False]
    if show_work:
        print("\n"* 3)
        print("Evaluating Player Experience Levels")
        print(f"\n---- Experienced Players ----")
        for ea in experienced_players:
            print(f"    {ea['name']}")
        print(f"\n---- Inexperienced Players ----")
        for ea in inexperienced_players:
            print(f"    {ea['name']}")
        print(f"\nRe-Assigning Players to Teams")

    all_assigned_teams = evenly_split_players(experienced_players, teams, all_assigned_teams, show_work)
    all_assigned_teams = evenly_split_players(inexperienced_players, teams, all_assigned_teams, show_work)

    print(f"\nTeam Re-Assignment Complete")
    return all_assigned_teams


def evenly_split_players(player_list, teams, all_assigned_teams, show_work):
    assignable_players, unassignable_players = get_assignable_players(player_list, teams)


    while assignable_players:
        for team in teams:
            active_player = assignable_players.pop(0)
            if show_work:
                print(f"    assigning {active_player['name']} to {team}")
            active_player["team"] = team
            all_assigned_teams.append(active_player)

    while unassignable_players:
        active_player = unassignable_players.pop(0)
        if show_work:
            print(f"    assigning {active_player['name']} to unassigned")
        active_player["team"] = "Unassigned"
        all_assigned_teams.append(active_player)

    return all_assigned_teams

def get_assignable_players(player_list, teams):
    num_players = len(player_list)
    num_teams = len(teams)
    players_per_team = num_players // num_teams
    num_assignable_players = players_per_team * num_teams
    assignable_players = player_list[:num_assignable_players]
    unassigned_players = player_list[num_assignable_players:]

    return assignable_players, unassigned_players


def force_int(prompt, min_int, max_int):
    while True:
        try:
            choice = int(input(prompt))
            if choice <= max_int:
                break
        except:
            print(f"ERROR: Please choice an integer between {min_int} and {max_int}")
    return choice



