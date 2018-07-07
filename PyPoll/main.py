# Dependencies
import pandas as pd


# Import Data
file = "Resources/election_data.csv"
election = pd.read_csv(file)

# Data Exploration
list(election) # ['Voter ID', 'County', 'Candidate']


# The total number of votes cast
votes=election["Voter ID"].count()

# A complete list of candidates who received votes, percentage, and total number of votes
results=election.groupby(["Candidate"]).count().sort_values(["Voter ID"],ascending=False)
results["Share"]=((results["Voter ID"]/votes)*100).map("{:.0f}%".format)
results=results.rename(columns={"Voter ID":"Votes Earned"})
results=results.loc[:,["Share","Votes Earned"]]



# The winner of the election based on popular vote.
max_vote=results["Votes Earned"].max()
winner=results.loc[results["Votes Earned"]==max_vote,:]
results=results.reset_index()
winner=results.iloc[0,0]


# Output

print ("Election Results")
print( "==========================")
print("Total Votes:",votes)
print(results.to_string(index=False))
print( "==========================")
print("Winner:",winner)
print( "==========================")