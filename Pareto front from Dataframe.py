import pandas as pd

def is_pareto(dataframe):
    #Returns True-False dataframe column if the row is Pareto optimal
    #All objectives have to be set up to minimize
    
    rows,columns = dataframe.shape
    paretoList = []
    for i in range(rows):
        pareto = True #If there are not rows with all objectives smaller than i, then i-th row is Pareto optimal
        for j in range(rows):
            #Change here from > to < if all objectives are set up for maximize
            #Compares objective values from j if they are smaller than i
            paretotest = dataframe.iloc[i] > dataframe.iloc[j]
            #If all objective values are smaller in j from i, then the i-th row is not Pareto optimal
            if all(paretotest) is True:
                pareto = False
                break
        paretoList.append(pareto)
    return pd.Series(paretoArray)
