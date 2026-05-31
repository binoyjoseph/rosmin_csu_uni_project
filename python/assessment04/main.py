"""
Parking Data Analysis Program
Loads parking records from a text file (plate, date, check_in, check_out, spot, fee)
and provides data analysis through a menu-driven interface 
1. Licence Plate History: Search for a licence plate and display all associated parking records.
2. Peak Hours Analysis: Identify the peak hours for parking based on the total number of parked vehicles.
3. Daily Revenue: Display the total revenue generated on a specific date entered by the user.
4. Average Stay Duration: Calculate and display the average stay duration of all parked vehicles for each date in the dataset.
Author: Rosmin Mary Roy
"""

import operator

# Record format constants
EXPECTED_FIELDS = 6        # number of fields per record
DELIMITER = "|"            # field separator
PLATE_MIN_LEN = 2          # minimum licence plate length
PLATE_MAX_LEN = 6          # maximum licence plate length
PLATE_PREFIX = "Z"         # all licence plates start with this letter
SPOT_MIN_LEN = 2           # one letter + 1 digit
SPOT_MAX_LEN = 3           # one letter + 2 digits

# Tuple indices for a parsed record (plate, date, check_in, check_out, spot, fee)
IDX_PLATE = 0
IDX_DATE = 1
IDX_CHECKIN = 2
IDX_CHECKOUT = 3
IDX_SPOT = 4
IDX_FEE = 5

def is_valid_plate(plate):
    """Return True if plate is 2-6 alphanumeric characters starting with Z."""
    if len(plate) < PLATE_MIN_LEN or len(plate) > PLATE_MAX_LEN:
        return False
    if not plate.startswith(PLATE_PREFIX):
        return False
    # isalnum() ensures only letters and digits (no spaces or symbols)
    return plate.isalnum()


def is_valid_date(date_str):
    """Return True if date_str matches yyyy/mm/dd with valid ranges."""
    # Split the date string by "/" and check that we get exactly 3 parts (year, month, day)
    parts = date_str.split("/")
    if len(parts) != 3:
        return False
    year_str, month_str, day_str = parts
    # Check that year is 4 digits, month and day are 2 digits, and all are numeric
    if len(year_str) != 4 or len(month_str) != 2 or len(day_str) != 2:
        return False
    if not (year_str.isdigit() and month_str.isdigit() and day_str.isdigit()):
        return False
    month = int(month_str)
    day = int(day_str)
    # Check that month is between 1 and 12 and day is between 1 and 31
    if month < 1 or month > 12:
        return False
    # Note: This does not check for the correct number of days in each month
    if day < 1 or day > 31:
        return False
    return True


def is_valid_time(time_str):
    """Return True if time_str is a 4-digit HHMM value in 0000-2359."""
    if len(time_str) != 4 or not time_str.isdigit():
        return False
    value = int(time_str)
    hour = value // 100
    minute = value % 100
    # Check that hour is between 0 and 23 and minute is between 0 and 59
    if hour < 0 or hour > 23:
        return False
    if minute < 0 or minute > 59:
        return False
    return True


def is_valid_spot(spot):
    """Return True if spot is one letter followed by one or two digits."""
    if len(spot) < SPOT_MIN_LEN or len(spot) > SPOT_MAX_LEN:
        return False
    # The first character must be a letter and the rest must be digits
    if not spot[0].isalpha():
        return False
    return spot[1:].isdigit()


def is_valid_fee(fee_str):
    """Return True if fee_str represents a non-negative whole number."""
    return fee_str.isdigit()


def time_to_minutes(hhmm):
    """Convert an HHMM integer to total minutes since midnight."""
    # hhmm // 100 gives the hour part, hhmm % 100 gives the minute part
    # Multiply the hour part by 60 and add the minute part to get total minutes
    return 60 * (hhmm // 100) + (hhmm % 100)


def parse_record(line):
    """
    Parse one line from the dataset file.
    Returns a tuple (plate, date, check_in, check_out, spot, fee) on success,
    or None if the line is blank or does not match the required format.
    """
    line = line.strip()
    # Reject blank lines silently
    if line == "":
        return None
    parts = line.split(DELIMITER)
    if len(parts) != EXPECTED_FIELDS:
        return None

    # Strip whitespace from each field and assign to variables for validation
    plate = parts[IDX_PLATE].strip()
    date = parts[IDX_DATE].strip()
    check_in = parts[IDX_CHECKIN].strip()
    check_out = parts[IDX_CHECKOUT].strip()
    spot = parts[IDX_SPOT].strip()
    fee = parts[IDX_FEE].strip()

    # Validate every field individually; reject the whole record on any failure
    if not is_valid_plate(plate):
        return None
    if not is_valid_date(date):
        return None
    if not is_valid_time(check_in):
        return None
    if not is_valid_time(check_out):
        return None
    if not is_valid_spot(spot):
        return None
    if not is_valid_fee(fee):
        return None

    return (plate, date, int(check_in), int(check_out), spot, int(fee))


def load_data(file_name):
    """
    Open the file and return (records, invalid_count). Lets the caller catch
    FileNotFoundError / OSError so file-name errors can be reported.
    """
    # The data structure for records is a list of tuples
    records = []
    invalid_count = 0
    file = open(file_name, "r")
    try:
        for line in file:
            # Skip blank lines silently; count malformed non-blank lines
            if line.strip() == "":
                continue
            # The data structure for a record is a tuple because the fields are fixed and we want immutability
            record = parse_record(line)
            if record is None:
                invalid_count += 1
            else:
                records.append(record)
    finally:
        file.close()
    return records, invalid_count


def prompt_dataset():
    """Repeatedly prompt for a dataset file name until it is a valid file"""
    while True:
        file_name = safe_input(">> Enter dataset filename: ").strip()
        if file_name == "":
            print("** Please enter a non-empty file name.")
            continue
        try:
            records, invalid_count = load_data(file_name)
        except FileNotFoundError:
            print(f"** Error: File not found.")
            continue
        except OSError:
            print(f"** Error: Could not open file.")
            continue

        print(f" Loaded {len(records)} record(s) "
              f"from {file_name}.")
        if invalid_count > 0:
            print(f"** Skipped {invalid_count} invalid record(s) in the file.")
        return records


def safe_input(prompt):
    """Wrap input() so EOF returns the exit code rather than crashing."""
    try:
        # Program must not crash, regardless of the user input.
        return input(prompt)
    except (EOFError):
        # Treat unexpected EOF as a request to exit the program gracefully
        print()
        return 5  # The exit code for the menu loop

def display_records(records):
    """Print parking records in a formatted table."""
    print(f"License-Plate\tDate\t\tCheck-In\tCheck-Out\tSpot ID\tFee")
    print(f"---------------------------------------------------------------------------")
    for record in records:
        plate, date, check_in, check_out, spot, fee = record
        print(f"{plate:<13}\t{date}\t{check_in:04d}\t\t{check_out:04d}\t\t{spot:<3}\t${fee}")


def licence_plate_history(records):
    """Menu option 1: list all records belonging to a given licence plate."""

    # First show the user all available licence plates in sorted order
    print("Available licence plates:", end=" ")
    sorted_plates = sorted(set(record[IDX_PLATE] for record in records))
    print(", ".join(sorted_plates))
    print()
    
    plate = safe_input(">> Enter licence plate: (press enter to show all records): ").strip().upper()
    if plate == "":
        print()
        display_records(records)
        return
    
    matches = []
    for record in records:
        if record[IDX_PLATE] == plate:
            matches.append(record)

    if len(matches) == 0:
        print(f"No records found for this licence plate.")
        return

    # Sort by date then check-in time
    matches.sort(key=operator.itemgetter(IDX_DATE, IDX_CHECKIN))
    display_records(matches)


def peak_hours_analysis(records):
    """
    Menu option 2: count how many vehicles checked in during each hour of the day across all records
    and display the hours sorted by count in descending order.
    """
    if len(records) == 0:
        print("No records available to analyse.")
        return

    # Create a list of 24 integers initialized to zero to count the number of parked vehicles for each hour (0-23)
    hour_counts = [0] * 24  # Initialize counts for each hour to zero
    for record in records:
        # Get the hour part of the check-in time with integer division by 100 (e.g., 0830 // 100 = 8)
        checkin_hour = record[IDX_CHECKIN] // 100
        # Increment the count for each hour in that range
        hour_counts[checkin_hour] += 1
    
    # Build a dictionary of check-in hours and their counts
    # This will allow us to display only the hours that are relevant (those with count > 0)
    checkin_hours_count = {}
    for hour, count in enumerate(hour_counts):
        if count > 0:
            checkin_hours_count[hour] = count

    # This will also allow us to sort by count in descending order while keeping the hour as the key for display
    checkin_hours_count = sorted(checkin_hours_count.items(), key=operator.itemgetter(1), reverse=True)

    print("\nCheck-In Hour\tCount")
    print("-----------------------")
    for hour, count in checkin_hours_count:
        print(f"  {hour}\t\t{count}")


def daily_revenue(records):
    """Menu option 3: display total fees collected on the entered date."""
    
    # Create a list of all unique dates in the dataset to help the user choose a valid date
    # and assign a number to each date for easier selection.
    dates = sorted(set(record[IDX_DATE] for record in records))

    # Build a dictionary mapping selection numbers to dates for easy lookup after user input
    # Each dictionary item is key:value pairs like "1":"2024/01/15", "2":"2024/01/16", etc.
    # The key is the string of the number (e.g., "1") and the value is the corresponding date (e.g., "2024/01/15")
    # enumerate(dates) generates pairs of (index, date) for each date in the sorted list of unique dates
    numbered_dates = {str(i + 1): date for i, date in enumerate(dates)}
    
    print("\nAvailable dates for revenue analysis:")
    for number, date in numbered_dates.items():
        print(f"  {number}. {date}")

    # Prompt the user to select a date by number
    # Lookup numbered_dates to get the date for the selected number
    number = safe_input(">> Select a date by number: ").strip()
    if number not in numbered_dates:
        print("** Invalid selection.")
        return
    date = numbered_dates[number]

    # Calculate total fees for the selected date by iterating through all records 
    # and summing the fees for records that match the date
    total_fee = 0
    count = 0
    for record in records:
        if record[IDX_DATE] == date:
            total_fee += record[IDX_FEE]
            count += 1

    if count == 0:
        print(f"No records found for {date}.")
        return
    print(f"\nTotal revenue for {date}: ${total_fee} ")


def average_stay_duration(records):
    """
    Menu option 4: compute and display the average stay duration of all
    parked vehicles for each date present in the dataset.
    """
    if len(records) == 0:
        print("No records available to analyse.")
        return

    # Calculate total stay minutes and count of records for each date by iterating through all records
    minutes_by_date = {}
    counts_by_date = {}
    for record in records:
        date = record[IDX_DATE]
        # Difference in minutes between check-in and check-out times for this record
        duration = (time_to_minutes(record[IDX_CHECKOUT])
                    - time_to_minutes(record[IDX_CHECKIN]))
        
        # Update the total minutes and count for this date in the dictionaries
        if date in minutes_by_date:
            minutes_by_date[date] += duration
            counts_by_date[date] += 1
        # If this is the first record for this date, initialize the total minutes and count
        else:
            minutes_by_date[date] = duration
            counts_by_date[date] = 1

    # Build a list of (date, average_minutes) tuples and sort chronologically
    summary = []
    for date in minutes_by_date:
        average = minutes_by_date[date] // counts_by_date[date]
        summary.append((date, average))
    summary.sort(key=operator.itemgetter(0))

    # Display results as a table with date and average stay duration in hours and minutes
    print("\nDate\t\tAverage stay duration (hour:minute)")
    print("--------------------------------------------------")
    for date, average_minutes in summary:
        # Convert total minutes into hours, minutes format for display
        # divmod returns quotient and remainder
        hours, minutes = divmod(average_minutes, 60)
        print(f"  {date}\t{hours}:{minutes:02d}")


def display_menu():
    """Print the main menu options."""
    print("\nParking Data Analysis")
    print("---------------------------") 
    print(" 1. Licence Plate History")
    print(" 2. Peak Hours Analysis")
    print(" 3. Daily Revenue")
    print(" 4. Average Stay Duration")
    print(" 5. Exit")


def run_menu(records):
    """Run the interactive menu loop until the user chooses to exit."""
    while True:
        display_menu()
        choice = safe_input(">> Enter your choice: ").strip()
        if choice == "1":
            licence_plate_history(records)
        elif choice == "2":
            peak_hours_analysis(records)
        elif choice == "3":
            daily_revenue(records)
        elif choice == "4":
            average_stay_duration(records)
        elif choice == "5":
            print("\nExiting program.")
            break
        else:
            print("** Invalid choice. Please enter a number between 1 and 5.")


def main():
    """Main function to load the dataset and start the menu loop."""
    print("Welcome to the Parking Data Analysis Program!\n")
    try:
        records = prompt_dataset()
        run_menu(records)
    except KeyboardInterrupt:
        # Ctrl+C should not produce a stack trace but should exit gracefully
        print("\nExiting program.")


main()