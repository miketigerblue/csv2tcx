import csv
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Create the root element
root = Element('TrainingCenterDatabase')

# Read the CSV and populate the XML
with open('training_plan.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    for row in reader:
        week, day, workout, duration, distance, details, intensity, equipment, description, notes = row
        # Create Activity element
        activity = SubElement(root, 'Activity')

        # Create elements for each data point and add them to the Activity
        SubElement(activity, 'Week').text = week
        SubElement(activity, 'Day').text = day
        SubElement(activity, 'Workout').text = workout
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

