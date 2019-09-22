hrs = input("Enter Hours:")
try:
    h=float(hrs)
except:
    print( "You did not enter a numeric value")
    quit()
rate= input("Enter Rate:")
try:
    r = float(rate)
except:
    print ( "You did not enter a numeric value")
    quit()

if h <=40:
    pay= h * r
else:
    pay= 40 * r + (h-40)* 1.5*r

print ( "Pay = ",pay)
