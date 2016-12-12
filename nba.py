from stattlepy import Stattleship
import pandas as pd
import csv
import random

new_query = Stattleship()
token = new_query.set_token('71c379b013f38f528b7c7461cea6a46e')
#output is a list of dicts, where each dict's values are lists of stats... list-dict-list-float (example of how data comes in)
#output = new_query.ss_get_results(sport='basketball',league='nba',ep='player_season_stats',player_id='nba-brandon-ingram',on='today')
output = {}
#find dict keys, then find the dict inside the dict keys
#print output[0].keys()
#dct = output[0]['player_season_stats']

nba_players = []
with open('players.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        row = str(row)
        row = row.replace(" ","-").replace("[","").replace("]","").replace("'","-").replace(".","-")
        row = row[:-1]
        row = "nba" + row
        row = row.lower()
        nba_players.append(row)

def get_season_averages(player):
    output = new_query.ss_get_results(sport='basketball',league='nba',ep='player_season_stats',player_id=player,on='today')
    season_avg = output[0]['player_season_stats']
    df = pd.DataFrame(season_avg)
    df['player'] = player
    return df

def aggregate_season_avgs():
    df = pd.DataFrame()
    for player in nba_players:
        try:
        #if player not in {'nba-cj-mccollum', 'nba-cj-miles', 'nba-cj-wilcox', 'nba-cj-watson', 'nba-cristiano-felicio', 'nba-d-j--augustin'}:
            df = pd.concat([df, get_season_averages(player)], axis=0)
        except KeyError:
            continue
    return df

def projection(mins, pts, tov, tp, fdfp):
    minutes = .8498
    pts_ma_1 = .275
    tov_ma_1 = 1.127
    tp_ma_1 = -1.0926
    fd_fp_ma_1 = .4927
    pred = minutes*mins + pts_ma_1*pts + tov_ma_1*tov + tp_ma_1*tp + fd_fp_ma_1*fdfp
    #print pred
    return pred

def generate_random_pred(num_pred):
    preds = []
    for i in range(num_pred):
        rnd_m = random.randint(15,30)
        rnd_p = random.randint(5,40)
        rnd_tov = random.randint(0,10)
        rnd_tp = random.randint(0,10)
        rnd_fd = random.randint(10,70)

        proj = projection(rnd_m, rnd_p, rnd_tov, rnd_tp, rnd_fd)
        preds.append(proj)

    return preds

def generate_random_price(num_pred):
    prices = []
    for i in range(num_pred):
        price = random.randint(3000,12000)
        prices.append(price)
    return prices


print generate_random_pred(10)  
print generate_random_price(10)  

#aggregate_season_avgs()    



#minutes + venue + team + opp + start + pts_ma_1 + trb_ma_1 + tov_ma_1 + stl_ma_1 + ast_ma_1 + tp_ma_1 + fd_fp_ma_1 + venue + team + opp_pts_ma_1 + opp_trb_ma_1 + opp_tov_ma_1 + opp_stl_ma_1 + opp_ast_ma_1 + opp_pace_ma_1 + off_rtg + def_rtg + min_ma_1 + opp_pts_ma_1 + opp_tov_ma_1 + opp_tp_ma_1 + opp_pace_ma_1