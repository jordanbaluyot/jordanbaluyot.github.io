#Research Fellows Task #1
import praw
import pandas as pd

# Initialize Reddit API Connection
reddit = praw.Reddit(client_id='****',
                     client_secret='****',
                     username='****',
                     password='****',
                     user_agent='*****')

# File name and reading CSV file
file_name = 'Loc_subreddit_list_active.csv'
file = pd.read_csv(file_name)

# Loop through all rows in the file and fetch subreddit descriptions
for index, row in file.iloc[:].iterrows():
    subreddit_name = row['Subreddit']
    try:
        subreddit = reddit.subreddit(subreddit_name)
        description = subreddit.public_description
        file.at[index, 'Description'] = description
        print(f"Fetched description for {subreddit_name}")
    except Exception as error:
        file.at[index, 'Description'] = 'Error fetching description'
        print(f"An error occurred for subreddit {subreddit_name}: {error}")

# Save the updated data back to the same CSV file
file.to_csv(file_name, index=False)
print("Updated CSV file saved to", file_name)
