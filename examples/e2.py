from gettext import find


text = "X-DSPAM-Confidence:    0.8475"
n1 = text.find('0')
n2 = text.find('5')


print(n1)
print(n2)

n3 = text[n1:n2+1]
print(n3)