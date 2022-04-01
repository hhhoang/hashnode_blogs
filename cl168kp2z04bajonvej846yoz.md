## Dummy models for dummies

Sometimes in your data science work you need to prove that your model is better than a 'dummy' model. Instead of write your own random guess snippet, you can take advantage of dummy models from sklearn package. We will be using one dummy model for regression problem and one dummy model for classification problem. 

For both of the dummy model demonstration, we will perform the following steps:

- read in the dataset and randomly split 70/30
- train the dummy model
- compare the dummy model with a 'real' and simple model


### Built-in dataset

Did you know that sklearn comes with some small %datasets[https://scikit-learn.org/stable/datasets], so that it comes in handy when you need something quickly. They are pretty clean and standard, so you don't need to perform data cleansing and quality check. They ranges from toy datasets to real world datasets for your usage.

For dummy regressor I will be using the diabetes dataset %[https://scikit-learn.org/stable/datasets/toy_dataset.html#boston-house-prices-dataset] and for dummy classifier I will be using the breast cancer dataset %[https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset]. I am sorry for bringing only sickness here though. I promise I will use another dataset next time. 

```
# Import the datasets
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_breast_cancer

# Load the diabetes dataset
diabetes = load_diabetes()
diabetes_X = diabetes['data']
diabetes_y = diabetes['target']

# Load the breast cancer dataset
breast_cancer = load_breast_cancer()
breast_cancer_X = breast_cancer['data']
breast_cancer_y = breast_cancer['target']

``` 


### Dummy Regressor

Dummy Regressor makes predictions based on one of the simple rules. The simple rules are as follow:

- mean: always predicts the mean of the training set

- median: always predicts the median of the training set

- quantile: always predicts a specified quantile of the training set, provided with the quantile parameter. If you use quantile, you need to specify which quantile you will be using, in which 0.0 means min value, 0.5 is the median and 1 means max value

- constant: always predicts a constant value that is provided by the user. If you use constant strategy, you need to specify which constant value

Here I will only demonstrate the strategies with mean and median and then compare the score (R squared) with a simple linear regression. R squared measures how well the actual outcomes are replicated by the regression line, hence how good your model is. R squared lies between 0 and 1, the closer to 1, the better the model is.

Let's read the dataset and split them into dependent and independent variables.

```
# import packages
from sklearn.model_selection import train_test_split

# Splitting the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
            diabetes_X, diabetes_y, test_size = 0.3, random_state = 0)

# declare strategies
strategies = ['mean', 'median']

for s in strategies:
    dummy_regr = DummyRegressor(strategy = s).fit(X_train, y_train)
    score = dummy_regr.score(X_test, y_test)
    print(f'For strategy {s}, score is: {score}')

``` 
For strategy mean, score is: -4.088943807989409e-07
For strategy median, score is: -0.02901059196601352


```
# compare with a simple linear regression
linear_regr = LinearRegression().fit(X_train, y_train)
lin_reg_score = linear_regr.score(X_test, y_test)
print(f'For simple linear regression, score is: {lin_reg_score}')
``` 
For simple linear regression, score is: 0.3928939845074757.

Eventhough the R squared for the linear regression isn't perfect yet, however in comparison to the dummy regresor it is already so much better.

### Dummy Classifier

A dummy classifier follows only one of a few strategies to predict the class label without giving any knowledge about the features but mainly depends on the values of observed target. The strategies include: 

- Most Frequent: The classifier always predicts the most frequent class label in the observed y argument passing to fit.
- Prior: It always predict the most frequent class label in the observed y argument passing to fit (like most frequent). The difference lies in the prediction probability (predict_proba method) which is out of scope here.
- Stratified: It predicts based on the class distribution of the training data. It is different from the “most frequent” strategy as it instead associates a probability with each data point of being the most frequent class label.
- Uniform: It generates predictions uniformly at random from the list of unique classes observed in y.
- Constant: The classifier always predicts a constant label provided by the user.

The method score of the class returns the mean accuracy so that we can compare the performance of the models. 


```
# Splitting the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
            breast_cancer_X, breast_cancer_y, test_size = 0.3, random_state = 0)

# declare strategies
strategies = ['most_frequent', 'prior', 'stratified', 'uniform']

for s in strategies:
    dummy_clf = DummyClassifier(strategy = s, random_state = 0)
    dummy_clf.fit(X_train, y_train)
    dummy_clf_score = dummy_clf.score(X_test, y_test)
    print(f'For strategy {s}, score is: {dummy_clf_score}')


#compare with a simple KNearestNeighbor with k=2
KNN_clf = KNeighborsClassifier(n_neighbors=2).fit(X_test, y_test)
KNN_clf_score = KNN_clf.score(X_test, y_test)
print(f'For a simple KNN classfier, score is: {KNN_clf_score}')

``` 
For strategy most_frequent, score is: 0.631578947368421.
For strategy prior, score is: 0.631578947368421.
For strategy stratified, score is: 0.5906432748538012.
For strategy uniform, score is: 0.6140350877192983.
For a simple KNN classfier, score is: 0.9824561403508771.

So we can see that just using a simple KNN classifier with a cluster of 2, we achieve 98% accuracy meanwhile dummy classifier gives around 60-63%.
