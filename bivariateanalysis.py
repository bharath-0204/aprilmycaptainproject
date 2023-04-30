import matplotlib.pyplot as plt

# Sample productivity data
productivity_data = {
    "6:00 AM": 2,
    "7:00 AM": 3,
    "8:00 AM": 4,
    "9:00 AM": 5,
    "10:00 AM": 5,
    "11:00 AM": 4,
    "12:00 PM": 3,
    "1:00 PM": 2,
    "2:00 PM": 3,
    "3:00 PM": 3,
    "4:00 PM": 4,
    "5:00 PM": 5,
    "6:00 PM": 4,
    "7:00 PM": 3,
    "8:00 PM": 2,
    "9:00 PM": 1,
    "10:00 PM": 1,
    "11:00 PM": 1,
    "12:00 AM": 1,
    "1:00 AM": 1,
    "2:00 AM": 1,
    "3:00 AM": 1,
    "4:00 AM": 1,
    "5:00 AM": 2
}

# Create two lists from the productivity data: time of day and productivity level
time_of_day = list(productivity_data.keys())
productivity_level = list(productivity_data.values())

# Create a bar chart
plt.bar(time_of_day, productivity_level)

# Set the title and axis labels
plt.title("Productivity level vs. time of day")
plt.xlabel("Time of day")
plt.ylabel("Productivity level")

# Display the chart
plt.show()
