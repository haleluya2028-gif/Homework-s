income = int ( input("enter your income "))
def tax_info (income):
    if income>=0 and income <=2000:
        tax= income*0
        print("Total tax is " + str(tax))
        print ( "Net income is " + str (income - tax))
    elif income>=2001 and income <=4000:
        tax= income*0.15
        print("Total tax is " + str(tax))
        print ( "Net income is " + str (income - tax))
    elif income>=4001 and income <=7000:
        tax= income*0.20
        print("Total tax is " + str(tax))
        print ( "Net income is " + str (income - tax)) 
    elif income>=7001 and income <=10000:
        tax= income*0.25
        print("Total tax is " + str(tax))
        print ( "Net income is " + str (income - tax)) 
    elif income>=10001 and income <=14000:
        tax= income*0.30
        
        print("Total tax is " + str(tax))
        print ( "Net income is " + str (income - tax)) 
    else:
        tax= income*0.35
        print("Total tax is " + str(tax))
        print ( "Net income is " + str (income - tax)) 
tax_info (income)

        