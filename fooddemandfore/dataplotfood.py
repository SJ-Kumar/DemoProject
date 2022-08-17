import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('seaborn')

df_meal = pd.read_csv(r'C:\10-Practice\DemoProject\fooddemandfore\meal_info.csv') 

df_center = pd.read_csv(r'C:\10-Practice\DemoProject\fooddemandfore\fulfilment_center_info.csv') 

df_food = pd.read_csv(r'C:\10-Practice\DemoProject\fooddemandfore\train_food.csv') 

df = pd.merge(df_food,df_center,on='center_id') 
df = pd.merge(df,df_meal,on='meal_id')

print(df)
table = pd.pivot_table(data=df,index='category',values='num_orders',aggfunc=np.sum)
print(table)

#dictionary for meals per food item
item_count = {}

for i in range(table.index.nunique()):
    item_count[table.index[i]] = table.num_orders[i]/df_meal[df_meal['category']==table.index[i]].shape[0]

#bar plot 
plt.bar([x for x in item_count.keys()],[x for x in item_count.values()],color='orange')

#adjust xticks
plt.xticks(rotation=70)

#label x-axis
plt.xlabel('Food item')

#label y-axis
plt.ylabel('No. of meals')

#label the plot
plt.title('Meals per food item')

#save plot
plt.savefig(r'C:\10-Practice\DemoProject\fooddemandfore\matplotlib_plotting_7.png',dpi=300,bbox_inches='tight')

#display plot
plt.show();

      