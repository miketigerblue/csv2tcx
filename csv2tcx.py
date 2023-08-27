import csv
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from datetime import datetime, timedelta

# Function to calculate the date of the workout
def calculate_date(start_date, week, day):
    days_from_start = (int(week) - 1) * 7 + int(day) - 1
    return start_date + timedelta(days=days_from_start)

# Initialize start date
start_date = datetime(2023, 8, 28)

# Create the root element
root = Element('TrainingCenterDatabase')

# Read the CSV and populate the XML
with open('training_plan.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    for row in reader:
        week, day, workout, duration, distance, details, intensity, equipment, description, notes = row

        # Calculate the date for this workout
        workout_date = calculate_date(start_date, week, day)

        # Create Activity element
        activity = SubElement(root, 'Activity')

        # Create elements for each data point and add them to the Activity
        SubElement(activity, 'Date').text = workout_date.strftime('%Y-%m-%d')
        SubElement(activity, 'WorkoutName').text = f"{workout} - {workout_date.strftime('%Y-%m-%d')}"
        SubElement(activity, 'Duration').text = duration
        SubElement(activity, 'Distance').text = distance
        SubElement(activity, 'Details').text = details
        SubElement(activity, 'Intensity').text = intensity
        SubElement(activity, 'Equipment').text = equipment
        SubElement(activity, 'Description').text = description
        SubElement(activity, 'Notes').text = notes

# Create the XML file
tree = ElementTree(root)
with open('training_plan.tcx', 'wb') as f:
    tree.write(f)

