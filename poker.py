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
    one:[ace,two],
    two:[one,three],
    three:[two,four],
    four:[three,five],
    five:[four,six],
    six:[five,seven],
    seven:[six,eight],
    eight:[seven,nine],
    nine:[eight,ten],
    ten:[nine,jack],
    jack:[ten,queen],
    queen:[jack,king],
    king:[queen,ace],
    ace:[king,one]
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
            pred,suc = neighbours[value]
            if (pred in values) and (suc in values):
                cntr = cntr + 1
        if cntr >= 3:
            return True
        else:
            return False
    return False
