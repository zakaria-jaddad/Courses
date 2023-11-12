# part A 

""" 
    i have a bit of knowledge in coding :)
"""

def main() : 
    annual_salary = int(input('Enter your annual salary : '))
    portion_saved = float(input('Enter the percent of your salary to save, as a decimal : '))
    total_cost = int(input('Enter the cost of your dream home : '))
    semi_annula_raise = float(input('Enter a semi annual raise : '))


    monthly_sallary = annual_salary / 12
    
    portion_down_payment = 0.25 * total_cost

    r = 0.04

    # current saving will be incremented every month by this formula (( current_savings * r / 12 ))
    current_savings = 0
    
    # number of months 
    number_of_months = 0

    while current_savings < portion_down_payment : 

        if number_of_months % 6 == 0 and number_of_months != 0: 
            monthly_sallary += monthly_sallary * semi_annula_raise
        
        current_savings += current_savings * (r / 12)
        
        current_savings += monthly_sallary * portion_saved

        number_of_months += 1




    print(number_of_months)

    # semmi annual salary
    # semi_annual_raise = float(input('Enter You\'re semi annual raise : '))




if __name__ == '__main__' : 
    main()