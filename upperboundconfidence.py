#import libs
import math
import pandas as pd
import matplotlib.pyplot as plt

#get the dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

#implement UCB
d = 10
N = 10000
number_of_selections = [0] * d
sum_of_rewards = [0] * d
ads_selected = []
total_reward = 0

for n in range(0 , N):
    max_upper_bound = 0
    ad = 0
    for i in range(0 , d):
        if number_of_selections[i] > 0:
            avarage_reware = sum_of_rewards[i] / number_of_selections[i]
            delta_i = math.sqrt(3 / 2 * math.log(n + 1) / number_of_selections[i])
            upper_bound = avarage_reware + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] += 1
    reward = dataset.values[n, ad]
    sum_of_rewards[ad] += reward
    total_reward += reward

print(total_reward)
# print(ads_selected)

#visualize the results
plt.hist(ads_selected)
plt.title("Histgram The upper confident bound algorithm")
plt.xlabel("Ads")
plt.ylabel("Number of times each ad selected")
plt.show()