import random
suits = ['Cơ', 'Rô', 'Chuồn', 'Bích']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(rank, suit) for suit in suits for rank in ranks]
def get_winner(players, scores):
    max_score = max(scores)
    winners = [i for i, j in enumerate(scores) if j == max_score]
    return [players[i] for i in winners]
def play_game():
    players = ['Người 1', 'Người 2', 'Người 3', 'Người 4']
    random.shuffle(deck)
    hands = [deck[i::4] for i in range(4)]
    scores = []
    for hand in hands:
        score = 0
        for card in hand:
            rank, _ = card
            if rank.isdigit():
                score += int(rank)
            elif rank in ['J', 'Q', 'K']:
                score += 10
            elif rank == 'A':
                score += 11
        scores.append(score)
    for i, hand in enumerate(hands):
        print(f'{players[i]}: {hand} (Điểm: {scores[i]})')
    winners = get_winner(players, scores)
    if len(winners) == 1:
        print(f'Người chơi {winners[0]} thắng!')
    else:
        print('Hòa!')
play_game()