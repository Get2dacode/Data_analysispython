import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

insurance_data = pd.read_csv('insurance.csv')
#getting a view of the first 5 rows
print(insurance_data.head())
#creating a scatterplot for analysis
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
plt.title('Does a higher bmi mean higher insurance charges')
plt.show()
#creating a regression line to check the strength of the relationship
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
plt.title('Does a higher bmi mean higher insurance charges')
plt.show()
#adding color to make our scatterplot better for visualization
plt.title('Do smokers with a high bmi have higher insurance charges')
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
plt.show()
#adding two regression lines, corresponding to smokers and nonsmokers
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
plt.title('Do smokers with a high bmi have higher insurance charges')
plt.show()
#categorical plot for the chargess of  smoker v non
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])
plt.title('Smoker v Nonsmoker charge relationship')
plt.show()
