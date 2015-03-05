from django.test import TestCase


class StupidTest(TestCase):

    def test_should_pass_allways(self):
        self.assertEqual(True, True)
