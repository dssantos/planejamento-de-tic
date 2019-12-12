from django.test import TestCase


class ReportTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/report2/')

    def test_get(self):
        """Get /report/ must return status 200"""
        self.assertEqual(200, self.resp.status_code)
