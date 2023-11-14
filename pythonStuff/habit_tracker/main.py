import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit

def main():
    habits: [Habit] = [
        track_habit("Coffee", datetime(2023, 11, 1, 8), cost=1, minutes_used=5),
        track_habit("Smoking", datetime(2023, 11, 1, 8), cost=15, minutes_used=60)
    ]
    
    df = pd.DataFrame(habits)
    print(tabulate(df, headers="keys", tablefmt="psql"))


if __name__ == "__main__":
    main()