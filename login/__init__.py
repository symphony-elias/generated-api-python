import asyncio

from jose import jwt

import datetime

from aiohttp_gen_api import Configuration, ApiClient
from aiohttp_gen_api.api.authentication_api import AuthenticationApi
from aiohttp_gen_api.api.messages_api import MessagesApi
from aiohttp_gen_api.model.authenticate_request import AuthenticateRequest


async def get_session_token(token):
    configuration = Configuration(host="https://develop2.symphony.com/login")
    configuration.verify_ssl = True
    configuration.cert_file = "/Users/elias.croze/.symphony/develop2.cert"
    client = ApiClient(configuration=configuration)
    api = AuthenticationApi(client)

    post = await api.pubkey_authenticate_post(authenticate_request=(AuthenticateRequest(token=token)))
    await client.close()
    return post.token


async def get_km_token(token):
    configuration = Configuration(host="https://develop2.symphony.com/relay")
    client = ApiClient(configuration=configuration)
    api = AuthenticationApi(client)

    post = await api.pubkey_authenticate_post(authenticate_request=(AuthenticateRequest(token=token)))
    await client.close()
    return post.token


async def authenticate(token):
    return await get_session_token(token), await get_km_token(token)


def get_key():
    with open("/Users/elias.croze/.symphony/fbbot_privatekey.pkcs8", "r") as f:
        content = f.readlines()
        key = "".join(content)
        return key


def create_jwt():
    private_key = get_key()
    expiration_date = int(datetime.datetime.now(datetime.timezone.utc).timestamp() + (5 * 58))
    payload = {
        "sub": "postman-ecroze",
        "exp": expiration_date
    }
    return jwt.encode(payload, private_key, algorithm="RS512")


async def send_message(session_token, km_token):
    configuration = Configuration(host="https://develop2.symphony.com/agent")
    client = ApiClient(configuration=configuration)
    api = MessagesApi(api_client=client)

    resp = await api.v4_stream_sid_message_create_post(sid="hyVxIm1YkYIy2I90Hny-Bn___okPIOj2dA",
                                                       session_token=session_token, key_manager_token=km_token,
                                                       message="<messageML>Hello world!</messageML>",
                                                       attachment=open("/Users/elias.croze/Downloads/lenna.png", "rb"))
    await client.close()
    print(resp)


async def authenticate_send_message():
    session_token, km_token = await authenticate(create_jwt())
    await send_message(session_token, km_token)


if __name__ == "__main__":
    asyncio.run(authenticate_send_message())
