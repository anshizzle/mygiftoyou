#!usr/bin/env/python

import praw

class RedditScraper:
	ACCEPTABLE_FILE_EXTENSIONS = ['gif', 'gifv']

	def __init__(self):
		self.user_agent = praw.Reddit(user_agent='my_gif_to_you')

	'''
		GET SUBMISSIONS
	'''
	def get_submissions_hot(self, subreddit, count):
		return self.user_agent.get_subreddit(subreddit).get_hot(limit=count)

	def get_submissions_top_all(self, subreddit, count):
		return self.user_agent.get_subreddit(subreddit).get_top_from_all(limit=count)

	def get_submissions_top_day(self, subreddit, count):
		return self.user_agent.get_subreddit(subreddit).get_top_from_day(limit=count)

	def get_submissions_top_month(self, subreddit, count):
		return self.user_agent.get_subreddit(subreddit).get_top_from_month(limit=count)

	def get_submissions_top_year(self, subreddit, count):
		return self.user_agent.get_subreddit(subreddit).get_top_from_year(limit=count)

	def get_author_submissions(self, submission, count):
		comment = submission.comments[0]
		author = comment.author
		author_submitted = author.get_submitted()

		temp_count = 0
		result = []
		for gif_submission in author_submitted:
			if temp_count >= count:
				return result
			result.append(gif_submission)
			count+=1
		return result

		#return [gif_submission for gif_submission in author_submitted[0:count] if is_gif(gif_submission)]

	'''
		GIF URL CHECKING
	'''
	def is_gif(self, url):
		if '.' in url:
			file_extension = url[url.rindex('.')+1:]
			if file_extension in self.ACCEPTABLE_FILE_EXTENSIONS:
				return True

		return False

	def is_gfycat(self, url):
		if 'gfycat.com' in url:
			return True

		return False


def main():
	r = RedditScraper()
	submissions = r.get_submissions_top_all('gifs', 1)

	for submission in submissions:
		if r.is_gif(submission.url):
			# write to db
			print submission.url
			print submission

			for author_sub in r.get_author_submissions(submission, 1):
				if r.is_gif(author_sub.url):
					print author_sub

		elif r.is_gfycat(submission.url):
			# write to db
			submission.url = submission.url.replace('gfycat.com', 'giant.gfycat.com') + '.gif'
			print submission.url
			print submission


if __name__ == "__main__":
	main()