"""
This is a sample knapsack problem based on greedy algorithm
Imagine you have a knapsack with a wight limitation.
You want to fill it with your items.

The list of your items:
['Watch', 'Radio', 'Books', 'Sanitizer', 'Jacket', 'Flower','Gift','Candy']

The values you gain from these items:
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


def greedy(items, maxWeight, keyFunction):
    sortedItems = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(sortedItems)):
        if (totalWeight + sortedItems[i].getWeight()) <= maxWeight:
            result.append(sortedItems[i])
            totalWeight += sortedItems[i].getWeight()
            totalValue += sortedItems[i].getValue()
    return (result, totalValue)


def greedytest(items, constraint, keyFunction):
    res, val = greedy(items, constraint, keyFunction)
    print('The total value you gain = ', val)
    print('Your items are : ')
    for item in res:
        print(' ', item)


def GreedyTest(maxWeight):
    items = OurItems()
    print('---------------------------------------------------')
    print('If you fill your backpack according to The Values :\nThe Maximum weight is = ', maxWeight)
    greedytest(items, maxWeight, value)
    print('------------------------------------------------------------')
    print('If you fill your backpack according to The  Inverse Weights :\nThe Maximum weight is = ', maxWeight)
    greedytest(items, maxWeight, weightInverse)
    print('------------------------------------------------------------')
    print('If you fill your backpack according to The Density of Items :\nThe Maximum weight is = ', maxWeight)
    greedytest(items, maxWeight, density)
    print('----------------------------------------------------------')


W = int(input('Inter the maximum weight of you knapsack, between 2 to 50 :\n'))
if 2 <= W <= 50:
    GreedyTest(W)
else:
    print('your number is not in the range (2,50)')
