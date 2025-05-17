import re #for regular expressions
import json
import aiofiles
from datetime import datetime,timezone
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel #to access telegram channels


api_id=20625150
api_hash='8fa147edfeb3fa03a9c8a4bc4962b2bc'
channel_name= 'toronionlinks'

onion_regex=re.compile(r'https?://[a-zA-Z0-9]{15,56}\.onion')#regular expression to extract files containing .onion links
#15,56 are onion link character length
output_file='onion_links.json'#j

async def extract_onion_links():
    async with TelegramClient('onion session',api_id,api_hash) as client:
        print("Connected. Fetching messages...")

        async for message in client.iter_messages(channel_name, limit=100):#iterates thru messages from a telegram channel and fetches last 100 messages
            if message.message:#checks if current message isnt empty and has some content 
                found_links=onion_regex.findall(message.message)#returns all messages that match with regex
                for link in found_links:#iterates thru each found link
                    onion_data={   #creates a dictionary containing metadata about found link
                        "source":"telegram" ,
                        "url": link,
                        "discovered_at": datetime.now(timezone.utc).isoformat(),#cuttent utch timestamp with 'Z' timezone indicator
                        "context":f"Found in Telegram Channel @{channel_name}",
                        "status":"pending"#initial status set to pending 
                    }
                    async with aiofiles.open(output_file,'a') as f:
                        await f.write(json.dumps(onion_data)+"\n")#converts dictionary into json format
        print(f"Extraction complete. Links saved in {output_file}")

import asyncio
asyncio.run(extract_onion_links())            