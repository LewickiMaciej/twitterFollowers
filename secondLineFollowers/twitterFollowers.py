from twitter import Api


class TwitterFollowers:
	
	def __init__(self, api):
		self.api = api

	def getFollowers(self, screen_name):
		first_line_followers = set()
		followers = self.api.GetFollowers(screen_name=screen_name)
		for follower in followers:
			first_line_followers.add(follower.screen_name)

		return first_line_followers

	def getSecondLine(self, first_line_followers):
		second_line_followers = {}
		set_of_second_line = set()
		for follower in first_line_followers:
			followers_of_follower = self.getFollowers(screen_name=follower)
			if followers_of_follower == None:
				continue
			self.addFollowersToList(
				second_line_followers, followers_of_follower, 
				set_of_second_line
			)
			
		return second_line_followers

	def addFollowersToList(self, second_line_followers, 
						   followers_of_follower, set_of_second_line):
		"""Add second line followers to dict of second line followers 
		or increase number which mean how much followers have this second line follower"""
		for follower in followers_of_follower:
			if follower in set_of_second_line:
				second_line_followers[follower] += 1
			else:
				set_of_second_line.add(follower)
				second_line_followers[follower] = 1

