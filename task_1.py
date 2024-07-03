import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

new_data = pd.DataFrame({'robot' : [0] * len(lst),
                         'human' : [0] * len(lst)})

new_data.index = range(1, len(lst) + 1)
new_data.index.name = 'Номер'

new_data['human'] = (data['whoAmI'] == 'human').astype(int).values
new_data['robot'] = (data['whoAmI'] == 'robot').astype(int).values

print(new_data)