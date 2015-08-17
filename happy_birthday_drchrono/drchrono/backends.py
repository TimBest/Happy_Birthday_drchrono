from social.backends.oauth import BaseOAuth2

class drchronoOAuth2(BaseOAuth2):
    """drchrono OAuth authentication backend"""
    name = 'drchrono'
    AUTHORIZATION_URL = 'https://drchrono.com/o/authorize/'
    ACCESS_TOKEN_URL = 'https://drchrono.com/o/token/'

    def get_user_details(self, response):
        """Return user details from drchrono account"""
        return {'username': response.get('login'),
                'email': response.get('email') or '',
                'first_name': response.get('name')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        #url = 'https://www.drchrono.com/api/users/current' + urlencode({
        #    'access_token': access_token
        #})
        #try:
            #return json.load(self.urlopen(url))
        #except ValueError:
        #    return None
        return None
