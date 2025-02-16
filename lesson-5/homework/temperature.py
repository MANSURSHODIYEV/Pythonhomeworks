def convert_cel_to_far(c):
    return round(c * 9 / 5 + 32, 2)

def convert_far_to_cel(f):
    return round((f - 32) * 5 / 9, 2)

f = float(input("Enter temperature in F:"))
print(f"{f} degrees F = {convert_far_to_cel(f)} degrees C")
c = float(input("Enter the temperature in C: "))
print(f"{c} degrees C = {convert_cel_to_far(c)} degrees F")

