# Function to calculate Bayes' Theorem
def bayes_theorem(P_A, P_B_given_A, P_B_given_not_A):
    # Calculate P(~A)
    P_not_A = 1 - P_A
    
    # Calculate the total probability of B using the law of total probability
    P_B = (P_B_given_A * P_A) + (P_B_given_not_A * P_not_A)
    
    # Calculate the posterior probability P(A|B) using Bayes' theorem
    P_A_given_B = (P_B_given_A * P_A) / P_B
    
    return P_A_given_B

# Taking user input for the probabilities
P_A = float(input("Enter the prior probability P(A) (e.g., probability of having a disease): "))
P_B_given_A = float(input("Enter the likelihood P(B|A) (e.g., probability of testing positive given the disease): "))
P_B_given_not_A = float(input("Enter the false positive rate P(B|~A) (e.g., probability of testing positive given no disease): "))

# Calculate the posterior probability P(A|B)
P_A_given_B = bayes_theorem(P_A, P_B_given_A, P_B_given_not_A)

# Output the result
print(f"The probability of having the disease given a positive test result is: {P_A_given_B:.4f}")
