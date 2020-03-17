# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
from sklearn import ensemble, linear_model, svm
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt


# The function os.getcwd() returns the directory where the regression.py script is located
directory = os.getcwd()

# We use pandas read_csv as an easy way to get the data from the csv into a python object we can work with
data = pd.read_csv(os.path.join(directory, 'data.csv'))

# The data we read in can be separted into independent variables and the net electrical output, which is what we are trying to predict
x = data[[u'temperature C', u'exhaust vacuum (cm Hg)', u'ambient pressure (mBar)', u'relative humidity (%)']]
y = data[[u'net electrical output (MW)']]

# It's a good idea in any regression to separate data into a training and validating set. Let's separate 20% of the data to form our validation.
training_fraction = 0.8
training_size = int(training_fraction*len(data))
shuffle = range(len(data)) # This will create numbers [0, 1, 2, 3, .... n]
np.random.shuffle(shuffle) # This will put those numbers in a random order
training_index = shuffle[:training_size] # Get the index of the records that we will put in our training set
validating_index = shuffle[training_size:] # Get the index of records in the validating set

# Split the x and y data into our training and validating
x_train = x.values[training_index]
y_train = y.values[training_index].flatten()

x_test = x.values[validating_index]
y_test = y.values[validating_index].flatten()

###################################
## EXAMPLE REGRESSION
###################################

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(x_train, y_train)

# Make predictions using the validating set
y_test_pred = regr.predict(x_test)

# Print the mean squared error (for me this is 20.093)
print "Mean squared error: {}".format(mean_squared_error(y_test, y_test_pred))
# Explained variance score: 1 is perfect prediction (for me this is 0.9318)
print 'Variance score: {}'.format(r2_score(y_test, y_test_pred))

#Plot the validation results
plt.plot(y_test, y_test_pred, '.')
plt.title('CCGT Regression')
plt.xlabel('Observed Net Output (MW)')
plt.ylabel('Predicted Net Output (MW)')
plt.show()

##################################
# Your Regression
##################################
# Play with different regressions that you find on https://scikit-learn.org
# Can you find a technique that gives you a validating dataset mean squared error of less than 15?
# You must implement at least one other regression type that is not the example given above or make some other change that gives improved results.

# YOUR CODE GOES HERE




##################################
# Use your best regression and answer the following questions
##################################
# 1. A location further south has average temperatures 4 degrees celsius warmer. All else equal, by what % do you expect the CCGT output to change?
# 2. What would you pick for this CCGT's summer rated capacity used in reliability planning and why?
# 3. Create a plot that shows the difference between exhaust vacuum and ambient pressure against the net plant output.
    # 1 cm HG = 13.332237 mBar

