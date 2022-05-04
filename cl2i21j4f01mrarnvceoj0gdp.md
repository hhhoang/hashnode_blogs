## Encoding Categorical Data

Encoding categorical variables is an important step in preprocessing for buillding a statistical model in data science. Because most of the machine learning algoriths donot work (well) with categorical data directly but rather in numeric form. The categorical data could be feedback type (very poor, poor, satisfactory, good, very good) or  regions (Europe, Asia, Americas, Oceania, Africa). The process to convert a categorical variable into numeric variable is called encoding.

There are many ways of categorical encoding, but the most popular ways are label encoding and one-hot encoding, which I will focus on this article. First, let's generate some data to use on both approaches. 


```
from sklearn import preprocessing
import pandas as pd

# initialize list of lists
data = [['male', 40, 'Basic'], ['female', 30, 'Master'], [
    'female', 22, 'Bachelor'], ['male', 60, 'Phd'], ['female', 44, 'Bachelor']]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Gender', 'Age', 'Education'])

# print dataframe.
print(df)
print(df.dtypes)

   Gender  Age Education
0    male   40     Basic
1  female   30    Master
2  female   22  Bachelor
3    male   60       Phd
4  female   44  Bachelor

Gender       object
Age           int64
Education    object

``` 

1. Label Encoding
Label encoding simply converts each unique wording label into numerical number based on alphabetical order. There are two ways you can achieve this by:
- approach 1: using category codes in pandas 
- approach 2: using class LabelEncoder from scikit-learn library

**Approach 1: Category Codes**

```
# Convert object type to category type
df['Education'] = df['Education'].astype('category')
df['Education_C'] =  df['Education'].cat.codes
print(df.head())

   Gender  Age Education  Education_C
0    male   40     Basic            1
1  female   30    Master            2
2  female   22  Bachelor            0
3    male   60       Phd            3
4  female   44  Bachelor            0
``` 


**Approach 2: LabelEncoder**
```

# instantiate LabelEncoder()
label_encoder = preprocessing.LabelEncoder()

# Encode labels in column 'Education'.
df['Education_N'] = label_encoder.fit_transform(df['Education'])
print(df.head())

   Gender  Age Education  Education_C  Education_N
0    male   40     Basic            1            1
1  female   30    Master            2            2
2  female   22  Bachelor            0            0
3    male   60       Phd            3            3
4  female   44  Bachelor            0            0
``` 
We see for both approaches, we have the same conversion of label to numerical form. However, there is no relationship between categories themselves, but label encoding introduces an order relationship. Will the model associate the higher value of label as better and so on? 

2. One-Hot Encoding

With one hot encoding we introduce a number of new dummy variables with binary encoding (0 and 1) to address if any label appears in which row (1) or not (0). After encoding, we will see each unique category of the feature 'Education' represented as a separate feature. The same as label encoding, we can generate one hot encoding by two methods:

- approach 1: using get_dummies from pandas
- approach 2: using class OneHotEncoder from scikit-klearn library


```
# 2.1 Approach 1: get_dummies
dummy_df = pd.get_dummies(df['Education'])
print(dummy_df)

   Bachelor  Basic  Master  Phd
0         0      1       0    0
1         0      0       1    0
2         1      0       0    0
3         0      0       0    1
4         1      0       0    0

``` 



```
# 2.2 Approach 2: OneHotEncoder()

# instantiate OneHotEncoder()
onehotencoder = preprocessing.OneHotEncoder()

# encode labels in column 'Education'
one_hot_df = onehotencoder.fit_transform(df['Education]).toarray()
``` 


One Hot Encoding overcomes the shortcoming of LabelEncoding in which it preserves the nature of no ordinal ranking amongst labels. However, its disadvantage lies at the high number of additional columns, which in turn causes the 'curse of dimensionality' as well as the memory consumption. 
