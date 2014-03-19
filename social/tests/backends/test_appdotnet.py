import json

from social.tests.backends.oauth import OAuth2Test


class AppDotNetOAuth2Test(OAuth2Test):
    backend_path = 'social.backends.appdotnet.AppDotNetOAuth2'
    user_data_url = 'https://alpha-api.app.net/stream/0/token'
    expected_username = 'testuser'
    access_token_body = json.dumps({
        'access_token': 'foobar',
        'token_type': 'bearer'
    })
    user_data_body = json.dumps({
        'data': {
            'app': {
                'client_id': 'test1',
                'link': 'http://test.example.com',
                'name': 'test client'
            },
            'client_id': 'test1',
            'invite_link': 'http://test.example.com/invite',
            'limits': {
                'available_invites': 0,
                'max_file_size': 0,
            },
            'scopes': [
                'basic',
            ],
            'storage': {
                'available': 1,
                'used': 0,
            },
            'user': {
                'avatar_image': {
                    'height': 640,
                    'is_default': False,
                    'url': 'http://avatar.example.com/image.jpg',
                    'width': 640
                },
                'canonical_url': 'https://alpha.app.net/testuser',
                'counts': {
                    'followers': 8060,
                    'following': 461,
                    'posts': 6418,
                    'stars': 648
                },
                'cover_image': {
                    'height': 1365,
                    'is_default': False,
                    'url': 'http://cover.example.com/image.jpg',
                    'width': 2048
                },
                'created_at': '2012-08-03T01:22:21Z',
                'description': {
                    'entities': {
                        'hashtags': [],
                        'links': [],
                        'mentions': []
                    },
                    'html': '<span itemscope="https://app.net/schemas/Post">'
                            'test</span>',
                    'text': 'test',
                },
                'id': '1',
                'locale': 'en_US',
                'name': 'Testy Testerson',
                'timezone': 'America/Los_Angeles',
                'type': 'human',
                'username': 'testuser',
            }
        },
        'meta': {
            'code': 200
        }
    })

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()
