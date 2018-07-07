# python-challenge


# Dependencies
import pandas as pd

# Import Data

file = "Resources/budget_data.csv"
budget = pd.read_csv(file)

# Data Exploration
list(budget) #['Date', 'Profit/Losses']


# The total number of months included in the dataset
months=budget["Date"].count()

# The total net amount of "Profit/Losses" over the entire period
net_amount=total_amount=budget["Profit/Losses"].sum()

# The average change in "Profit/Losses" between months over the entire period
budget["Change"]= budget["Profit/Losses"].diff()
average_change=round(budget["Change"].mean(),2)

# The greatest increase in profits (date and amount) over the entire period
max_increase_amt=budget["Change"].max()
max_month=budget.loc[budget["Change"]==max_increase_amt,:]
max_month_name=max_month.iloc[0,0]


# The greatest decrease in losses (date and amount) over the entire period
max_decrease_amt=budget["Change"].min()
min_month=budget.loc[budget["Change"]==max_decrease_amt,:]
min_month_name=min_month.iloc[0,0]


budget["Change"].min() #-2196167



# Output
print ("Financial Analysis")
print( "==========================")
print("Total Months:",months)
print("Total: $",net_amount)
print("Average  Change $:",average_change)
print("Greatest Increase in Profits:",max_month_name,"($",max_increase_amt,")")
print("Greatest Decrease in Profits:",min_month_name,"($",max_decrease_amt,")")
