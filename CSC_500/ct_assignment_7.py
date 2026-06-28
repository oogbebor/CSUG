# Step 1: Data Specifications

# Create three separate dictionaries to store the following data. In each dictionary, the Course Number must serve as the Key.

# Store Data
#
# | Course Number (key) | Room Number (value) | Instructor (value) |
# | ------------------- | ------------------- | ------------------ |
# | CSC101              | 3004                | Haynes             |
# | CSC102              | 4501                | Alvarado           |
# | CSC103              | 6755                | Rich               |
# | NET110              | 1244                | Burke              |
# | COM241              | 1411                | Lee                |

# Three separate dictionaries, each keyed by the Course Number.
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

meeting_times = {
    "CSC101": "9.00AM",
    "CSC102": "11.30AM",
    "CSC103": "12.45PM",
    "NET110": "2.00PM",
    "COM241": "3.30PM",
}

# Step 2: Program Logic

# Input: Prompt the user to enter a Course Number (e.g., CSC101).
# Output: Display the Room Number, Instructor, and Meeting Time. If the course does not exist, provide a friendly error message.

course_number = input("Enter a Course Number (e.g., CSC101): ").strip().upper()

# Look up the course in each dictionary. Accessing a missing key raises a
# KeyError, which shows a friendly error message.
try:
    print(f"Course Number: {course_number}")
    print(f"Room Number:   {room_numbers[course_number]}")
    print(f"Instructor:    {instructors[course_number]}")
    print(f"Meeting Time:  {meeting_times[course_number]}")
except KeyError:
    print(f"Sorry, '{course_number}' is not a valid course number. Please try again.")

