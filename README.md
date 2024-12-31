
# CGPA Calculation Program

## Description

This is a Python project designed to calculate the **Cumulative Grade Point Average (CGPA)** for students of the Department of Chemistry, HSTU. The program takes input for CGPAs of eight semesters and computes the overall CGPA. It also determines the class of the result based on the overall CGPA.

### Features:
- Calculates CGPA based on individual semester CGPAs and their respective credit hours.
- Validates user input to ensure CGPAs are in the range of 2.00 to 4.00.
- Provides the class of result based on the calculated CGPA:
  - **First Class**: 3.00 to 4.00
  - **Second Class**: 2.25 to 2.99
  - **Third Class**: 2.00 to 2.24
- Displays errors for invalid inputs.

## How to Run

1. Make sure you have Python 3 installed on your system.
2. Download the `CGPA_Calculation.py` file from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory where the `CGPA_Calculation.py` file is located.
5. Run the program using the following command:
   ```bash
   python CGPA_Calculation.py
   ```
6. Follow the prompts to enter the CGPA for each semester.

## Example Input and Output

### Input:
```
LEVEL-1 SEMESTER-I EXAMINATION CGPA: 3.50
LEVEL-1 SEMESTER-II EXAMINATION CGPA: 3.70
LEVEL-2 SEMESTER-I EXAMINATION CGPA: 3.80
LEVEL-2 SEMESTER-II EXAMINATION CGPA: 3.60
LEVEL-3 SEMESTER-I EXAMINATION CGPA: 3.40
LEVEL-3 SEMESTER-II EXAMINATION CGPA: 3.50
LEVEL-4 SEMESTER-I EXAMINATION CGPA: 3.90
LEVEL-4 SEMESTER-II EXAMINATION CGPA: 3.80
```

### Output:
```
=== CGPA Calculation Result ===
Total Credits: 157.0
Your Overall CGPA: 3.65
Class of Result: First Class
```

## Input Validation

- If any CGPA is entered outside the range of 2.00 to 4.00, the program will display an error message and terminate.

### Example:
#### Input:
```
LEVEL-1 SEMESTER-I EXAMINATION CGPA: 4.5
```
#### Output:
```
Error: CGPA must be between 2.00 and 4.00. Invalid value entered: 4.5
```

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

**Happy Coding!**
