thonimport json

class InstagramParser:
    @staticmethod
    def parse_follower_data(follower_data):
        parsed_data = []
        for follower in follower_data:
            parsed_data.append({
                "id": follower["node"]["id"],
                "full_name": follower["node"]["full_name"],
                "profile_pic_url": follower["node"]["profile_pic_url"],
                "is_verified": follower["node"]["is_verified"],
                "followed_by_viewer": follower["node"]["followed_by_viewer"],
                "username": follower["node"]["username"],
                "requested_by_viewer": follower["node"]["requested_by_viewer"],
                "creators_username": follower["node"]["owner"]["username"],
                "status": "Following" if follower["node"]["followed_by_viewer"] else "Not Following"
            })
        return parsed_data