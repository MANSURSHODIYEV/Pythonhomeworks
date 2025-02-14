txt = "abcdefghijklmno"
vowels = "aeiouAEIOU"
res = ""
i = 0

while i < len(txt):
    res += txt[i]
    if (i + 1) % 3 == 0 and i != len(txt) - 1:
        if txt[i] in vowels and i + 1 < len(txt):
            res += txt[i + 1] + "_"
            i += 1  # Keyingi harfni oldindan qo‘shganimiz uchun indeksni oshiramiz
        else:
            res += "_"
    i += 1

print(res)
