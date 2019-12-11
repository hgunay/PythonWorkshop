x = object()
y = object()

list1 = [x]*10
list2 = [y]*10
list = list1 + list2

print("List 1 contains %d objects " % len(list1))
print("List 2 contains %d objects " % len(list2))
print("List contains %d objects " % len(list))

if list1.count(x) == 10 and list2.count(y) == 10:
    print("Almost there...")

if list.count(x) == 10 and list.count(y) == 10:
    print("Great!")