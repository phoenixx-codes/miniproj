# Telegram .onion Link Extractor
This Tool connects to a **public Telegram Channel** using **Telethon** library and extracts all `.onion` URLs from recent messages. It saves the links in a structured JSON file.
## 🚀 Features
- Connects to Telegram using your phone number and API credentials
- Extracts `.onion` links using regular expressions
- Saves results to `onion_links.json` in a clean format
- Uses asynchronous code with `async/await`
## 🛠️ Setup Instructions
1. Install dependencies:
   ```bash
   pip install telethon
2.Create a Telegram app at https://my.telegram.org to get :
api_id
api_hash
3. run the script :python extract_onion_links.py
4.Enter your phone number and OTP when prompted.
5.The script connects to Telegram and starts extracting links from recent messages.

💾 Output Format
Each .onion link is saved in onion_links.json as a JSON object:

{
  "source": "telegram",
  "url": "http://exampleonionurl.onion",
  "discovered_at": "2025-05-17T12:34:56Z",
  "context": "Found in Telegram channel @toronionlinks",
  "status": "pending"
}

📌 Notes
Channel used for testing: @toronionlinks 
📄 License
This is a simple academic/learning project and is free to use or modify.

