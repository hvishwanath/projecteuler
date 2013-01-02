#Global Definitions
one = '1'
two = '2'
three = '3'
four = '4'
five = '5'
six = '6'
seven = '7'
eight = '8'
nine = '9'
ten = '10'
jack = 'J'
queen = 'Q'
king = 'K'
ace = 'A'

neighbours = {
    one:[1,ace,two],
    two:[2,one,three],
    three:[3,two,four],
    four:[4,three,five],
    five:[5,four,six],
    six:[6,five,seven],
    seven:[7,six,eight],
    eight:[8,seven,nine],
    nine:[9,eight,ten],
    ten:[10,nine,jack],
    jack:[11,ten,queen],
    queen:[12,jack,king],
    king:[13,queen,ace],
    ace:[14,king,one]
    }

def isSameSuite(hand):
    """True if all cards are of same family"""
    suite = getSuite(hand)
    s = ''.join(suite)
    return s.count(s[0]) == 5

def getSuite(hand):
    cards = hand.split(' ')
    suite = []
    for card in cards:
        suite.append(card[-1])
    return suite

def getValues(hand):
    cards = hand.split(' ')
    values = []
    for card in cards:
        values.append(card[:-1])
    return values    
    
def isRoyalFlush(hand):
    """Ten, Jack, Queen, King, Ace, in same suit"""
    if isSameSuite(hand):
        values = getValues(hand)
        if (ten in values) and (jack in values) and (queen in values) and (king in values) and (ace in values):
            return True
    return False

def isStraightFlush(hand):
    cntr = 0
    if isSameSuite(hand):
        values = getValues(hand)
        for value in values:
            rank,pred,suc = neighbours[value]
            if (pred in values) and (suc in values):
                cntr = cntr + 1
        if cntr >= 3:
            return True
        else:
            return False
    return False

def isFourOfAKind(hand):
    values = getValues(hand)
    for value in values:
        if values.count(value) == 4:
            return True
    return False

def isFullHouse(hand):
    if isThreeOfAKind(hand):
        
def isThreeOfAKind(hand):
    values = getValues(hand)
    for value in values:
        if values.count(value) == 3:
            return True
    return False

def isOnePair(hand):
    values = getValues(hand)
    for value in values:
        if values.count(value) == 3:
            return True
    return False

def getHighCard(hand):
    values = getValues(hand)
    max = 0
    
    for value in values:
def isFullHouse(hand):
    