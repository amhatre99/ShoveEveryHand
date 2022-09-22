from treys import Evaluator
from treys import Card
from treys import Deck

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suited = ['o', 's']
table = {}


def simulate(abbreviated_hand, trials):
    evaluator = Evaluator()

    if abbreviated_hand[-1] != 's':
        hand = sorted([Card.new(abbreviated_hand[0] + 's'), Card.new(abbreviated_hand[1] + 'c')])
    else:
        hand = sorted([Card.new(abbreviated_hand[0] + 's'), Card.new(abbreviated_hand[1] + 's')])

    hand_wins = 0
    for _ in range(trials):
        deck = Deck()
        deck.cards.remove(hand[0])
        deck.cards.remove(hand[1])
        villain = deck.draw(2)
        board = deck.draw(5)
        hero_rank = evaluator.evaluate(board, hand)
        villain_rank = evaluator.evaluate(board, villain)
        if hero_rank < villain_rank:
            hand_wins += 1
        elif hero_rank == villain_rank:
            hand_wins += 0.5

    return hand_wins / trials


if __name__ == '__main__':
    trials = 100000

    for rankOne in range(13):
        for rankTwo in range(rankOne + 1, 13):
            for suit in suited:
                curr_hand = ranks[rankTwo] + ranks[rankOne] + suit
                table[curr_hand] = simulate(curr_hand, trials)
    for rank in ranks:
        poket_pair = rank + rank
        table[poket_pair] = simulate(poket_pair, trials)

    print(table)
