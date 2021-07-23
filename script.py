import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

#print(wood.head())
#print(steel.head())
#print(wood[wood.Park == 'El Toro'])





# write function to plot rankings over time for 1 roller coaster here:
def coaster_ranking(coaster, ranking, park):
    df = ranking[(ranking.Name == coaster) & (ranking.Park == park)]
    x = df['Year of Rank'].values
    y = df.Rank.values
    
    x_values = range(np.min(x), (np.max(x) + 1))
    y_values = range(np.min(y), (np.max(y) + 1))
    
    ax = plt.subplot()
    
    plt.plot(x, y, marker='o')
    ax.invert_yaxis()
    plt.ylabel('Rank')
    ax.set_xticks(x_values)
    ax.set_yticks(y_values)
    plt.title(f'{coaster} Rankings')
    
    plt.show()



#coaster_ranking('El Toro', wood, 'Six Flags Great Adventure')




plt.clf()

# write function to plot rankings over time for 2 roller coasters here:

def coaster_ranking2(coaster1, ranking1, park1, coaster2, ranking2, park2):
    df1 = ranking1[(ranking1.Name == coaster1) & (ranking1.Park == park1)]
    x1 = df1['Year of Rank'].values
    y1 = df1.Rank.values
    
    df2 = ranking2[(ranking2.Name == coaster2) & (ranking2.Park == park2)]
    x2 = df2['Year of Rank'].values
    y2 = df2.Rank.values
    
    x_lst = np.concatenate((x1, x2), axis=None)
    y_lst = np.concatenate((y1, y2), axis=None)
    
    x_values = range(np.min(x_lst), np.max(x_lst))
    y_values = range(np.min(y_lst), np.max(y_lst))
    
    ax = plt.subplot()
    
    plt.plot(x1, y1, marker='o', label=coaster1)
    plt.plot(x2, y2, marker='o', label=coaster2)
    
    ax.invert_yaxis()
    plt.ylabel('Rank')
    plt.ylabel('Year')
    ax.set_xticks(x_values)
    ax.set_yticks(y_values)
    plt.title(f'{coaster1} vs {coaster2} Rankings')
    plt.legend()
    
    plt.show()


#coaster_ranking2('El Toro', wood, 'Six Flags Great Adventure', 'Boulder Dash', wood, 'Lake Compounce')


plt.clf()

# write function to plot top n rankings over time here:

def coaster_ranking_n(rank, ranking):
    if rank <= 0:
        return "Rank does not exist"
    
    df = ranking[ranking.Rank <= rank]
    

    
    ax = plt.subplot()

    
    for coaster in set(df.Name):    
        
        coaster_rankings = df[df.Name == coaster]
        
        plt.plot(coaster_rankings['Year of Rank'], coaster_rankings.Rank, label=coaster, marker='o')

        
       
    ax.invert_yaxis()
    plt.title(f'Top {rank} Rankings')
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend()
    
    plt.show()





#coaster_ranking_n(5, wood)



plt.clf()

# load roller coaster data here:

roller_coasters = pd.read_csv('roller_coasters.csv')
print(roller_coasters.head())

# write function to plot histogram of column values here:

def column_data(column):
    df = roller_coasters[column].dropna()

    plt.hist(df.values, bins=20)
    plt.title(f"{column} Histogram")
    plt.ylabel(column)

    plt.show()


#column_data('length')


plt.clf()

# write function to plot inversions by coaster at a park here:

def inversions(coaster_df, park_name):
    df = coaster_df[coaster_df.park == park_name]

    num_inv = df.num_inversions.values
    names = df.name.values
    
    
    
    ax = plt.subplot()
    plt.bar(range(len(names)), num_inv)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=30)
    plt.xlabel('Coaster Names')
    plt.ylabel('Number of Inversions')
    plt.title(f'Number of Inversions per Coaster at {park_name}')
    plt.show()

    

#inversions(roller_coasters, 'Parc Asterix')

plt.clf()

# write function to plot pie chart of operating status here:

def coaster_pie(df):
    

    operating = df[df.status == 'status.operating']
    closed = df[df.status == 'status.closed.definitely']

    operating_values = len(operating)
    closed_values = len(closed)

    pie_values = [operating_values, closed_values]

    labels = ['operating', 'closed']

    plt.pie(pie_values, labels=labels, autopct='%d%%')
    plt.axis('equal')
    plt.title('Operating Status Chart')
    plt.show()





#coaster_pie(roller_coasters)


plt.clf()

# write function to create scatter plot of any two numeric columns here:

def coaster_scatter(column1, column2, df):

    x = df[column1].values
    y = df[column2].values

    plt.scatter(x, y)
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(f'{column1} in relation to {column2}')

    plt.show()


#coaster_scatter('speed', 'length', roller_coasters)





plt.clf()
