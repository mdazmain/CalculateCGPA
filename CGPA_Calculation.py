
def calculate_cgpa():
    # Title of the program
    print("=== CGPA Calculation for the Students of the Department of Chemistry, HSTU ===\n")
    
    # Credits for each semester (as per your table)
    credits = [18.5, 16.5, 19.5, 20.5, 21.5, 20.5, 21.5, 18.5]
    total_credits = sum(credits)

    # Prompt the user to input CGPA for all 8 semesters with updated titles
    print("Enter the CGPA for each semester (valid range: 2.00 to 4.00):")
    semester_cgpa = []
    semesters = [
        "LEVEL-1 SEMESTER-I EXAMINATION",
        "LEVEL-1 SEMESTER-II EXAMINATION",
        "LEVEL-2 SEMESTER-I EXAMINATION",
        "LEVEL-2 SEMESTER-II EXAMINATION",
        "LEVEL-3 SEMESTER-I EXAMINATION",
        "LEVEL-3 SEMESTER-II EXAMINATION",
        "LEVEL-4 SEMESTER-I EXAMINATION",
        "LEVEL-4 SEMESTER-II EXAMINATION"
    ]
    
    for i in range(8):
        try:
            cgpa = float(input(f"{semesters[i]} CGPA: "))
            if 2.00 <= cgpa <= 4.00:
                semester_cgpa.append(cgpa)
            else:
                print(f"Error: CGPA must be between 2.00 and 4.00. Invalid value entered: {cgpa}")
                return  # Exit the program
        except ValueError:
            print("Error: Invalid input. Please enter a valid number between 2.00 and 4.00.")
            return  # Exit the program

    # Calculate weighted grade points
    weighted_grade_points = [cgpa * credit for cgpa, credit in zip(semester_cgpa, credits)]
    total_weighted_grade_points = sum(weighted_grade_points)

    # Calculate overall CGPA
    overall_cgpa = total_weighted_grade_points / total_credits

    # Determine the class of result
    if 3.00 <= overall_cgpa <= 4.00:
        result_class = "First Class"
    elif 2.25 <= overall_cgpa < 3.00:
        result_class = "Second Class"
    elif 2.00 <= overall_cgpa < 2.25:
        result_class = "Third Class"
    else:
        result_class = "Failed"

    # Print the result
    print("\n=== CGPA Calculation Result ===")
    print(f"Total Credits: {total_credits}")
    print(f"Your Overall CGPA: \033[1m{overall_cgpa:.2f}\033[0m")  # Bold text for CGPA
    print(f"Class of Result: {result_class}")


# Run the function
calculate_cgpa()
