# Import packages
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split

from sklearn.dummy import DummyRegressor
from sklearn.dummy import DummyClassifier

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier


##################### DUMMY REGRESSOR #################################
# Load diabetes data
diabetes = load_diabetes()
# Load diabetes into a dataframe and set the field names
diabetes_X = diabetes['data']
diabetes_y = diabetes['target']

# Splitting the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
            diabetes_X, diabetes_y, test_size = 0.3, random_state = 0)

#score returns the R2, which measures how well the actual outcomes are replicated by the regression line
# or how good your model is. R2 lies between 0 and 1, the closer to 1, the better the model is

# declare strategies
strategies = ['mean', 'median']

for s in strategies:
    dummy_regr = DummyRegressor(strategy = s).fit(X_train, y_train)
    score = dummy_regr.score(X_test, y_test)
    print(f'For strategy {s}, score is: {score}')

    

# compare with a simple linear regression
linear_regr = LinearRegression().fit(X_train, y_train)
lin_reg_score = linear_regr.score(X_test, y_test)
print(f'For simple linear regression, score is: {lin_reg_score}')


##### Dummy Classifier ######
breast_cancer = load_breast_cancer()

breast_cancer_X = breast_cancer['data']
breast_cancer_y = breast_cancer['target']


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

