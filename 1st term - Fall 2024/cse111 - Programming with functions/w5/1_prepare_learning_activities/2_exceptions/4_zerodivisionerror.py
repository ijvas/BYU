# Example 4

# The computer raises a ZeroDivisionError when a program attempts to divide a number by zero (0)




def main():
  try:
    players = int(input("Enter the number of players: "))
    teams = int(input("Enter the number of teams: "))
    players_per_team = players / teams
    print(f"Each team should have {players_per_team} players")
  except ZeroDivisionError as zero_div_err:
    print(zero_div_err)
if __name__ == "__main__":
  main()



#   > python zero_div_error.py
# Enter the number of players: 20
# Enter the number of teams: 0
# division by zero