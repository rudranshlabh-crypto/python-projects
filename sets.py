basket1={"apple","banana","mango","apple","grape"}
basket2={"banana","kiwi","mango","kiwi"}

print("fruits in basket1 are:", basket1)
print("fruits in basket2 are:", basket2)

basket1.add("orange")
print("after adding orange in basket1:", basket1)

common_fruits = basket1.intersection(basket2)
print("common fruits in basket 1 and 2 are:", common_fruits)

import array as arr:
a=arr.array('i', [1,2,3,2,1])
a.insert(1,5)
a.append(6)
print("array after adding elements is", a)
count1=a.count(1)
print(count1)
a.reverse()
print (a)