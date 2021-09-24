'''

'''

N = int(input())
lst = list(map(int, str(input())))

red = []
blue = []
yellow = []

# red : 5432154321


# blue : 1234512345
for i in range(len(lst)):
    if i == 5:
        i = 1
    blue.append(i+1)


# red = blue.reversed()

for i in range(len(lst)):
    yellow.append(3)

print(red)
print(blue)
print(yellow)
