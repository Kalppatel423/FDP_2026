#String
x = input("Enter a string: ")
print(x)

#integer
y = int(input("Enter an integer: "))
print(y)

#Float
z = float(input("Enter a float: "))
print(z)

#List
a = input("Enter list elements: ").split()
print("List:", a)

#tuple
b = input("Enter tuple elements ").split()
print(b)

#set
d =  input("Enter set elements: ").split()
print(d)


#Methods
#String Methods
s = "Good Morning"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.replace("G", "M"))
print(s.find("o"))
print(s.count("o"))
print(s.split())
print(len(s))
print(s.isalpha())
print(s.isalnum())
print(s.startswith("Z"))
print(s.endswith("k"))

#List Methods
l = [10, 20, 30]
l.append(40)
l.insert(1, 15)
l.extend([50, 60])
l.remove(20)
l.pop()
l.sort()
l.reverse()
print(l)
print(l.count(30))
print(l.index(30))
print(len(l))
print(l.copy())
l.clear()
print(l)

#Tuple methods
t = (1, 2, 3, 2)
print(t.count(2))
print(t.index(3))
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))

#Set Methods 
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
s.discard(2)
print(s)
print(len(s))
print(s.copy())
print(s.union({1, 7}))
print(s.intersection({1, 3}))
print(s.difference({3}))
print(s.symmetric_difference({3, 4}))
s.clear()
print(s)

#Dictionary Methods
d = {"a": 1, "b": 2}
print(d.keys())
print(d.values())
print(d.items())
print(d.get("a"))
d.update({"c": 3})
print(d)
print(d.pop("b"))
print(d)
print(d.copy())
print(len(d))
d.clear()
print(d)



