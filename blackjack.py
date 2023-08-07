import random
from replit import clear

def logo():
    """Printing logo blackjack"""
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

def play_blackjack():
    """Ask if user wants play"""
    value_play_black_jack = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if value_play_black_jack == 'y':
        return True
    else:
        return False

def draw_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_card = random.choice(cards)
    return drawn_card

def calculate_player_score(player_cards):
    """Take a list of cards and return the score calculated from the cards"""
    player_score = 0

    for num in player_cards:
        player_score += num

    if 11 in player_cards and player_score > 21:
        card_eleven_index = users_cards.index(11) 
        users_cards[card_eleven_index] = 1
        player_score -= 10

    return player_score

def start_game():
    """Returns starting cards for user and computer"""
    users_cards = []
    computers_cards = []
    for i in range(2):
        users_cards.append(draw_card())
    for i in range(2):
        computers_cards.append(draw_card())
    return users_cards, computers_cards
    
def another_card():
    """Ask user for another card"""
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
        return True
    else:
        return False

def is_blackjack(users_score, users_cards, computers_score, computers_cards):
    """Check if player has blackjack"""
    if users_score == 21 and 11 in users_cards and 10 in users_cards:
        print("User has blackjack")
        return True
    elif computers_score == 21 and 11 in computers_cards and 10 in computers_cards:
        print("Computer has blackjack")
        return True
    else:
        return False
    
def print_score(users_score, users_cards, computers_score, computers_cards)
    """Printing cards and scores"""
    print(f"Your final hand: {users_cards} final score: {users_score}\nComputer's final hand: {computers_cards}, final score: {computers_score}")

def compare(users_score, users_cards, computers_score, computers_cards):
    #Bug fix. If you and the computer are both over, you lose.
    if users_score > 21 and computers_score > 21:
        print("You went over. You lose 😤")

        
    if users_score > computers_score:
        print_score(users_score, users_cards, computers_score, computers_cards)
        print("You WIN")
    elif users_score < computers_score:
        print_score(users_score, users_cards, computers_score, computers_cards)
        print("You LOSE")
    else:
        print_score(users_score, users_cards, computers_score, computers_cards)
        print("DRAW")

def engine():
    users_score = calculate_player_score(users_cards)
    computers_score = calculate_player_score(computers_cards)
    print(f"Your cards: {users_cards}, current score: {users_score}\nComputer's first card: {computers_cards[0]}")

    if is_blackjack(users_score, users_cards, computers_score, computers_cards):
        if users_score == 21:
            print_score(users_score, users_cards, computers_score, computers_cards)
            print("You WIN")
            return True
        else:
            print_score(users_score, users_cards, computers_score, computers_cards)
            print("You LOSE")
            return True
    else:
        if users_score > 21:
            print_score(users_score, users_cards, computers_score, computers_cards)
            print("You LOSE")
            return True
        else:
            if another_card():
                users_cards.append(draw_card())
                return False
            else:
                while computers_score < 17:
                    computers_cards.append(draw_card())
                    computers_score = calculate_player_score(computers_cards)
               
                compare(users_score, users_cards, computers_score, computers_cards)
                return True

if __name__ == "__main__":
    while play_blackjack() == True:
        clear()
        logo()
        users_cards, computers_cards = start_game()

        game_finished = False
        while not game_finished:
            game_finished = engine()
