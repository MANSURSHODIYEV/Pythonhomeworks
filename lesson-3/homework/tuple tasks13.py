numbers = (10, 25, 8, 99, 45, 67)


tahrirlangan = sorted(set(numbers)) 

if len(tahrirlangan) > 1:
    second_largest = tahrirlangan[-2] 
    print("Ikkinchi eng katta element:", second_largest)
else:
    print("Tupleda yetarli element yo'q.")
