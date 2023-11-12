""" 
    Part C: Finding the right amount to save away
    ouput : how much should a user save for each month
"""
def calculate_savings(**kwargs): 
    """ 
    kwargs = {
                r,
                annual_salary,
                semi_annula_raise,
                portion_saved
            }
    """

    # parameter destructuring using key words arguments 
    r = kwargs.get('r')
    annual_salary = kwargs.get('annual_salary')
    semi_annual_raise = kwargs.get('semi_annual_raise')
    portion_saved = kwargs.get('portion_saved')

    current_savings = 0


    for i in range(1, 37) : 
        monthly_salary =  annual_salary / 12
        if i % 6 == 0: 
            annual_salary *= 1 + semi_annual_raise

        current_savings += current_savings * (r / 12)

        current_savings += monthly_salary * portion_saved

    # 150000
    return current_savings

    
def main() : 

    # initial variables
    portion_down_payment = 0.25
    r = 0.04
    semi_annual_raise = 0.07
    total_cost = 1_000_000

    # first payment 
    down_payment = portion_down_payment * total_cost

    # annual salary
    annual_salary = float(input('Enter your annual salary : '))
    
    current_savings = 0


    # binary search method
    lower_bound = 0
    upper_bound = 10000
    epsilon = 100
    bisection_counter = 0

    # portion saved 
    # 1 is because i want to save all my monthly salary wich lead to the fastes time for a down pyment 
    portion_saved = 1 

    # months saving is a variable that contain savings fro 36 months 
    months_saving = calculate_savings(
        r = r, 
        annual_salary = annual_salary, 
        semi_annual_raise = semi_annual_raise, 
        portion_saved = portion_saved
    )

    if months_saving < down_payment - epsilon :
        print('It is imposible to pay the the down payment in three years.')
        return 
    
    # binary search implementation
    while abs(current_savings - down_payment) >= epsilon : 

        bisection_counter += 1
        mid_bound = int(upper_bound + lower_bound) // 2  # mid point 

        portion_saved = mid_bound / 10000.0 # convert the mid bound to a value from 0 to 1 

        current_savings = calculate_savings(
                            r = r, 
                            annual_salary = annual_salary, 
                            semi_annual_raise = semi_annual_raise, 
                            portion_saved = portion_saved
                        )
        
        if current_savings > down_payment + epsilon : 
            upper_bound = mid_bound
        
        elif current_savings < down_payment - epsilon : 
            lower_bound = mid_bound
        else : 
            break



    print(f'Best savings rate : {portion_saved}')
    print(f'bisection steps is : {bisection_counter}')




if __name__ == '__main__' : 
    main()