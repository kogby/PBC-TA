class Card:
    def __init__(self, suit, rank):
        suit_order = ["C", "D", "H", "S"]
        rank_order = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
        self.suit = int(suit_order.index(suit))
        self.rank = int(rank_order.index(rank))

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def draw_a_card(self, card):
        self.cards.append(card)

    def is_straight(self):  # 判斷是否為順子
        values = [c.get_rank() for c in self.cards]
        if set(values) == {0, 9, 10, 11, 12}:
            return True
        if max(values) - min(values) == 4 and len(set(values)) == 5:
            return True
        return False

    def is_flush(self):  # 判斷是否為同花
        for i in range(1, len(self.cards)):
            if self.cards[i].get_suit() != self.cards[i - 1].get_suit():
                return False
        return True

    def count_suits(self):
        suits = [0, 0, 0, 0]
        for c in self.cards:
            suits[c.get_suit()] += 1
        return suits

    def count_ranks(self):
        ranks = [0] * 13
        for c in self.cards:
            ranks[c.get_rank()] += 1
        return ranks

    def get_rank(self):
        if self.is_straight() and self.is_flush():
            return 9
        elif 4 in self.count_ranks():
            return 8
        elif 3 in self.count_ranks() and 2 in self.count_ranks():
            return 7
        elif self.is_flush():
            return 6
        elif self.is_straight():
            return 5
        elif 3 in self.count_ranks() and 2 not in self.count_ranks():
            return 4
        elif 2 in self.count_ranks():
            if self.count_ranks().count(2) == 2:
                return 3
            else:
                return 2
        else:
            return 1


player_num = int(input())
all_cards = []
for i in range(player_num):
    all_cards.append(input().split(","))

player_name = input().split(",")
players = []
for i, cards in enumerate(all_cards):
    player = Deck(player_name[i])
    players.append(player)
    for c in cards:
        suit = c[0]
        rank = c[1]
        card = Card(suit, rank)
        player.draw_a_card(card)

players.sort(key=lambda x: x.get_rank(), reverse=True)

count = 1
for i in range(len(players) - 1):
    if players[i].get_rank() == players[i + 1].get_rank():
        count += 1
    else:
        break

if count > 1:
    print(count)

if count == 1:
    print(players[0].name)
