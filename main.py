import random

deck = [(rank, suit) for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] for suit in ['♥', '♦', '♣', '♠']]
random.shuffle(deck)

def distribute_cards(deck):
    return [deck.pop() for _ in range(4)]

def check_for_capture(player_card, table_cards):
    captured_cards = []
    for card in table_cards:
        if card[0] == player_card[0]:  # نفس القيمة
            captured_cards.append(card)
    return captured_cards

def play_basra():
    player1_hand = distribute_cards(deck)
    player2_hand = distribute_cards(deck)
    table_cards = distribute_cards(deck)

    player1_score = 0
    player2_score = 0

    while deck:
        print("\nبطاقات اللاعب 1:", player1_hand)
        print("البطاقات على الطاولة:", table_cards)
        player1_choice = int(input("اختر بطاقة للعب (0-3): "))
        player1_card = player1_hand.pop(player1_choice)

        captured_cards = check_for_capture(player1_card, table_cards)
        if captured_cards:
            table_cards = [card for card in table_cards if card not in captured_cards]
            player1_score += len(captured_cards) + 1  # +1 لنفس البطاقة
            print("اللاعب 1 التقط", captured_cards)

        table_cards.append(player1_card)

        player2_card = player2_hand.pop(random.randint(0, len(player2_hand) - 1))
        print("\nاللاعب 2 لعب:", player2_card)

        captured_cards = check_for_capture(player2_card, table_cards)
        if captured_cards:
            table_cards = [card for card in table_cards if card not in captured_cards]
            player2_score += len(captured_cards) + 1
            print("اللاعب 2 التقط", captured_cards)

        table_cards.append(player2_card)

        if not player1_hand and deck:
            player1_hand = distribute_cards(deck)
            player2_hand = distribute_cards(deck)

    print("\nانتهت اللعبة!")
    print("نتيجة اللاعب 1:", player1_score)
    print("نتيجة اللاعب 2:", player2_score)

play_basra()