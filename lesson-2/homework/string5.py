s = input()
print(sum(c in "aeiouAEIOU" for c in s), sum(c.isalpha() and c not in "aeiouAEIOU" for c in s))
