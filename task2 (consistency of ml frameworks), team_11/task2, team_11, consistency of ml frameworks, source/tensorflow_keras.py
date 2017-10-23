import tensorflow as tf
import pandas as pd
import numpy as np

from keras.layers import Dense
from keras.models import Model, Sequential
from keras import initializers, optimizers

sumdata_noise_path = "data/with noise/The SUM dataset, with noise.csv"
sumdata_path = "data/without noise/The SUM dataset, without noise.csv"
housing_price_path = "data/housing dataset.csv"
sumdata_noise = pd.read_csv(sumdata_noise_path, delimiter=";")

# Remove 'Instance' as it simply represents the row number
sumdata_noise.drop('Instance', axis = 1)

# Extract 'Nosiy Target' as regression target
sumdata_noise_reg_Y = sumdata_noise[['Noisy Target']]

# Extract 'Nosiy Target Class' as regression target
sumdata_noise_classif_Y = sumdata_noise['Noisy Target Class']

# Extract rest columns as explananatory variables
sumdata_noise_X = sumdata_noise.iloc[:, 1:-2]


X = sumdata_noise_X.head(n = 1000)
y = sumdata_noise_reg_Y.head(n = 1000)
X = X.as_matrix()
y = y.as_matrix()
ndims = X.shape[1]

rnd_indices = np.random.rand(len(X)) <0.8
X_train, X_test = X[rnd_indices], X[~rnd_indices]
y_train, y_test = y[rnd_indices], y[~rnd_indices]


model = Sequential([
        Dense(1, activation='linear', input_shape=(ndims,))
    ])

sgd = optimizers.SGD(lr=0.01)
model.compile(loss='mse', optimizer=sgd)


model.fit(X_train, y_train, epochs=1000, batch_size=10,verbose=0)
model.fit(X_train, y_train, epochs=100, batch_size=100,verbose=1)
score = model.evaluate(X_test, y_test, batch_size=100)
print(score)

