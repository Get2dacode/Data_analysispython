#importing the neccessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#creating our candy varaible to copy our panda read csv file
candy = pd.read_csv('candy.csv')
#gathering sample data and info
print(candy.head(),candy.info())
#setting our grid style
sns.set_style('whitegrid')
#creating a regression scatter plot
sns.lmplot(x='sugarpercent' , y = 'pricepercent' , hue = 'chocolate', data = candy)
plt.title('Chocolate v Non-Chocolate candy')
plt.show()
sns.set_style('darkgrid')
# creating a scatter categorical plot
sns.swarmplot(x=candy.chocolate,y=candy.pricepercent)
plt.title('chocolate candy is more expensive than non-chocolate candy')
plt.show()
