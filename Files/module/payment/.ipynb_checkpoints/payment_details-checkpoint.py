import os, sys
from os.path import dirname, join, abspath

# Get the current directory (where this script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Insert the parent directory of the current directory into sys.path
sys.path.insert(0, abspath(join(current_dir, '..')))

# Importing course_details from the course module
from course import course_details

def payment():
    print("This is my payment details")

# Call the course function from course_details
course_details.course()
