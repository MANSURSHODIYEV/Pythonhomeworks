my_dict = {'a': 1, 'b': 2, 'c': 3}


key = 'b'
value = my_dict.get(key)

if value is not None:
    print(f"Kalit va qiymat juftligi: {key}: {value}")
else:
    print("Kalit mavjud emas")
