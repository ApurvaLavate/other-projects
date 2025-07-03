import random

score = {"wins": 0, "losses": 0, "ties": 0}

def get_computer_move():
    return random.choice(['rock', 'paper', 'scissors'])

def get_result(player, computer):
    if player == computer:
        return 'Tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return 'You win'
    else:
        return 'You lose'

def play_game():
    while True:
        player_move = input("Enter your move (rock/paper/scissors) or 'quit': ").lower()
        if player_move == 'quit':
            break
        if player_move not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Try again.")
            continue

        computer_move = get_computer_move()
        print(f"Computer chose: {computer_move}")

        result = get_result(player_move, computer_move)
        print(result)

        if result == 'You win':
            score['wins'] += 1
        elif result == 'You lose':
            score['losses'] += 1
        else:
            score['ties'] += 1

        print("Score:", score)

play_game()
