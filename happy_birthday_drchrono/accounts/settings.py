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

SOCIAL_AUTH_DRCHRONO_KEY  = os.environ.get('DRCHRONO_CLIENT_ID', 'Riowa6L4VwMruzpWfL1DAs0jFuf7Gsd2xP9IfFsF')
SOCIAL_AUTH_DRCHRONO_SECRET = os.environ.get('DRCHRONO_API_SECRET', '')
# TODO: define the scope parameters of this app 
