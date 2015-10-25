#!usr/bin/env/python

import praw

class RedditScraper:
	ACCEPTABLE_FILE_EXTENSIONS = ['gif', 'gifv']

	def __init__(self):
		self.user_agent = praw.Reddit(user_agent='my_gift_to_you')

	def get_submissions_hot(self, subreddit, count):
		return self.user_agent.get_subreddit(subreddit).get_hot(limit=count)

	def get_submissions_top(self, subreddit, count):
		return self.user_agent.get_subreddit(subreddit).get_top(limit=count)

	def is_gif(self, submission):
		url = submission.url

		if '.' in url:
			file_extension = url[url.rindex('.')+1:]
			if file_extension in self.ACCEPTABLE_FILE_EXTENSIONS:
				return True

		return False

	def is_gfycat(self, submission):
		url = submission.url

		if 'gfycat.com' in url:
			return True

		return False


def main():
	r = RedditScraper()
	submissions = r.get_submissions_top('naturegifs', 1)

	for submission in submissions:
		if r.is_gif(submission):
			# write to db
			print submission.url
			print submission
		elif r.is_gfycat(submission):
			# write to db
			submission.url = submission.url.replace('gfycat.com', 'giant.gfycat.com') + '.gif'
			print submission.url
			print submission


if __name__ == "__main__":
	main()