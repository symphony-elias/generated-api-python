import asyncio

from jose import jwt

import datetime


def urllib_post(token):
    from openapi_client_urllib import ApiClient, Configuration, AuthenticateRequest, AuthenticationApi
    request = AuthenticateRequest(token=token)
    configuration = Configuration(host="https://devx1.symphony.com/login")

    api = AuthenticationApi(ApiClient(configuration=configuration))
    post = api.pubkey_authenticate_post(authenticate_request=request)
    print(post)


async def aiohttp_post(token):
    from openapi_client_aio.api.authentication_api import AuthenticationApi
    from openapi_client_aio.api_client import ApiClient
    from openapi_client_aio.configuration import Configuration
    from openapi_client_aio.models.authenticate_request import AuthenticateRequest

    configuration = Configuration(host="https://develop2.symphony.com/login")
    client = ApiClient(configuration=configuration)
    api = AuthenticationApi(client)

    post = await api.pubkey_authenticate_post(authenticate_request=(AuthenticateRequest(token=token)))
    await client.close()

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
    asyncio.run(aiohttp_post(create_jwt()))
