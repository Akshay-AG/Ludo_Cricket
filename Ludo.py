# Calculate the winning probability after each dice roll
import random

def roll_dice():
    return random.randint(1, 6)
    #return 6

def simulate_ludo_match(num_simulations=10000):
    # Initialize counters for different outcomes
    player_wins = [0] * 4
    draw = 0

    for _ in range(num_simulations):
        winner = simulate_single_match()

        # Update outcome counters
        if winner != -1:
            player_wins[winner] += 1
        else:
            draw += 1

    # Calculate probabilities
    total_matches = sum(player_wins) + draw
    player_win_probabilities = [wins / total_matches for wins in player_wins]
    draw_probability = draw / total_matches

    return player_win_probabilities, draw_probability

def simulate_single_match():
    # Simulate a single match of Ludo
    player_positions = [0] * 4

    while True:
        for player in range(4):
            roll = roll_dice()
            if player_positions[player] == 0 and roll != 6:
                continue  # Player must roll a 6 to move out of the starting area

            player_positions[player] += roll
            player_positions[player] = adjust_position(player, player_positions[player])

            if player_positions[player] >= 100:
                return player  # Player wins if they reach or pass the finish line

def adjust_position(player, position):
    return position  

# Simulate Ludo match and print probabilities
player_win_probabilities, draw_probability = simulate_ludo_match()
for player, probability in enumerate(player_win_probabilities):
    print(f"Player {player + 1} win probability:", probability)
print("Draw probability:", draw_probability)
