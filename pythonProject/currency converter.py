#currency convertor
#converting from indian rupees to given currency

with open('currency.txt') as op:
    lines = op.readlines()

CurDict = {}
for line in lines:
    parsed = line.split('\t')
    CurDict[parsed[0]] = parsed[1]

[print(cur) for cur in CurDict]
ip = input("Enter the currency in which you want to change\n")


rs = int(input("Enter the amount: "))
cur = float(CurDict[ip])*rs
print(f"The amount {rs} rupees in {ip} is {cur}")