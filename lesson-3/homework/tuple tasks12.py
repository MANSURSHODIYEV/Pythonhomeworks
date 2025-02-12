numbers = (10, 25, 8, 99, 45, 67)

# Takrorlanmas elementlarni saralash
tahrirlangan = sorted(set(numbers))  # set() takrorlanishlarni oldini oladi

# Ikkinchi eng katta elementni olish
if len(tahrirlangan) > 1:
    second_largest = tahrirlangan[-2]  # Eng katta elementdan oldingisi
    print("Ikkinchi eng katta element:", second_largest)
else:
    print("Tupleda yetarli element yo'q.")
