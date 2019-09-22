def computepay(h,r):
    if h <=40:
        pay= h * r
        return pay

    else:
        pay= 40 * r + (h-40)* 1.5*r
        return pay


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

p=computepay(h,r)
print(p)
