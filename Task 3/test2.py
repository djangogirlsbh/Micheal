
ans = int(input("1 for cel to Fah, 2 for Fah to cel"))

if ans == 1:
    cel = int(input("enter temp in cel"))
    fah = (cel - 9/5) + 32
    print('%.2f Celsius is: %.2f Fahrenheit' %(cel, fah))
else:
    fah = int(input("enter temp in Fah"))
    cel = (fah - 32) * 5/9
    print('%.2f Fahrenheit is: %0.2f Celsius' %(fah, cel))



