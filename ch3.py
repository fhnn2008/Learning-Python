score =input("Enter a score : ")
try:
    sc = float(score)
except:
    print("Enter a numeric value")
if sc >= 0.9:
    print ("A")
elif sc >= 0.8:
    print("B")
elif sc >= 0.7:
    print("C")
elif sc >= 0.6:
    print("D")
else:
    print ("E")
