import praw
import json

# Create a Reddit API instance
def create_api_instance():

    with open("./params/reddit_api_client.json", "r") as f:
        api_params = json.load(f)
        
    return praw.Reddit(
    client_id=api_params["client_id"],
    client_secret=api_params["client_secret"],
    user_agent=api_params["user_agent"],
    )
    

def get_top_submission_for_user(client, username, time_filter, limit):
    user = client.redditor(username)
    return user.submissions.top(time_filter=time_filter, limit=limit)

def get_top_comments_for_submission(submission, limit):
    submission.comments.replace_more(limit=limit)
    comments = submission.comments.list()
    
    # Sort comments by top (highest upvoted first)
    comments.sort(key=lambda x: x.score, reverse=True)
    
    top_10_comments = comments[:limit]
    
    return top_10_comments