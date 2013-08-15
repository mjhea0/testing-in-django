from model_mommy import mommy
from django.test import TestCase
from whatevs.models import Forum, Thread

class WhateverTestMommy(TestCase):
	
	def test_forum_creation_mommy(self):
		new_forum = mommy.make('whatevs.Forum')
		new_thread = mommy.make('whatevs.Thread')
		self.assertTrue(isinstance(new_forum, Forum))
		self.assertTrue(isinstance(new_thread, Thread))
		self.assertEqual(new_forum.__unicode__(), new_forum.title)
		self.assertEqual(new_thread.__unicode__(), (str(new_thread.forum) + " - " + str(new_thread.title)))
