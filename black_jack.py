import random

def play_blackjack():
    value_play_black_jack = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if value_play_black_jack == 'y':
        return True
    else:
        return False

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_card = random.choice(cards)
    return drawn_card

def calculate_player_score(player_cards):
    player_score = 0

    for num in player_cards:
        player_score += num
    return player_score


def start_game():
    users_cards = []
    computers_cards = []
    for i in range(2):
        users_cards.append(draw_card())
    for i in range(2):
        computers_cards.append(draw_card())
    return users_cards, computers_cards
    
def another_card():
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
        return True
    else:
        return False

def is_blackjack(users_score, users_cards, computers_score, computers_cards):
    if users_score == 21 and 11 in users_cards and 10 in users_cards:
        print("User has blackjack")
        return True
    elif computers_score == 21 and 11 in computers_cards and 10 in computers_cards:
        print("Computer has blackjack")
        return True
    else:
        return False

def is_score_over_21(player_score):
    if player_score > 21:
        return True
    else:
        return False

def is_ace(users_cards):    
    if 11 in users_cards:
        return True
    else:
        return False

def change_ace(users_score, users_cards):  
    card_eleven_index = users_cards.index(11) 
    users_cards[card_eleven_index] = 1
    users_score -= 10 # 11 -> 1 Playerscore 
    if users_score > 21:
        return True, users_score
    else:
        return False, users_score
    
def print_score(users_score, users_cards, computers_score, computers_cards):
    print(f"Your final hand: {users_cards} final score: {users_score}\nComputer's final hand: {computers_cards}, final score: {computers_score}")

def compare(users_score, users_cards, computers_score, computers_cards):
    users_score = calculate_player_score(users_cards)
    computers_score = calculate_player_score(computers_cards)

    if users_score > computers_score:
        print_score()
        print("You WIN")
    elif users_score < computers_score:
        print_score()
        print("You lose")
    else:
        print_score()
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
            print("You lose")
            return True
    else:
        if is_score_over_21(users_score):
            if is_ace(users_cards):
                value_change_ace, users_score = change_ace(users_score, users_cards)
                if value_change_ace:
                    print_score(users_score, users_cards, computers_score, computers_cards)
                    print("You lose")
                    return True
                else: 
                    if another_card():
                        users_cards.append(draw_card())
                        return False
            else:
                print_score(users_score, users_cards, computers_score, computers_cards)
                print("You lose")
                return True
        else:
            if another_card():
                users_cards.append(draw_card())
                return False
            else:
                while computers_score < 17:
                    computers_cards.append(draw_card())
                    computers_score = calculate_player_score(computers_cards)
                    if is_score_over_21(computers_score):
                        if is_ace(computers_cards):
                            value_change_ace, computers_score = change_ace(computers_score, computers_cards)
                            if value_change_ace:
                                print_score(users_score, users_cards, computers_score, computers_cards)
                                print("You WIN")
                                return True
                            elif computers_score == 21:
                                print_score(users_score, users_cards, computers_score, computers_cards)
                                print("You lose")
                                return True
                            else:
                                compare(users_score, users_cards, computers_score, computers_cards)
                    else: 
                        compare(users_score, users_cards, computers_score, computers_cards)

                    

if __name__ == "__main__":
    value_play_blackjack = True

    while value_play_blackjack == True:
        value_play_blackjack = play_blackjack()
        users_cards, computers_cards = start_game()


        # users_cards = [11,11]

        game_finished = False
        while not game_finished:
            game_finished = engine()
            

        