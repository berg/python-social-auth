"""
App.net OAuth2 backend, docs at:
    http://psa.matiasaguirre.net/docs/backends/appdotnet.html
"""
from social.backends.oauth import BaseOAuth2


class AppDotNetOAuth2(BaseOAuth2):
    name = 'appdotnet'
    AUTHORIZATION_URL = 'https://account.app.net/oauth/authenticate'
    ACCESS_TOKEN_URL = 'https://account.app.net/oauth/access_token'
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_id(self, details, response):
        return response['data']['user']['id']

    def get_user_details(self, response):
        name = response['data']['user'].get('name') or ''
        name_parts = name.split(' ', 1)
        first_name = name_parts[0]
        last_name = ''
        if len(name_parts) > 1:
            last_name = name_parts[1]

        return {'username': response['data']['user']['username'],
                'fullname': name,
                'first_name': first_name,
                'last_name': last_name,
                'email': ''}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('https://alpha-api.app.net/stream/0/token',
                             params={'access_token': access_token})
