from random import Random
import random

class Card:
    __types__ = ["Bich", "Nhep", "Ro", "Co"]
    __ranks__ = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, type = 0, rank = 0):
        self.type = type
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} {self.type}"
    
    def compare(self, otherCard):
        # So sánh chất của quân bài
        if self.type > otherCard.type:
            return 1
        elif self.type < otherCard.type:
            return -1
        else: # Hai quân bài có cùng chất => so sánh giá trị
            if self.rank > otherCard.rank:
                return 1
            elif self.rank < otherCard.rank:
                return -1
            else: # Hai quân bài cùng chất cùng giá trị
                return 0
    # So sánh bằng
    def __eq__(self, otherCard):
        return self.compare(otherCard) == 0
    # So sánh lớn hơn
    def __gt__(self, otherCard):
        return self.compare(otherCard) == 1
    # So sánh nhỏ hơn
    def __lt__(self, otherCard):
        return self.compare(otherCard) == -1

class Deck:
    # Bộ bài có 52 quân
    def __init__(self):
        self.cards = []
        for type in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(type, rank))
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + str(i+1) + ") " + str(self.cards[i]) + '\n'
        return s
    def shuffle(self):
        Random.shuffle(self.cards)
    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
    def isEmpty(self):
        return self.cards == []
    def pop(self):
        return self.cards.pop()
    def deal(self, hands):
        num_cards = len(self.cards)
        num_hands = len(hands)

        for i in range(num_cards):
            if self.isEmpty():
                break
            card = self.pop()
            hand = hands[i % num_hands]
            hand.add(card)

class Hand(Deck):
    def __init__(self, name="Nguyen Van A"):
        self.cards = []
        self.name = name
    def add(self, card):
        self.cards.append(card)
    def remove(self, index):
        self.cards.pop(index - 1)
    def get_card(self, index):
        return self.cards[index]
d1 = Deck()

p1 = Hand("A")
p2 = Hand("B")
p3 = Hand("C")
p4 = Hand("D")

hands = [p1, p2, p3, p4]

# Chia bài
d1.deal(hands)
play_first = random.randint(0,4)
count_turn = 1
recentCard = Card(0,0)

while True:
    if count_turn >= 4:
        count_turn = 1
        recentCard = Card(0,0)
    # Tìm ra người chơi hiện tại và người chơi kế tiếp
    player = hands[play_first % 4]
    play_first += 1

    # IN ra người chơi hiện tại
    print(player)


    ask = input("Danh hoac bo qua: ")

    while ask == "":
        ask = input("Danh hoac bo qua: ")
        
    # Nếu người chơi chọn đánh
    while ask == 'play':
        index = int(input('quan bai nao: '))

        if recentCard < player.get_card(index - 1):
            recentCard = player.get_card(index - 1)
            player.remove(index - 1)
            break
        else:
            print("quan bai phai lon hon quan bai truoc")
            ask = input("danh hoac bo qua: ")
    if ask == "pass":
        count_turn += 1
    if player.isEmpty():
        break