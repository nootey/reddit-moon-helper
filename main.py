import client.reddit as reddit_client
import pandas as pd

def append_data(data, comments):
    for comment in comments[:10]:
        comment_text = comment.body.lstrip('-')
        comment_text = comment_text.replace('\n', ' ').strip()
        data.append({"score": comment.score, "comment": comment_text})


def main():
    user = reddit_client.create_api_instance()
    submissions = reddit_client.get_top_submission_for_user(user, "CryptoDaily-", "week", 5)

    data = []
    
    for submission in submissions:
        print("Fetching comments for:", submission.title)
        top_10_comments = reddit_client.get_top_comments_for_submission(submission, 10)
        append_data(data, top_10_comments)

    data.sort(key=lambda x: x["score"], reverse=True)       
    df = pd.DataFrame(data)
    df.to_csv('data/top_comments.csv', index=False, columns=["score", "comment"])

if __name__ == '__main__':
    main()