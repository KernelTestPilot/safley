import pandas as pd

df = pd.read_json("users.json")

# Age groups
def age_group(age):
    if age < 30:
        return "young"
    elif age < 50:
        return "middle"
    else:
        return "senior"

df["age_group"] = df["age"].apply(age_group)

# Time of day
df["created_at"] = pd.to_datetime(df["created_at"])

def time_of_day(hour):
    if hour < 12:
        return "morning"
    elif hour < 18:
        return "afternoon"
    else:
        return "evening"

df["time_of_day"] = df["created_at"].dt.hour.apply(time_of_day)

# Filter failures
fail_df = df[df["success"] == False]

# Group
grouped = fail_df.groupby(["age_group", "time_of_day", "gender"]).size()

print(grouped)