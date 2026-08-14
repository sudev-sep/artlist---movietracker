from django.test import TestCase


class TokenEndpointTests(TestCase):
    def test_token_endpoint_accepts_trailing_newline_in_path(self):
        response = self.client.post('/api/token/\n', {'username': 'dummy', 'password': 'dummy'})

        self.assertNotEqual(response.status_code, 404)
