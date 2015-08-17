import requests
from social.backends.oauth import BaseOAuth2
from social.utils import handle_http_errors
from social.exceptions import AuthMissingParameter


class drchronoOAuth2(BaseOAuth2):
    """drchrono OAuth authentication backend"""
    name = 'drchrono'
    AUTHORIZATION_URL = 'https://drchrono.com/o/authorize/'
    ACCESS_TOKEN_URL = 'https://drchrono.com/o/token/'

    def get_user_details(self, response):
        """Return user details from drchrono account"""
        return {'username': response.get('username'),}

    '''def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://www.drchrono.com/o/token/' + urlencode({
            'access_token': access_token
        })
        try:
            return json.load(self.urlopen(url))
        except ValueError:
            return None'''

    @handle_http_errors
    def auth_complete(self, *args, **kwargs):
        """Completes loging process, must return user instance"""
        self.process_error(self.data)
        if not self.data.get('code'):
            raise AuthMissingParameter(self, 'code')

        state = self.validate_state()
        key, secret = self.get_key_and_secret()
        response = requests.post(self.ACCESS_TOKEN_URL, data={
            'code': self.data['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': self.get_redirect_uri(state),
            'client_id': key,
            'client_secret': secret,
        })
        response.raise_for_status()
        data = response.json()

        access_token = data['access_token']
        # TODO: Add token refreshing
        #refresh_token = data['refresh_token']
        #expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])
        data = self.user_data(access_token, *args, **kwargs)
        kwargs.update({'response': data, 'backend': self})
        return self.strategy.authenticate(*args, **kwargs)
