import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#imports

# Create Dataframe
dataframe = pd.read_csv("C:\\Users\\Owner\\Documents\\covid_deaths_usafacts_may2020.csv", index_col=0)

# Confirm data was loaded into dataframe
#print(dataframe.head(50))

# Need to wrap in a Loop to iterate all dates. Updating the indexes each time.
fig = plt.figure(figsize=(150,350))
ax = fig.add_subplot(1,1,1)
ax.bar(dataframe.index, dataframe['5/31/2020'], color='b', align='center', label='5/31/2020')
ax.bar(dataframe.index, dataframe['5/15/2020'], color='g', align='center', label='5/15/2020')
ax.bar(dataframe.index, dataframe['5/1/2020'], color='r', align='center', label='5/1/2020')
#End loop

ax.set_xticks(ax.get_xticks())
ax.set_xticklabels(dataframe.index, rotation=90, ha='right', rotation_mode="anchor", fontsize='12')
ax.set_title('Number of Cases by State', fontsize='22')
ax.set_ylabel('# of Cases')
ax.set_xlabel('State')
ax.yaxis.get_ticklocs(minor=True)
ax.minorticks_on()
ax.xaxis.set_tick_params(which='minor', bottom=False)
ax.grid(axis='y', which='both', linestyle='dotted', linewidth='0.5', color='black')
handles,labels=ax.get_legend_handles_labels()
ax.legend(list(reversed(handles)), list(reversed(labels)), loc='upper right', title='Date')


# Confirm data was loaded into dataframe
#print(dataframe.head(50))

#Loop to iterate all dates. Updating the indexes each time.
fig = plt.figure(figsize=(150,350))
ax = fig.add_subplot(1,1,1)
ax.plot(dataframe['5/31/2020'], dataframe.index,color='b', label='5/31/2020')
ax.plot(dataframe['5/15/2020'], dataframe.index, color='g', label='5/15/2020')
ax.plot(dataframe['5/1/2020'], dataframe.index, color='r', label='5/1/2020')
#End loop

ax.set_xticks(ax.get_xticks())
ax.set_xticklabels(dataframe.index, rotation=90, ha='right', rotation_mode="anchor", fontsize='12')
ax.set_title('Number of Cases by State', fontsize='22')
ax.set_xlabel('# of Cases')
ax.set_ylabel('State')
ax.xaxis.get_ticklocs(minor=True)
ax.minorticks_on()
ax.yaxis.set_tick_params(which='minor', bottom=False)
ax.grid(axis='x', which='both', linestyle='dotted', linewidth='0.5', color='black')
handles,labels=ax.get_legend_handles_labels()
ax.legend(list(reversed(handles)), list(reversed(labels)), loc='upper right', title='Date')

plt.show()




