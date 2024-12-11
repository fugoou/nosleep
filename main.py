import os
import praw
import random

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

subreddit = reddit.subreddit("nosleep")
posts = list(subreddit.hot(limit=None))
post = random.choice(posts)

title = post.title
content = post.selftext
# author = post.author.name if post.author else "[deleted]"
# post_time = datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S UTC')

readme_content = (
    f"# {title}\n"
    # f"> Posted by: u/{author}  \n"
    # f"> Posted on: {post_time}  \n\n"
    f"{content}"
)

with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(readme_content)
