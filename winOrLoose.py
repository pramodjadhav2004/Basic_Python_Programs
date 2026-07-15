#to compare the points of two teams and print whether team A wins, loses or draws with team B
def compare(team_a_points, team_b_points):
    if (team_a_points>team_b_points):
        return "Win"
    elif (team_a_points==team_b_points):
        return "Draw"
    elif (team_a_points<team_b_points):
        return "Lose"
    

team_a_points = int(input("Enter the points of team A: "))
team_b_points = int(input("Enter the points of team B: "))

compare_result = compare(team_a_points, team_b_points)

print(compare_result)