#import the libs
import pandas as pd
from apyori import apriori

#get the dataset
dataset = pd.read_csv("Market_Basket_Optimisation.csv" , header=None)

#create a list for the transactions to be used for the algorithm
transactions = []
for i in range(0 , 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

#create the rules
rules = apriori(transactions , min_support=0.003 , min_confidence=0.2 , min_lift=3 , min_length=2)

#get the results
results = list(rules)

print(results)

