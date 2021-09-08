"""
This is a sample Binary knapsack problem based on Optimal choice algorithm
Imagine you have a knapsack with a capacity.
You want to fill it with your items.

The list of your items:
['Watch', 'Radio', 'Books', 'Sanitizer', 'Jacket', 'Flower','Gift','Candy']

The values of your items:
[120, 20, 20, 80, 150, 64, 40, 50]

The weights of these items:
[2, 3, 5, 8, 10, 5, 15, 5]


@author: Manijeh Komeili
"""


class Item(object):

    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<<< ' + self.name + ', ' + 'value: ' + str(int(self.value)) + ', ' + 'weight: ' + str(
            int(self.weight)) + ' >>>'
        return result


def value(item):
    return item.getValue()


def weightInverse(item):
    return 1.0 / item.getWeight()


def density(item):
    return item.getValue() / item.getWeight()


def OurItems():
    names = ['Watch', 'Radio', 'Books', 'Sanitizer', 'Jacket', 'Flower', 'Gift', 'Candy']
    values = [120, 20, 20, 80, 150, 64, 40, 50]
    weights = [2, 3, 5, 8, 10, 5, 15, 5]
    Items = []
    for i in range(len(names)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items


def BinaryRep(n, nDigit):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    if len(result) > nDigit:
        raise ValueError('Error')
    for i in range(nDigit - len(result)):
        result = '0' + result

    return result


def Powerset(L):
    powerset = []
    for i in range(0, 2 ** len(L)):
        binStr = BinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset


def chooseOpt(pset, maxWeight, getVal, getWeight):
    optVal = 0.0
    optSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > optVal:
            optVal = itemsVal
            optSet = items
    return (optVal, optSet)


def testOpt(maxWeight):
    items = OurItems()
    pset = Powerset(items)
    oV, oS = chooseOpt(pset, maxWeight, Item.getValue, Item.getWeight)

    print('The total value you gain = ', oV)
    print('Your items are : ')
    for item in oS:
        print(item)


W = int(input('Inter the maximum weight of you knapsack, between 2 to 50 :\n'))
if 2 <= W <= 50:
    testOpt(W)
else:
    print('your number is not in the range (2,50)')
