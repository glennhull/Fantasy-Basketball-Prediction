from stattlepy import Stattleship
import pandas as pd
import csv

new_query = Stattleship()
token = new_query.set_token('71c379b013f38f528b7c7461cea6a46e')
#output is a list of dicts, where each dict's values are lists of stats... list-dict-list-float (example of how data comes in)
output = new_query.ss_get_results(sport='basketball',league='nba',ep='player_season_stats',player_id='nba-brandon-ingram',on='today')

#find dict keys, then find the dict inside the dict keys
#print output[0].keys()
dct = output[0]['player_season_stats']
df = pd.DataFrame(dct)
#print df
#print output[0]['player_season_stats']
#for a in output[0]['game_logs']:
#    print a['three_pointers_pct']
nba_players = []
with open('players.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        row = str(row)
        row = row.replace(" ","-").replace("[","").replace("]","").replace("'","-")
        row = row[:-1]
        row = "nba" + row
        row = row.lower()
        nba_players.append(row)

def get_season_averages(player):
    print player
    output = new_query.ss_get_results(sport='basketball',league='nba',ep='player_season_stats',player_id=player,on='today')
    print output

get_season_averages(nba_players[100])
#minutes + venue + team + opp + start + pts_ma_1 + trb_ma_1 + tov_ma_1 + stl_ma_1 + ast_ma_1 + tp_ma_1 + fd_fp_ma_1 + venue + team + opp_pts_ma_1 + opp_trb_ma_1 + opp_tov_ma_1 + opp_stl_ma_1 + opp_ast_ma_1 + opp_pace_ma_1 + off_rtg + def_rtg + min_ma_1 + opp_pts_ma_1 + opp_tov_ma_1 + opp_tp_ma_1 + opp_pace_ma_1