from django.test import TestCase

from .twitterFollowers import TwitterFollowers


class TwitterAddFollowersToListTests(TestCase):

	def test_add_followers_to_list_only_insert(self):
		second_line_followers = {'aaa': 1, 'ccc': 1, 'eee': 1}
		followers_of_follower = {'bbb', 'ddd', 'fff'}
		set_of_second_line = {'aaa', 'ccc', 'eee'}
		result = {'aaa': 1, 'bbb': 1, 'ccc': 1, 'ddd': 1, 'eee': 1, 'fff': 1}

		TwitterFollowers.addFollowersToList(None, 
			second_line_followers, followers_of_follower, set_of_second_line
		)

		self.assertEqual(second_line_followers, result)

	def test_count_follower(self):
		second_line_followers = {'aaa': 2, 'ccc': 1, 'eee': 1}
		followers_of_follower = {'aaa', 'bbb', 'ddd', 'eee', 'fff'}
		set_of_second_line = {'aaa', 'ccc', 'eee'}
		result = {'aaa': 3, 'bbb': 1, 'ccc': 1, 'ddd': 1, 'eee': 2, 'fff': 1}

		TwitterFollowers.addFollowersToList(
			None, second_line_followers, 
			followers_of_follower, set_of_second_line
		)

		self.assertEqual(second_line_followers, result)

	def test_followers_are_longer(self):
		second_line_followers = {'aaa': 4, 'ccc': 7, 'eee': 2}
		followers_of_follower = {'aaa', 'bbb', 'ddd', 'fff', 'ggg'}
		set_of_second_line = {'aaa', 'ccc', 'eee'}
		result = {'aaa': 5, 'bbb': 1, 'ccc': 7, 'ddd': 1, 
				  'eee': 2, 'fff': 1, 'ggg': 1
		}

		TwitterFollowers.addFollowersToList(
			None, second_line_followers, 
			followers_of_follower, set_of_second_line
		)

		self.assertEqual(second_line_followers, result)

	def test_second_line_is_longer(self):
		second_line_followers = {'aaa': 4, 'ccc': 7, 'eee': 2}
		followers_of_follower = {'aaa', 'bbb'}
		set_of_second_line = {'aaa', 'ccc', 'eee'}
		result = {'aaa': 5, 'bbb': 1, 'ccc': 7, 'eee': 2}
		set_after = {'aaa', 'bbb', 'ccc', 'eee'}

		TwitterFollowers.addFollowersToList(
			None, second_line_followers, 
			followers_of_follower, set_of_second_line
		)

		self.assertEqual(set_after, set_of_second_line)
		self.assertEqual(second_line_followers, result)

	def test_second_line_is_empty(self):
		second_line_followers = {}
		followers_of_follower = {'aaa', 'bbb'}
		set_of_second_line = set()
		result = {'aaa': 1, 'bbb': 1}

		TwitterFollowers.addFollowersToList(
			None, second_line_followers, 
			followers_of_follower, set_of_second_line
		)

		self.assertEqual(second_line_followers, result)

	def test_followers_of_follower_is_empty(self):
		second_line_followers = {'aaa': 4, 'ccc': 7, 'eee': 2}
		followers_of_follower = set()
		set_of_second_line = {'aaa', 'ccc', 'eee'}
		result = {'aaa': 4, 'ccc': 7, 'eee': 2}

		TwitterFollowers.addFollowersToList(
			None, second_line_followers, 
			followers_of_follower, set_of_second_line
		)

		self.assertEqual(second_line_followers, result)
