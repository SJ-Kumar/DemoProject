 # Imports
import os
import pprint
from requests_oauthlib import OAuth2Session

 # Set environment variables
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

 # Credentials you get from registering a new application
client_id = '868cwwcr8rjojs'
client_secret = 'TY3x27KzObVZOTDs'

 # LinkedIn OAuth2 requests require scope and redirect_url parameters.
 # Ensure these values match the auth values in your LinkedIn App
 # (see auth tab on LinkedIn Developer page)
scope = ['r_liteprofile']
redirect_url = 'https://margamfarms.onrender.com/'

 # OAuth endpoints given in the LinkedIn API documentation
authorization_base_url = 'https://www.linkedin.com/oauth/v2/authorization'

token_url = 'https://www.linkedin.com/oauth/v2/accessToken'

linkedin = OAuth2Session(client_id, redirect_uri='https://margamfarms.onrender.com/', scope=scope)

 # Redirect user to LinkedIn for authorization
authorization_url, state = linkedin.authorization_url(authorization_base_url)
print(f"Please go here and authorize: {authorization_url}")

 # Get the authorization verifier code from the callback url
redirect_response = input('Paste the full redirect URL here:')

 # Fetch the access token
linkedin.fetch_token(token_url, client_secret=client_secret,
                      include_client_id=True,
                      authorization_response=redirect_response)

 # Fetch a protected resource, i.e. user profile
r = linkedin.get('https://api.linkedin.com/v2/me')

# print(r.content)

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(r.json())