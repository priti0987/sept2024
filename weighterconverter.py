wei = float(input("Enter your weight : "))

unit = input("Kilograms or Pounds? (K or L) : " )
if unit == 'K':
    wei == wei*2.205
    unit = "Lbs."
elif unit == 'L':
    wei = wei/2.205
    unit = "Kgs."
else:
    print(f"Unit => {unit} was not valid ")
print(f"Your weight is :{round(wei)} {unit}")