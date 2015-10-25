#!usr/bin/env

import praw

class RedditScraper:
	def __init__(self):
		self.user_agent = praw.Reddit(user_agent='my_gift_to_you')

	def get_submissions_hot(self, subreddit, count):
		return self.user_agent.get_subreddit(subreddit).get_hot(limit=count)

	def get_submissions_top(self, subreddit, count):
		return self.user_agent.get_subreddit(subreddit).get_top(limit=count)


def main():
	r = RedditScraper()
	for submission in r.get_submissions():
		print submission.url

if __name__ == "__main__":
	main()