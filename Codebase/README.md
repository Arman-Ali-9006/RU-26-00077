# Classroom Timetable Generator

A simple Python project that generates a classroom timetable based on the number of days, periods per day, and the number of periods assigned to each subject.

## Project Overview

The **Classroom Timetable Generator** takes the subject names and their required weekly periods as input. It then arranges those periods across the available days while following the project's scheduling rules.

The program uses a backtracking approach to find a valid timetable. If the given requirements cannot be arranged, it displays an error message.

## Features

- Takes the number of working days as input.
- Takes the number of periods per day as input.
- Accepts multiple subjects and their required periods.
- Combines entries that have the same subject name.
- Checks that the total subject periods equal the total available timetable slots.
- Allows a maximum of **2 periods of the same subject per day**.
- Generates and displays the timetable day by day.
- Displays useful error messages for invalid or impossible input.

## Requirements

- Python 3.x
- No external Python packages are required.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the project file as `class_time_table.py`.
3. Open a terminal or Command Prompt in the folder containing the file.
4. Run:

   ```bash
   python class_time_table.py
   ```

   On some Windows systems, you may need to use:

   ```bash
   py class_time_table.py
   ```

5. Enter the requested information when prompted.

## Example

The following is an example of valid input:

```text
Enter number of days: 3
Enter periods per day: 3
Enter number of subjects: 3
Enter subject name: Programming
Enter periods for Programming: 3
Enter subject name: Maths
Enter periods for Maths: 3
Enter subject name: Chemistry
Enter periods for Chemistry: 3
```

One possible output is:

```text
Mon: Programming, Programming, Maths
Tue: Maths, Chemistry, Chemistry
Wed: Programming, Maths, Chemistry
```

The exact arrangement may vary, but the timetable must satisfy the scheduling rules.

## Scheduling Rules and Validation

The program checks the following conditions:

1. **Days and periods:** Both values must be positive integers.
2. **Number of subjects:** The number of subjects must be a positive integer.
3. **Subject name:** A subject name cannot be empty.
4. **Subject periods:** Each subject must have a positive integer number of periods.
5. **Total periods:** The sum of all subject periods must be equal to `number of days × periods per day`.
6. **Daily subject limit:** A subject cannot be scheduled more than twice on the same day.
7. **Possible arrangement:** If no timetable satisfies the rules, the program reports that a timetable cannot be generated with the given constraints.

If the same subject name is entered more than once, its period counts are added together.

## How It Works

1. The program collects the timetable details from the user.
2. It validates the subject names and period counts.
3. It calculates the total available slots and compares them with the required subject periods.
4. It tries to place subjects into the timetable while keeping each subject's daily count at 2 or less.
5. If a choice leads to a dead end, the backtracking process removes that choice and tries another subject.
6. Once a valid arrangement is found, the program prints the timetable.

## Main Functions

| Function | Purpose |
|---|---|
| `parse_subjects()` | Validates subject names and period counts, and combines repeated subject names. |
| `generate_timetable()` | Checks scheduling constraints and generates a valid timetable using backtracking. |
| `main()` | Takes user input, handles errors, calls the other functions, and displays the result. |

## Error Handling

The program displays an error message when:

- Days or periods per day are not valid positive integers.
- The number of subjects is not a positive integer.
- A subject name is empty.
- A subject's period count is not a positive integer.
- Total required periods do not match the available slots.
- A subject requires more than 2 periods per day on average under the project's daily limit.
- No valid timetable can be generated with the entered constraints.

## Project Structure

```text
Classroom-Timetable-Generator/
├── class_time_table.py
└── README.md
```

## Limitations

- The program uses fixed day labels (`Mon` to `Sat`) for the first six days. For additional days, it displays labels such as `Day 7`.
- Each subject is limited to two periods per day.
- The program generates a timetable based on subject period counts; it does not include teacher availability, classroom availability, holidays, or period-specific preferences.

## Future Improvements

- Allow users to enter custom day names.
- Add teacher and classroom allocation.
- Save the generated timetable to a text, CSV, or Excel file.
- Add a graphical user interface.
- Allow additional scheduling preferences.

## Author

Add your name, class, roll number, and college name here before submitting the project.
