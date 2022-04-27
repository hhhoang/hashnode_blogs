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

   Gender  Age Education
0    male   40     Basic
1  female   30    Master
2  female   22  Bachelor
3    male   60       Phd
4  female   44  Bachelor

``` 

1. Label Encoding
Label encoding simply converts each unique wording label into numerical number based on alphabetical order. There are two ways you can achieve this by:
- using replace function 
- using from package


```
data = df.copy()
# instantiate LabelEncoder()
label_encoder = preprocessing.LabelEncoder()

# Encode labels in column 'Education'.
data['Education'] = label_encoder.fit_transform(data['Education'])
print(data.head())
``` 


Let’s see how to implement label encoding in Python using the scikit-learn library and also understand the challenges with label encoding.

2. One-Hot Encoder
Label encoding is easy to understand and straightforward to implement, however the numeric values are assigned 
