import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python lookup.py [username]")
    sys.exit()

# Grab the argument properly
username = sys.argv[1].replace('@', '').strip()

# FixTweet API endpoint for reliable profile data retrieval
url = f"https://api.fxtwitter.com/{username}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print(f"Looking up ID for @{username}...")

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Safely check if the response format is JSON 
        try:
            data = response.json()
            user_info = data.get("user", {})
            user_id = user_info.get("id")

            if user_id:
                print(f"\nSuccess! Twitter ID: {user_id}")
            else:
                print("\nError: ID field missing from the user data.")
        except ValueError:
            print("\nError: API sent back a non-JSON page. The profile might be completely private.")

    elif response.status_code == 404:
        print("\nError: That username does not exist or is suspended.")
    else:
        print(f"\nServer responded with status code: {response.status_code}")

except Exception as e:
    print(f"\nNetwork Error: {e}")

