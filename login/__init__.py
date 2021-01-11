import asyncio

import urllib3
from jose import jwt

import datetime


def urllib_post(token):
    from openapi_client_urllib import ApiClient, Configuration, AuthenticateRequest, AuthenticationApi
    request = AuthenticateRequest(token=token)
    configuration = Configuration(host="https://develop2.symphony.com/login")
    configuration.proxy = "http://127.0.0.1:3128"  # for proxy
    configuration.proxy_headers = urllib3.util.make_headers(proxy_basic_auth='proxyuser:passw0rd') # for proxy basic authentication

    api = AuthenticationApi(ApiClient(configuration=configuration))
    post = api.pubkey_authenticate_post(authenticate_request=request)
    print(post)


def get_key():
    with open('/Users/elias.croze/.symphony/fbbot_privatekey.pkcs8', 'r') as f:
        content = f.readlines()
        key = ''.join(content)
        return key


def create_jwt():
    private_key = get_key()
    expiration_date = int(datetime.datetime.now(datetime.timezone.utc).timestamp() + (5 * 58))
    payload = {
        'sub': "postman-ecroze",
        'exp': expiration_date
    }
    return jwt.encode(payload, private_key, algorithm='RS512')


if __name__ == "__main__":
    urllib_post(create_jwt())
