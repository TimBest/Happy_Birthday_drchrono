import os

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

DRCHRONO_CLIENT_ID       = os.environ.get('DRCHRONO_CLIENT_ID', '1GB3JDpDxmcYFkJwxgfIHo6N3KHxlYzS54NOszay')
DRCHRONO_API_SECRET         = os.environ.get('DRCHRONO_API_SECRET', '')
