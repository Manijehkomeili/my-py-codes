import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
np.set_printoptions(suppress=True)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

train = pd.read_csv('C:/Users/Mojtaba/Desktop/Titanic-Kaggle-main/Data/train.csv')
# print(train.head())
print(f'This dataset has {train.shape[0]} rows and {train.shape[1]} features.')
train.describe(include='all')
Survived_cls_Fare = train.groupby('Survived').mean().drop(['PassengerId', 'SibSp', 'Parch', 'Age'], axis=1)
print('-------------------------------------------------------------------------------------\n'
      'survived or not survived classification based on the average of their Fares\n'
      'this is clear that the most people with higher class ticket survived')

print(Survived_cls_Fare)
print('-------------------------------------------------------------------------------------\n'
      'survived or not survived classification based on the gender \n'
      'this is clear that the most of females survived ')
Survived_cls_sex = train.groupby('Sex').mean().drop(['PassengerId', 'SibSp', 'Parch', 'Age'], axis=1)
print(Survived_cls_sex)
print('-------------------------------------------------------------------------------------\n'
      'Now its time to clean the data.\n'
      'First we need to find missing values in dataset')

null_records = train.isnull().sum()
print(null_records)
print('there are 177 records with missing age, and \n '
      '\t\t   2 records with missing embarked feature, and\n '
      '\t\t   687 rows with missing values in "Cabin" feature.')

outliers = train['Fare'][train['Fare'] > train['Fare'].quantile(.99)]
print(outliers)
print('512.33 is detected as outliers so I changed it to the second most value in Fare feature (263)')
train.loc[[258, 679, 737], 'Fare'] = 263

# data visualizations

fig, axes = plt.subplots(2, 3, figsize=(24, 18))

sns.histplot(data=train, x='Survived', bins=2, shrink=.8, ax=axes[0, 0], discrete=True, hue='Survived',
             palette="coolwarm")
axes[0, 0].set_title('Survived distribution')
axes[0, 0].set_xlabel('Survived')
axes[0, 0].set_xticks([0, 1])

sns.histplot(data=train, x='Pclass', bins=3, shrink=.8, ax=axes[0, 1], discrete=True, hue='Pclass', palette="coolwarm")
axes[0, 1].set_title('Passenger Class distribution')
axes[0, 1].set_xlabel('Passenger Class')
axes[0, 1].set_xticks([1, 2, 3])

sns.histplot(data=train, x='Sex', bins=2, shrink=.8, ax=axes[0, 2], discrete=True, hue='Sex', palette="coolwarm")
axes[0, 2].set_title('Sex distribution')
axes[0, 2].set_xlabel('Sex')

sns.histplot(data=train, x='Age', bins=10, shrink=.8, ax=axes[1, 0], kde=True, palette="coolwarm")
axes[1, 0].set_title('Age distribution')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_xticks(range(0, 80 + 1, 5))

sns.histplot(data=train, x='Fare', shrink=.8, ax=axes[1, 1], palette="coolwarm")
axes[1, 1].set_title('Fare distribution')
axes[1, 1].set_xlabel('Fare')

temp = train.copy()
temp['Embarked'][temp['Embarked'] == 'S'] = 'Cherbourg'
temp['Embarked'][temp['Embarked'] == 'C'] = 'Queenstown'
temp['Embarked'][temp['Embarked'] == 'Q'] = 'Southampton'

sns.histplot(data=temp, x='Embarked', bins=3, shrink=.8, ax=axes[1, 2], discrete=True, hue='Embarked',
             palette="coolwarm")
axes[1, 2].set_title('Embark distribution')
axes[1, 2].set_xlabel('Embark')
axes[1, 2].set_xticks(['Cherbourg', 'Queenstown', 'Southampton'])

plt.show()

# violin plot

fig, axes = plt.subplots(2, 3, figsize=(24, 18))

sns.violinplot(data=train, x="Pclass", y="Fare", hue="Survived",
               split=True, inner="quart", linewidth=1,
               palette="husl", ax=axes[0, 0])
axes[0, 0].set_title('Fare vs Passenger Class Violin Plot - Color Coded Survival Status')
axes[0, 0].set_ylabel('Fare')

sns.violinplot(data=train, x="Sex", y="Fare", hue="Survived",
               split=True, inner="quart", linewidth=1,
               palette="husl", ax=axes[0, 1])
axes[0, 1].set_title('Fare vs Sex Violin Plot - Color Coded Survival Status')

sns.violinplot(data=train, x="Embarked", y="Fare", hue="Survived",
               split=True, inner="quart", linewidth=1,
               palette="husl", ax=axes[0, 2])
axes[0, 2].set_title('Fare vs Embarked Violin Plot - Color Coded Survival Status')

sns.violinplot(data=train, x="Pclass", y="Age", hue="Survived",
               split=True, inner="quart", linewidth=1,
               palette="husl", ax=axes[1, 0])
axes[1, 0].set_title('Age vs Passenger Class Violin Plot - Color Coded Survival Status')
axes[1, 0].set_ylabel('Age')

sns.violinplot(data=train, x="Sex", y="Age", hue="Survived",
               split=True, inner="quart", linewidth=1,
               palette="husl", ax=axes[1, 1])
axes[1, 1].set_title('Age vs Sex Violin Plot - Color Coded Survival Status')

sns.violinplot(data=train, x="Embarked", y="Age", hue="Survived",
               split=True, inner="quart", linewidth=1,
               palette="husl", ax=axes[1, 2])
axes[1, 2].set_title('Age vs Embarked Violin Plot - Color Coded Survival Status')

plt.show()


def correlation_heatmap(df):
    _, ax = plt.subplots(figsize=(14, 12))

    colormap = sns.diverging_palette(180, 5, s=80, l=55, n=9)

    _ = sns.heatmap(df.corr(), annot=True, cmap=colormap, square=True, cbar_kws={'shrink': .8}, ax=ax, linewidths=0.1,
                    vmax=1.0, linecolor='white',
                    annot_kws={'fontsize': 20})

    plt.title('Pearson Correlation of Features', y=1.05, size=15)


co_plt = train.drop(['PassengerId'], axis=1).corr()
correlation_heatmap(co_plt)
plt.show()

pp = sns.pairplot(train.drop(['PassengerId'], axis=1), hue='Survived', palette='husl', size=1.2,
                  diag_kws=dict(shade=True), plot_kws=dict(s=10))
pp.set(xticklabels=[])
plt.show()
