# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Error, invalid arguments")
    teams = []
    # TODO: Read teams into memory from file
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for team_dic in reader:
            # it needs to get the full dictionary not the last one
            team_dic["rating"] = int(team_dic["rating"])
            teams.append(team_dic)
    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    for i in range(0, N):
        team_name = simulate_tournament(teams)
        if team_name in counts:
            counts[team_name] = counts[team_name] + 1
        else:
            counts[team_name] = 0
            counts[team_name] = counts[team_name] + 1
    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability
    # this function return true or false
    # true if team1 win
    # false if team2 win
    # like it make a match betwin them


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners
    # this functiion is like 16 round until the final
    # this function return list of teams that won the round if there are 16
    # function return 8 of the winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    next_round = []
    next_round = simulate_round(teams)
    if len(next_round) != 1:
        name = simulate_tournament(next_round)
    else:
        # getting access to a dictionary inside a list
        return next_round[0]["team"]
    return name


if __name__ == "__main__":
    main()
# thamx man it was great time with you i had fun