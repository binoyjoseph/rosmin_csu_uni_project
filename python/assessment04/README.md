# Assessment item 4 - Files and Data Structures

In this assessment, you will perform some exploratory data analysis on a dataset collected from parking sites.

The dataset is a plain text file that contains parking records with the following columns:
- Licence Plate (2-6 combination of letters and digits starting with Z)
- Date (yyyy/mm/dd)
- Check-In Time (HHMM)
- Check-Out Time (HHMM)
- Parking Spot ID (one letter followed by one or two digits)
- Parking Fee Paid (whole number)

Each record is stored on a separate line, and columns are separated by the vertical bar | character.
Example record: `ZA12BC|2025/04/15|1525|1820|B5|79`

A sample dataset will be available in the subject site. As explained in Task 2, you are expected to create additional modified datasets for testing.

As your program starts, it should prompt the user for the dataset file name and load its data into memory in appropriate data structures. Your program will then present a main menu with the following options:

1. Licence Plate History: Search for a licence plate and display all associated parking records.
2. Peak Hours Analysis: Identify the peak hours for parking based on the total number of parked vehicles.
3. Daily Revenue: Display the total revenue generated on a specific date entered by the user.
4. Average Stay Duration: Calculate and display the average stay duration of all parked vehicles for each date in the dataset.
5. Exit the Program.

The details of how the system should work are provided in the sample run video, which will be available in the subject site. Review the sample run to clearly understand all the requirements.

Your program must handle invalid inputs gracefully. At a minimum, it should manage the following situations:
- Incorrect file names
- Incorrect record formats (skip invalid records)
- Invalid menu options or sub-menu selections
In addition, your program must not crash, regardless of the user input.

### Constraints
In addition to your own modules (if any), you can only import the operator library module (see the sample codes below).

### Sample Codes
The following sample codes can be useful for your assessment. Adapt them to your specific needs.

1. Suppose we have a list of tuples such as

```
staff_age = [('Peter', 25), ('Sam', 21), ('Kathie', 34), ('Helen', 23)]
```

In order to sort this list by the age of staff members, use code below

```
import operator
staff_age.sort(key=operator.itemgetter(1)) # since age is at index 1 in each tuple
```

Refer to the operator module documentation (https://docs.python.org/3/library/operator.html) for more details.

2. Get the hour value from HHMM timestamp

```
timestamp = 1450
timestamp_hour = timestamp // 100
```

3. Get the minute value from HHMM timestamp

```
timestamp = 1450
timestamp_minute = timestamp % 100
```

4. Calculate difference in minutes between two HHMM timestamps

```
from_timestamp = 1450
till_timestamp = 1720
from_minutes = 60 * (from_timestamp // 100) + from_timestamp % 100
till_minutes = 60 * (till_timestamp // 100) + till_timestamp % 100
difference_minutes = till_minutes - from_minutes
```

5. Convert total minutes into hours, minutes

```
total_minutes = 150
hours, minutes = divmod(total_minutes, 60)
```

### Tasks

Your assessment should consist of the following tasks:

#### Task 1 (30 marks)
Implement your program in Python. Comment on your code as necessary to explain it clearly. You should follow good programming practices, for example using named constants, creating several reusable functions (top-down design) and minimising the use of global variables.
- Code includes function header comments.
- Named constants are used instead of magic numbers.
- Avoids unnecessary global variables.
- All variables have meaningful names.
- Sufficient inline comments are present.
- Use docstrings for comments.

#### Task 2 (10 marks)
Perform black-box testing of your program and document it in tabular form as follows. The minimum number of test cases is ten (10) tests cases. To ensure comprehensive testing, provide more test cases than the required minimum.
A lot of input going in to this program is through dataset text file. Therefore, for some test cases you would create additional dataset files with modified data. Include all of those files in your submission so that marker can verify your test cases.

| Test data | Reason it was selected | Expected output | Screenshot of actual output |
|-----------|------------------------|-----------------|-----------------------------|
| -         | -                      | -               | -                           |


Your submission will consist of:
1. Source code of your Python implementation (*.py)
2. Alternate dataset files used for test cases. Name them test1.txt, test2.txt and so on
(referring to test # in the table).
3. The table recording your chosen test data and results (it should be a PDF file).

It is critically important that your test runs are unmodified outputs from your program, and that these results should be reproducible by the marker running your saved .py python program.

- Test data explores every branch of the program.
- To demonstrate comprehensive testing, number of test cases exceeds the required minimum. 
- Sound justification is provided for the selection of test data.
- Diversity is evident among the chosen test data.

### RATIONALE
This assessment task will assess the following learning outcome/s:
- Demonstrate and explain elements of good programming style.
- Identify, isolate and correct errors in all phases of the programming process.
- Interpret algorithms and program code.
- Apply sound program analysis, design, coding, debugging, testing and documentation techniques for simple programming problems.
- Write code in an appropriate coding language.