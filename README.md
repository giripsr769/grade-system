 # Grade System

 A simple grade-management project for evaluating student marks and converting them into grades. This README documents the project purpose, grading rules, setup, usage, and suggested structure.

 ## Overview

 The Grade System accepts a student's marks, validates the input, calculates the result, and assigns a letter grade. It can be extended to support multiple subjects, grade-point averages, pass/fail status, and report generation.

 ## Features

 - Accepts marks for one or more subjects.
 - Validates that marks are numeric and within the `0–100` range.
 - Calculates total marks and percentage.
 - Assigns a letter grade.
 - Identifies pass or fail status.
 - Provides a clear, reusable foundation for future enhancements.

 ## Grading Scale

 | Percentage | Grade | Result |
 |------------|-------|--------|
 | 90–100     | A+    | Pass   |
 | 80–89      | A     | Pass   |
 | 70–79      | B     | Pass   |
 | 60–69      | C     | Pass   |
 | 50–59      | D     | Pass   |
 | 0–49       | F     | Fail   |

 > The grading scale can be adjusted to match the requirements of your institution.

 ## Requirements

 - A programming language runtime appropriate to the implementation.
 - A terminal or command prompt.
 - A code editor such as Visual Studio Code.

 ## Getting Started

 1. Open a terminal in the project directory:

	 ```text
	 cd "Week_1\Day-2\Assingment\grade-system"
	 ```

 2. Install any dependencies required by the implementation.
 3. Run the project's entry-point file using the command appropriate for its language.
 4. Enter valid marks when prompted and review the calculated result.

 ## Example

 ```text
 Enter marks: 86
 Percentage: 86%
 Grade: A
 Result: Pass
 ```

 ## Validation Rules

 - Empty input should be rejected.
 - Marks must be numeric.
 - Marks below `0` or above `100` are invalid.
 - Invalid input should display a helpful error message instead of producing an incorrect grade.

 ## Calculation

 For multiple subjects:

 ```text
 total marks = sum of subject marks
 maximum marks = number of subjects × 100
 percentage = (total marks / maximum marks) × 100
 ```

 The final grade is determined from the calculated percentage using the grading scale above.

 ## Suggested Project Structure

 ```text
 grade-system/
 ├── README.md          # Project documentation
 ├── src/                # Application source code
 ├── tests/              # Test cases
 └── package/config file # Runtime-specific configuration
 ```

 ## Testing Checklist

 Test the application with:

 - `100` and `90` to verify the highest grade boundary.
 - `89`, `79`, `69`, and `59` to verify grade transitions.
 - `0` and `49` to verify failing scores.
 - Negative values and values above `100`.
 - Empty, text, decimal, and unexpected input.

 ## Future Enhancements

 - Add student names and IDs.
 - Support weighted subjects and credit hours.
 - Calculate GPA or CGPA.
 - Store and retrieve student records.
 - Export results as CSV or PDF.
 - Add a graphical or web-based interface.

 ## Contributing

 1. Create a feature branch.
 2. Make focused changes.
 3. Add or update tests.
 4. Document user-visible changes.
 5. Submit a pull request for review.

 ## License

 No license has been specified yet. Add a license file before distributing or reusing this project.
