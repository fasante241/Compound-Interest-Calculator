# COMPOUND INTEREST CALCULATOR

# Compound Interest Formula Function
def compound_interest_calculator(principal, time, annual_rate, frequency):
    multiplier = pow((1 + (annual_rate/frequency)), ( time * frequency))  
    total_amount = round(principal * multiplier , 2)
    return total_amount
    

def compound_frequency(options):
    frequency = None
    if options == 1:
        frequency = 1        
        
    elif options == 2:
        frequency = 2
      
    elif options == 3:
        frequency = 4

    elif options == 4:
        frequency = 12

    elif options == 5:
       frequency = 365  
    return frequency
      
    

def menu():
    # COMPOUND INTEREST CALCULATOR
    # Take inputs for pricipal, time, rate and compound frequency

    print('COMPOUND INTEREST CALCULATOR')


    # Step 1: Principal
    principal = int(input('Enter your initial investment: '))


    # Step 2: Time
    time = float(input('Speicfy the length of time in years: '))

    # Step 3: Annual Interest Rate
    annual_rate = float(input('Enter your estimated interest rate: ')) / 100


    # Step 4: Compound Frequency
    print('''
    Compound Frequency:
        1. Annually
        2. Semiannually
        3. Quarterly
        4. Monthly
        5. Daily
    ''')

    options = int(input('Select from the options below how many times you want your investment to be compounded in a year: '))

    frequency = compound_frequency(options)
 
    if frequency == None:
        print('Wrong Selection')
    else:
        total = compound_interest_calculator(principal, time, annual_rate, frequency)
        print(f'In {int(time)} years, your Total Amount accrued will be ${total}.')

    
menu()


    
    

