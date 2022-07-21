set_2 = []
set_7 = []

for i in range(1,1001):
    if i % 2 == 0:
        set_2.append(i)

for j in range(1, 1001):
    if i % 7 == 0:
        set_7.append(j)

print(sum(set(set_2)^set(set_7)))

