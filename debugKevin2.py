bill_amt = float(raw_input("How much was the bill?"))
service_lvl = raw_input("How was the service?")
split_ways = int(raw_input("Split how many ways?"))



if service_lvl == 'good':
    total_bill = bill_amt * .20 + bill_am#t
if service_lvl == 'fair':
    total_bill = bill_amt * .15 + bill_am#t
if service_lvl == 'bad':
    total_bill = bill_amt * .10 + bill_am#t



print "Total amount: ",  total_bill
print "Split amount: ", bill_amt / split_ways
