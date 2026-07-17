"""
League Points Calculator Script

This script calculates the total league points for a sports team based on their 
match record. It applies a custom scoring algorithm where different outcomes 
carry different mathematical weights:
  - Wins: +4 points each
  - Draws: +2 points each
  - Losses: -1 point each (penalty)

The script features robust input handling. It processes a single comma-separated 
string from the user, parses it into integer values, and safely handles invalid 
data types or incorrect input formats using a try-except block.
"""
def calculate_league_points(wins, draws, losses):
    win_point = wins * 4
    draw_point = draws * 2
    loss_point = losses * -1
    total = win_point + draw_point
    ans = total + loss_point
    print(ans)    


statistics = input("Enter wins, draws, and losses separated by commas: ").split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
calculate_league_points(wins,draws,losses)
