import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")
Month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
flight_data = pd.read_csv('flight_delays.csv', index_col="Month")
# Print the data
print(flight_data)
# Set the width and height of the figure
plt.figure(figsize=(10,6))
# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=Month, y=flight_data.NK)
# Add label for vertical axis
plt.ylabel("Arrival delays (in minutes)")
plt.show()
# Set the width and height of the figure
plt.figure(figsize=(14,7))
# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")
# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)
# Add label for horizontal axis
plt.xlabel("Airlines")
plt.show()
