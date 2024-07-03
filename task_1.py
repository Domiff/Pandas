import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

new_data = pd.DataFrame({'robot' : [],
                         'human' : []})

new_data['human'] = data['whoAmI'] == 'human'
new_data['robot'] = data['whoAmI'] == 'robot'
print(new_data)