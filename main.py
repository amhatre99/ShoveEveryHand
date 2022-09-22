from poker.hand import Range
from treys import Evaluator
from treys import Card
from treys import Deck
from poker.hand import Combo


def shove_simulator(strategy, starting_stack, trials):
    evaluator = Evaluator()

    hero_wins = 0
    for _ in range(trials):
        hero_money = starting_stack
        big_blind = True
        while 0 < hero_money < 2 * starting_stack:
            deck = Deck()
            hero = deck.draw(2)
            str_hand = Card.int_to_str(hero[0]) + Card.int_to_str(hero[1])
            if Combo(str_hand) not in strategy:
                hero_money -= int(big_blind) * 0.5 + 0.5
                big_blind = not big_blind
            else:
                villain = deck.draw(2)
                board = deck.draw(5)
                hero_rank = evaluator.evaluate(board, hero)
                villain_rank = evaluator.evaluate(board, villain)
                if hero_rank < villain_rank:
                    hero_money = max(2 * starting_stack, 2 * hero_money)
                elif hero_rank > villain_rank:
                    hero_money = max(0, 2 * hero_money - 2 * starting_stack)
        if hero_money == 2 * starting_stack:
            hero_wins += 1

    return hero_wins / trials


if __name__ == '__main__':
    hero_starting_stack = 200
    strat_1 = set(Range("33+, K7o+, K6s+, A2o+, A2s+, Q8o+, Q8s+").combos)
    strat_2 = set(Range("AJs, AQs, AKo, AKs, 77, 88, 99, TT, JJ, QQ, KK, AA").combos)

    print(len(strat_2))
    print(shove_simulator(strat_2, hero_starting_stack, trials=100000))
