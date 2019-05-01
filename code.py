# --------------
import json
from collections import Counter

with open(path) as f:
    data = json.load(f)

# Code starts here
 
# Can you find how many deliveries were faced by batsman  `SC Ganguly`.
First_innings_info = data['innings'][0]
First_inning_deliveries = First_innings_info['1st innings']['deliveries']

def no_of_deliveries_faced_by_batsman(batsman_name, deliveries):
    balls_faced = sum(list(map(lambda x: 1 if list(x.values())[0]['batsman'] == batsman_name else 0, deliveries)))
    return balls_faced

ganguly_ballsfaced = no_of_deliveries_faced_by_batsman('SC Ganguly', First_inning_deliveries) 
print(f'Deliveries faced by Ganguly is {ganguly_ballsfaced}') 

# Who was man of the match and how many runs did he scored ?
    
    ## Man of the match

man_of_the_match = data['info']['player_of_match'][0]

    ## Runs scored by man of the match

def no_of_runs_scored_by_batsman(batsman_name, deliveries):
    runs_scored = sum(list(map(lambda x: list(x.values())[0]['runs']['batsman'] if list(x.values())[0]['batsman'] == batsman_name else 0, deliveries)))
    return runs_scored

runs_scored_by_man_of_the_match = no_of_runs_scored_by_batsman(man_of_the_match, First_inning_deliveries)

print(f'Man of the match was: {man_of_the_match} and he scored {runs_scored_by_man_of_the_match} runs')

# Which batsmen played in the first inning?

batsmen_played_in_first_innings = set(list(map(lambda x: list(x.values())[0]['batsman'], First_inning_deliveries)))

print(f'Batsmen who played in the first inning are {batsmen_played_in_first_innings} ')

# Which batsman had the most no. of sixes in first inning ?
def calculate_no_of_sixes(batsman_name, deliveries):
    is_six = list(map(lambda y: 1 if all([list(y.values()
    )[0]['runs']['batsman'] == 6, list(y.values())[0]['runs']['extras'] == 0, list(y.values())[0]['batsman'] == batsman_name]) else 0, deliveries ))
    sixes_scored = is_six.count(1) 

    ## With for loop
    # sixes_scored = 0
    # for delivery in deliveries:
    #     delivery_info = list(delivery.values())[0]
    #     is_six = 1 if all([delivery_info['runs']['batsman'] == 6, delivery_info['runs']['extras'] == 0, delivery_info['batsman'] == batsman_name) else 0
    # sixes_scored += is_six
    
    return batsman_name, sixes_scored


sixes_scored_by_batsman = dict(list(map(lambda x: calculate_no_of_sixes(x, First_inning_deliveries),  batsmen_played_in_first_innings))) 

max_sixes = max(sixes_scored_by_batsman, default = 0, key = lambda k: sixes_scored_by_batsman[k])

print(f'{max_sixes} hit the maximum sixes') 

# Find the names of all players that got bowled out in the second innings.

second_innings_info = data['innings'][1]['2nd innings']
second_inning_deliveries = second_innings_info['deliveries']

def players_bowled_out(deliveries):
    bowled_out_batsman = []

    for delivery in deliveries:
        delivery_info = list(delivery.values())[0]
        if 'wicket' in delivery_info: 
            if delivery_info['wicket']['kind'] == 'bowled':
                bowled_out_batsman.append(delivery_info['wicket']['player_out']) 

    return bowled_out_batsman

second_innings_bowled_out_batsman = players_bowled_out(second_inning_deliveries)
print(f'Players bowled out in second innings are: {second_innings_bowled_out_batsman}')


# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?

max_valid_deliveries = 120 

n_extra_runs_first_innings = 0
n_extras_first_innings = 0

for delivery in First_inning_deliveries: 
    # Take the information out of the delivery, as it's a dict inside a dict
    delivery_info = list(delivery.values())[0] 
    runs_in_the_delivery = delivery_info['runs']['total']
    extra_runs_in_the_delivery = delivery_info['runs']['extras']
    n_extra_runs_first_innings += extra_runs_in_the_delivery # add to n_extras
    #If number of extras is more than one then add 
    if extra_runs_in_the_delivery >= 1:
        n_extras_first_innings += 1

print('{} extras were bowled and {} extra runs were taken in the first innings'.format(n_extras_first_innings, n_extra_runs_first_innings))

# Second Innings Extras

n_extra_runs_second_innings = 0
n_extras_second_innings = 0

for delivery in second_inning_deliveries: 
    # Take the information out of the delivery, as it's a dict inside a dict
    delivery_info = list(delivery.values())[0] 
    runs_in_the_delivery = delivery_info['runs']['total'] 
    extra_runs_in_the_delivery = delivery_info['runs']['extras']
    n_extra_runs_second_innings += extra_runs_in_the_delivery # add to n_extras
    #If number of extras is more than one then add 
    if extra_runs_in_the_delivery >= 1:
        n_extras_second_innings += 1

print(f'{n_extras_second_innings} extras were bowled and {n_extra_runs_second_innings} extra runs were taken in the second innings') 


# Code ends here 


