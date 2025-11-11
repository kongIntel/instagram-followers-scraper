thonimport requests
import json
import time

class InstagramFollowerScraper:
    def __init__(self, sessionid, username):
        self.sessionid = sessionid
        self.username = username
        self.base_url = f'https://www.instagram.com/{username}/followers/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0',
            'Cookie': f'sessionid={sessionid};'
        }

    def get_followers(self, max_count=1000):
        followers = []
        after = ''
        while len(followers) < max_count:
            url = f"{self.base_url}?max_id={after}" if after else self.base_url
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                raise Exception(f"Error fetching data: {response.status_code}")
            data = response.json()

            followers.extend(data['data']['user']['edge_followed_by']['edges'])
            after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']
            if not after:
                break
            time.sleep(2)  # To avoid rate limiting

        return followers[:max_count]

    def save_to_json(self, followers, filename="followers_data.json"):
        with open(filename, 'w') as f:
            json.dump(followers, f, indent=4)

if __name__ == "__main__":
    sessionid = "YOUR_SESSION_ID"  # Replace with actual session ID
    username = "target_username"   # Replace with target Instagram username
    scraper = InstagramFollowerScraper(sessionid, username)
    followers = scraper.get_followers()
    scraper.save_to_json(followers)