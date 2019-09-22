text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(".")
slice= text[pos-1:pos+4]
print(slice)
number=float(slice)
print(number)
