# Who needs an IDE when you have Neovim, for ease of use 
# run in Terminal in same dir as file is in `python assignment14.py`

# Assignment 14: Loan Qualification Program

# This program determines whether a customer qualifies for a loan
# based on their annual income and years at their current job.

# Define the function that checks qualification criteria
def loan_qualification(income, years_on_job):
    # Check if both conditions are met: income >= 30000 and years_on_job >= 2
    if income >= 30000 and years_on_job >= 2:
        print("Congratulations! You qualify for the loan.")
    else:
        print("Sorry, you do not qualify for the loan.")

# Define the main function where the program starts
def main():
    # Prompt the user for their annual income
    income = float(input("Enter your annual income: $"))

    # Prompt the user for the number of years at their current job
    years_on_job = float(input("Enter the number of years at your current job: "))

    # Call the loan_qualification function with the user inputs
    loan_qualification(income, years_on_job)

# Call the main function to execute the program
main()

#Github: gnotree, https://github.com/gnotree
