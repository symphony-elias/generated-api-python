import asyncio

from jose import jwt

import datetime


def urllib_post(token):
    from openapi_client_urllib import Configuration, ApiClient
    from openapi_client_urllib.api.authentication_api import AuthenticationApi
    from openapi_client_urllib.model.authenticate_request import AuthenticateRequest
    request = AuthenticateRequest(token=token)
    configuration = Configuration(host="https://develop2.symphony.com/login")

    api = AuthenticationApi(ApiClient(configuration=configuration))
    post = api.pubkey_authenticate_post(authenticate_request=request)
    print(post)


async def aio_post(token):
    from openapi_client_aio import Configuration, ApiClient
    from openapi_client_aio.api.authentication_api import AuthenticationApi
    from openapi_client_aio.model.authenticate_request import AuthenticateRequest

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
    asyncio.run(aio_post(create_jwt()))
