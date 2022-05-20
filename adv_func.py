# lambda

result = lambda a,b : a+b
print(type(result))


set1 = ("val1",)
print(type(set1))
# insidde the tuple we are having one limitation

list1 = [1,2,3,[11,22,[111,123,55]],["harry"]]
print(list1[3][2][1])
# via mail


'''
sweetness value of the sweetest ice cream. Note that there is a class provided for you in the Tests tab.

class IceCream:
  def __init__(self, flavor, num_sprinkles):
    self.flavor = flavor
    self.num_sprinkles = num_sprinkles

Each sprinkle has a sweetness value of 1
Check below for the sweetness values of the different flavors.

Flavors	   Sweetness Value
Plain	        0
Vanilla	        5
ChocolateChip	5
Strawberry  	10
Chocolate	    10

Examples
ice1 = IceCream("Chocolate", 13)         # value of 23     10+13
ice2 = IceCream("Vanilla", 0)           # value of 5       5+0
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8      5+3


sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23

sweetest_icecream([ice3, ice1]) ➞ 23

sweetest_icecream([ice3, ice5]) ➞ 17
Notes
Remember to only return the sweetness value.

'''

lst = [1,2,3,4,5,67]

(i>3 for i in lst)

# (exp for i in var)
'''

python+javascript(react+node)

15lpa

lco
Hitesh LCO

ineuron
'''
class IceCream:
  def __init__(self, flavor, num_sprinkles):
    self.flavor = flavor
    self.num_sprinkles = num_sprinkles

ice1 = IceCream("Chocolate", 13)         # value of 23     10+13

ice2 = IceCream("Vanilla", 0)           # value of 5       5+0
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8      5+3

def sweetest_icecreamlst(lst):
    flavor_val = {
        "Plain" : 0,
        "Vanilla" : 5,
        "ChocolateChip" : 5,
        "Strawberry" : 10,
        "Chocolate" : 10
    }
    return max(i.num_sprinkles + flavor_val[i.flavor] for i in lst)  # lst = [ice1,ice2....]

print(sweetest_icecreamlst([ice1, ice2, ice3, ice4, ice5]))

        


