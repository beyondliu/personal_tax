
def personal_tax(x):
    taxable = x - 3500 
    if taxable <= 0:
        return x
    if taxable >= 80000:
        return x - ((taxable-80000)*0.45+25000*0.35+20000*0.3+26000*0.25+4500*0.2+300+45)        
    elif 80000 > taxable >= 55000:
        return x - ((taxable-55000)*0.35+20000*0.3+26000*0.25+4500*0.2+300+45)    
    elif 55000 > taxable >= 35000:
        return x - ((taxable-35000)*0.3+26000*0.25+4500*0.2+300+45)
    elif 35000 > taxable >= 9000:
        return  x - ((taxable-9000)*0.25+4500*0.2+300+45)
    elif 9000 > taxable >= 4500:
        return x - ((taxable-4500)*0.2+300+45)
    elif 4500 > taxable >= 1500:
        return x - ((taxable-1500)*0.1+45)
    else:
        return x - taxable*0.03

                        