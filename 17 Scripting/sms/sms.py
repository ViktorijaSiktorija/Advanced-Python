# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

account_sid = 'broj sida'
auth_token = 'token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="I AM the hacker womaaan",
                    from_='+broj',
                    to='+mojBroj'
                )

print(message.sid)
