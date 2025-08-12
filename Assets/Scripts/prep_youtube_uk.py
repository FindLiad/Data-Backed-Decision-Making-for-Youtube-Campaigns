import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv() 

API_KEY = os.getenv("YOUTUBE_API_KEY")
API_VERSION = 'v3'

youtube = build('youtube', API_VERSION, developerKey=API_KEY)

def get_channel_stats(youtube, channel_identifier):
    # Accepts either a channel ID (UC...) or a handle (@name)
    params = {'part': 'snippet,statistics'}

    if isinstance(channel_identifier, str) and channel_identifier.startswith('UC'):
        params['id'] = channel_identifier
    else:
        # treat as a handle; strip leading '@' if present
        params['forHandle'] = str(channel_identifier).lstrip('@')

    response = youtube.channels().list(**params).execute()

    # Defensive: handle API error payloads (no 'items' key)
    if 'error' in response:
        print('YouTube API error:', response['error'])
        return None

    items = response.get('items', [])
    if items:
        item = items[0]
        return dict(
            channel_name=item['snippet']['title'],
            total_subscribers=item['statistics'].get('subscriberCount'),
            total_views=item['statistics'].get('viewCount'),
            total_videos=item['statistics'].get('videoCount'),
        )
    return None
 

# channel_id = "UC_aEa8K-EOJ3D6gOs7HcyNg" 
channel_id = "UC9LQwHZoucFT94I2h6JOcjw"
get_channel_stats(youtube, channel_id)

# Read CSV into dataframe 
df = pd.read_csv("youtube_data_united-kingdom.csv")

# Extract channel IDs and remove potential duplicates
channel_ids = df['NOMBRE'].str.split('@').str[-1].unique()

# Initialize a list to keep track of channel stats
channel_stats = []

# Loop over the channel IDs and get stats for each
for channel_id in channel_ids:
    stats = get_channel_stats(youtube, channel_id)
    if stats is not None:
        channel_stats.append(stats)

# Convert the list of stats to a df
stats_df = pd.DataFrame(channel_stats)

df.reset_index(drop=True, inplace=True)
stats_df.reset_index(drop=True, inplace=True)

# Concatenate the dataframes horizontally
combined_df = pd.concat([df, stats_df], axis=1)

# Save the merged dataframe back into a CSV file
combined_df.to_csv('updated_youtube_data_uk.csv', index=False)

combined_df.head(10)

