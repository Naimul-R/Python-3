# st = set() #create an empty set 

st = {3, 6, 10, 18, "Naimul", 99.99}

st.add(100)
print(st, type(st))
st.remove(18)
print(st, type(st))

#inportant methods for sets 
s1 = {4, 6, 19, 18, 100}
s2 = {45, 100, 108}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.issubset(s2))
