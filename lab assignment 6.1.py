s = input("Enter string: ")

v = c = sp = l = 0

for i in s:
    if i in "aeiouAEIOU":
        v += 1
    elif i.isalpha():
        c += 1
    if i == " ":
        sp += 1
    if i.islower():
        l += 1

print("Vowels:", v)
print("Consonants:", c)
print("Spaces:", sp)
print("Lowercase:", l)