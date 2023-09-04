text = "X-DSPAM-Confidence:    0.8475"

colonPosition = text.find(':')
slicedNum = text[colonPosition+1:]
strippedNum = slicedNum.strip()
numF = float(strippedNum)

print(numF);
