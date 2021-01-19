from django.test import TestCase


class ImportTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/importpa/')

    def test_get(self):
        """Get /importpa/ must return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'importpa.html')