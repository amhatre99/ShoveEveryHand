from treys import Evaluator
from treys import Card
from treys import Deck


def rank_key(rank):
    ranks = {'2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             'T': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 14}
    return ranks[rank]


def find_threshold(p, starting_stack, trials):
    evaluator = Evaluator()

    hero_wins = 0
    for _ in range(trials):
        hero_money = starting_stack
        big_blind = True
        while 0 < hero_money < 2 * starting_stack:
            deck = Deck()
            hero = sorted(deck.draw(2))
            hand_string = Card.int_to_str(hero[0]) + Card.int_to_str(hero[1])
            if hand_string[0] == hand_string[2]:
                hand_string = hand_string[0] + hand_string[0]
            elif hand_string[1] != hand_string[3]:
                hand_string = ''.join(sorted([hand_string[0], hand_string[2]], key=rank_key, reverse=True)) + 'o'
            else:
                hand_string = ''.join(sorted([hand_string[0], hand_string[2]], key=rank_key, reverse=True)) + 's'
            if final_lookup[hand_string] < p:
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


final_lookup = {
    "32o": 0.321205,
    "32s": 0.36018,
    "42o": 0.33388,
    "42s": 0.368135,
    "52o": 0.3431,
    "52s": 0.37614,
    "62o": 0.34088,
    "62s": 0.37649,
    "72o": 0.34478,
    "72s": 0.382855,
    "82o": 0.368945,
    "82s": 0.40156,
    "92o": 0.39208,
    "92s": 0.42664,
    "T2o": 0.416515,
    "T2s": 0.44856,
    "J2o": 0.44395,
    "J2s": 0.471895,
    "Q2o": 0.473125,
    "Q2s": 0.501715,
    "K2o": 0.50352,
    "K2s": 0.528925,
    "A2o": 0.550065,
    "A2s": 0.573265,
    "43o": 0.351585,
    "43s": 0.387365,
    "53o": 0.36303,
    "53s": 0.39894,
    "63o": 0.36387,
    "63s": 0.396605,
    "73o": 0.36685,
    "73s": 0.399835,
    "83o": 0.3743,
    "83s": 0.40591,
    "93o": 0.398625,
    "93s": 0.433025,
    "T3o": 0.42394,
    "T3s": 0.45685,
    "J3o": 0.45219,
    "J3s": 0.482095,
    "Q3o": 0.48158,
    "Q3s": 0.510205,
    "K3o": 0.51155,
    "K3s": 0.540655,
    "A3o": 0.559325,
    "A3s": 0.580655,
    "54o": 0.381905,
    "54s": 0.412635,
    "64o": 0.379965,
    "64s": 0.41138,
    "74o": 0.386,
    "74s": 0.419915,
    "84o": 0.39619,
    "84s": 0.42568,
    "94o": 0.405325,
    "94s": 0.438245,
    "T4o": 0.439745,
    "T4s": 0.46694,
    "J4o": 0.461345,
    "J4s": 0.49106,
    "Q4o": 0.49041,
    "Q4s": 0.519255,
    "K4o": 0.52095,
    "K4s": 0.546905,
    "A4o": 0.564565,
    "A4s": 0.59144,
    "65o": 0.401655,
    "65s": 0.432765,
    "75o": 0.403345,
    "75s": 0.43762,
    "85o": 0.413065,
    "85s": 0.444165,
    "95o": 0.427335,
    "95s": 0.456675,
    "T5o": 0.44053,
    "T5s": 0.473765,
    "J5o": 0.471935,
    "J5s": 0.49913,
    "Q5o": 0.50108,
    "Q5s": 0.52871,
    "K5o": 0.53214,
    "K5s": 0.557145,
    "A5o": 0.5785,
    "A5s": 0.598575,
    "76o": 0.422765,
    "76s": 0.454555,
    "86o": 0.43207,
    "86s": 0.46088,
    "96o": 0.44622,
    "96s": 0.476085,
    "T6o": 0.461065,
    "T6s": 0.48922,
    "J6o": 0.478775,
    "J6s": 0.50926,
    "Q6o": 0.512205,
    "Q6s": 0.538555,
    "K6o": 0.54271,
    "K6s": 0.566485,
    "A6o": 0.57598,
    "A6s": 0.59805,
    "87o": 0.45078,
    "87s": 0.479915,
    "97o": 0.463655,
    "97s": 0.491425,
    "T7o": 0.47691,
    "T7s": 0.506115,
    "J7o": 0.50018,
    "J7s": 0.524915,
    "Q7o": 0.51759,
    "Q7s": 0.54301,
    "K7o": 0.550945,
    "K7s": 0.57514,
    "A7o": 0.588335,
    "A7s": 0.61074,
    "98o": 0.479025,
    "98s": 0.508875,
    "T8o": 0.49666,
    "T8s": 0.5221,
    "J8o": 0.516285,
    "J8s": 0.538895,
    "Q8o": 0.535195,
    "Q8s": 0.55847,
    "K8o": 0.564235,
    "K8s": 0.583115,
    "A8o": 0.59903,
    "A8s": 0.619395,
    "T9o": 0.51564,
    "T9s": 0.54182,
    "J9o": 0.531335,
    "J9s": 0.55822,
    "Q9o": 0.54894,
    "Q9s": 0.57523,
    "K9o": 0.57897,
    "K9s": 0.599095,
    "A9o": 0.607355,
    "A9s": 0.62862,
    "JTo": 0.55402,
    "JTs": 0.57144,
    "QTo": 0.572085,
    "QTs": 0.592445,
    "KTo": 0.59903,
    "KTs": 0.615665,
    "ATo": 0.629815,
    "ATs": 0.643865,
    "QJo": 0.579955,
    "QJs": 0.60005,
    "KJo": 0.605935,
    "KJs": 0.62696,
    "AJo": 0.633755,
    "AJs": 0.654685,
    "KQo": 0.61458,
    "KQs": 0.63409,
    "AQo": 0.643045,
    "AQs": 0.66167,
    "AKo": 0.651555,
    "AKs": 0.670145,
    "22": 0.50144,
    "33": 0.537105,
    "44": 0.57276,
    "55": 0.604375,
    "66": 0.632445,
    "77": 0.66346,
    "88": 0.691645,
    "99": 0.719595,
    "TT": 0.74883,
    "JJ": 0.774765,
    "QQ": 0.798175,
    "KK": 0.82402,
    "AA": 0.85419,
}

if __name__ == '__main__':
    hero_starting_stack = 400
    curr_prob = 0.5
    high = 0.65
    maximum = 0.5
    best_prob = 0.5
    precision = 0.0001
    while curr_prob < high:
        win_rate = find_threshold(curr_prob, hero_starting_stack, trials=10000)
        if win_rate > maximum:
            maximum = win_rate
            best_prob = curr_prob
        curr_prob += precision
    print(best_prob, maximum)
    # finds
    # p = 0.6445999999999841
    # win_rate = 0.7384
