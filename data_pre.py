# import libraries
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import   StandardScaler

# read csv files
data = pd.read_csv("Data.csv")

# dependant and independant values
independant = data.iloc[: , :-1].values
dependant = data.iloc[: , 3].values

# handle the missing values
imputer = SimpleImputer(missing_values=np.nan , strategy='mean')
imputer = imputer.fit(independant[: , 1:3])
independant[: , 1:3] = imputer.transform(independant[: , 1:3])

# encode catagorical values
independant_encoder = LabelEncoder()
independant[: , 0] = independant_encoder.fit_transform(independant[:,0])
# create dummy variables
# onehotencoder = OneHotEncoder(categories=independant[0] , handle_unknown='ignore')
# independant = onehotencoder.fit_transform(independant).toarray()

# handle the dependant variable
dependant_encoder = LabelEncoder()
dependant = dependant_encoder.fit_transform(dependant)

# spliting data into test set and training set
independant_train , independant_test , dependant_train , dependant_test = train_test_split(independant , dependant , test_size=0.2 , random_state=0)

# feature scaling
independant_scaler = StandardScaler()
independant_train = independant_scaler.fit_transform(independant_train)
independant_test = independant_scaler.transform(independant_test)
print(independant_test)
