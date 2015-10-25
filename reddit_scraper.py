#!usr/bin/env

import praw

class RedditScraper:
	def __init__(self):
		self.user_agent = praw.Reddit(user_agent='my_gift_to_you')

	def get_submissions(self):
		return self.user_agent.get_subreddit('opensource').get_hot(limit=5)

def main():
	r = RedditScraper()
	for submission in r.get_submissions():
		print submission.url

if __name__ == "__main__":
	main()