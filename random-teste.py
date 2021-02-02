#%%
import numpy as np 
import matplotlib.pyplot as plt 

arr1 = np.random.normal(0,1,10000)


fig,axs = plt.subplots(figsize = (10,6))

plt.hist(arr1, bins = 100, color = 'black')
plt.show()
# %%
