
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

df = pd.read_csv('dataout.csv',delimiter='\t',header=None,usecols=[1,2,3,4])

#print(df)

df = df.iloc[1:,:4]

#print(df)

df = df.astype({1: int,2: int,3: int,4: "category"})
df[5]=df[4].cat.codes

#print(df)

dffiltered = df[df[1] < 1024]
dffiltered = dffiltered[dffiltered[2] < 1024]
dffiltered = dffiltered[dffiltered[3] < 1024]

#print(dffiltered)

dffilterednp = np.zeros((dffiltered.shape[0],3))

dffilterednp[:,0] = dffiltered[1].to_numpy()
dffilterednp[:,1] = dffiltered[2].to_numpy()
dffilterednp[:,2] = dffiltered[3].to_numpy()
dffilterednp = dffilterednp.astype(int)

#print(dffilterednp)

dflabelsnp = dffiltered[5].to_numpy().astype(int)

#print(dflabelsnp)

x_train, x_test, y_train, y_test = train_test_split(dffilterednp, dflabelsnp, test_size=0.2,random_state=4)

# print(x_train,x_test,y_train,y_test)

model = RandomForestClassifier(n_estimators=10)
model.fit(x_train, y_train)

model.score(x_test,y_test)

print(model.score(x_test,y_test))

y_predicted = model.predict(x_test)

cm = confusion_matrix(y_test, y_predicted)
print(cm)

model2 = KNeighborsClassifier(n_neighbors=4)
model2.fit(x_train, y_train)

print(model.score(x_test,y_test))

y_predicted = model2.predict(x_test)

cm2 = confusion_matrix(y_test, y_predicted)
print(cm2)