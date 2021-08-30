import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")
# Read the file into a variable spotify_data
spotify_data = pd.read_csv('spotify.csv', index_col="Date", parse_dates=True)
# Print the first 5 rows of the data
spotify_data.head()
# Print the last five rows of the data
spotify_data.tail()
sns.set_style("dark")

# Line chart showing daily global streams of each song
sns.lineplot(data=spotify_data)
# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
plt.ylabel('Streams')

plt.show()
# Set the width and height of the figure
plt.figure(figsize=(14,6))
list(spotify_data.columns)

# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")

# Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")
plt.title("Daily Global Streams for Shape of You vs Despacito in 2017-2018")
# Add label for horizontal axis
plt.xlabel("Date")
# Add label for vertical axis
plt.ylabel('Streams')
plt.show()
