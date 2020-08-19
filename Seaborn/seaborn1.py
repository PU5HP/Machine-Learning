import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
print(tips.head())
sns.barplot(x='sex',y='total_bill',data=tips)
plt.show()

titanic =sns.load_dataset('titanic')
print(titanic.columns)
sns.barplot(x='sex',y='survived',data=titanic)
plt.show()

sns.countplot(x='survived',data=titanic)
plt.show()

sns.countplot(x='embark_town',data=titanic)
plt.show()

sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()

sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')
plt.show()


sns.violinplot(x='day',y='total_bill',data=tips)
plt.show()

sns.violinplot(x='day',y='total_bill',data=tips,hue='smoker')
plt.show()

#DISTRIBUTION PLOT
sns.distplot(tips['total_bill'])
plt.show()

sns.distplot(tips['total_bill'],kde=False)
plt.show()

#KDE GRAPH
sns.kdeplot(tips['total_bill'])
plt.show()

#JOINT PLOt
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
plt.show()

#pair plot 
sns.pairplot(tips)
plt.show()

sns.pairplot(tips,hue='sex')
plt.show()

#CORRELATION AND THE HEAT MAP
tips_cor = tips.corr()
print(tips_cor)

#HEAT-MAP
sns.heatmap(tips_cor,annot=True)
plt.show()