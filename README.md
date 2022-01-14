# Election Analysis

## Overview
For this analysis, a Colorado Board of Election employee wants our help to audit the US Congressional precinct result in the state. Using our python skills we were tasked to fins multiple things:

- Total votes in the election
- A breakdown of the number/percentage of votes for each county and candidate
- Which county had the largest turnout 
- Who the winner was, the amount of votes they received, and their percentage of votes with respect to the total votes

## Election-Audit Results
Below we can see the overall output from running our script:


![](https://github.com/mooshak21/Election_Analysis/blob/main/Resources/D2.png)

- How many votes were cast in this congressional election?
> After running our program, we can see that the total number of votes were 369,711


![](https://github.com/mooshak21/Election_Analysis/blob/main/Resources/total_votes.png)

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
> The provided image shows the breakdown and the percentage of total votes for each county


![](https://github.com/mooshak21/Election_Analysis/blob/main/Resources/county_votes.png)

- Which county had the largest number of votes?
> Denver had the most votes with 306,055


![](https://github.com/mooshak21/Election_Analysis/blob/main/Resources/largest_turnout.png)

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
> The provided image shows the breakdown and the percentage of total votes for each candidate


![](https://github.com/mooshak21/Election_Analysis/blob/main/Resources/candidate_votes.png)

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
> The provided image shows the breakdown of the winner's statistics


![](https://github.com/mooshak21/Election_Analysis/blob/main/Resources/winner_breakdown.png)

## Summary
### Proposal
We were able to provide a high-level breakdown of the Colorado Congressional election using this code to highlight key points. This is a program that can definitely be used in the future for other elections with a few alterations:

1. Currently our code is specific to Colorado in the output in the command prompt. To change this we would want to change all factors specific to the town/state/candidate names to dynamically pull from the csv rather than hard coding them in. This would allow any state to use this program for their elections with the accurate data for their state in the output. This is only if the csv file is in the same format as the csv we used in the project which will most likely be true for most states as they will have the individual rows as each ballot. 

2. Another thing we can alter with the script is to put the code we created into functions when necessary. This will allow for code to be reused more easily and will complete the actions in a more general sense rather than specifying the candidate/county names. 