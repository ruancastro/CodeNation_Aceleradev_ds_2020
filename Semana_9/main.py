import pandas as pd
from collections import Counter
import numpy as np
from sklearn.ensemble import RandomForestClassifier

df_test = pd.read_csv('test.csv')
df_train = pd.read_csv('train.csv')

#Counter(df_train.IN_TREINEIRO)

ID = 'NU_INSCRICAO'
target = 'IN_TREINEIRO'
df = df_train[list(df_test.columns)].fillna(0)
df = df.drop(columns=[ID])
train_features = pd.get_dummies(df)


# Labels are the values we want to predict
train_labels = np.array(df_train[target].to_list())
# Saving feature names for later use
feature_list = list(train_features.columns)
# Convert to numpy array
features_nparray = np.array(train_features)

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)


# Instantiate model with 1000 decision trees
rf = RandomForestClassifier(n_estimators = 200, random_state = 42, n_jobs = -1, verbose = 1)
# Train the model on training data
rf.fit(train_features, train_labels);

#predictions = rf.predict(train_features)

#sum(predictions-train_labels)

df_answer = pd.DataFrame()

df_answer[ID] = df_test[ID]
df_test = df_test.drop(columns=[ID]).fillna(0)
test_features = pd.get_dummies(df_test)
predictions = rf.predict(test_features)

df_answer[target] = list(predictions)
#df_answer.head()

df_answer.to_csv('answer.csv', index=False)