import asyncio

TOKEN = 'eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJwb3N0bWFuLWVjcm96ZSIsImV4cCI6MTYxMDExMzE3NX0.fPtsdm1cpckxNW-RsMEBNFhk9X56IDZtN-9qgIxNzkSMoFFEixQzY-1YT6iysIpAg2VcsgPHfx67joEWXeZLdBrtjTl6qlPbovFOUgoE77aaIp88hrCrnZB3FP69fzbA-NgE18i_6CSJNz0qq7XjzLr8cfeBgQy5bkl9ZavZUO-dftypkQvqJfoeoAtp5harsfmJlQsDn1E8GqykD0_9T4rP0TRbwReHIIczT9sfWJdI8Bbh2iORQCV9w1w-PMpSedjnBufQhjTFrE2doSfeKazrGj0Q87Xcl-_rRQeBxqGLPyrV4-S8o1AeOjPR58F11JfQZ1ZY3Ah8qHZTdaWbT7ed6KY0qks-6_Aq0NxplNNIC5d4rjxSQT6chHJ6YDBipp6RfbY_2b7fuJRxYK3PlcQMtWXngVhEyHUh15hjvgEzR6vH3g5i4JKJJRyUsA3Ct5-xbquB4c7u_ciA3kHgRL_UXw1WCz_IYDF4sAtqOwc4sNohIZCT74PWnppw62kSn6hwssA1Y2qzc6IDAAigkEuwLjAdTVSg3y453je893jSB7CyFPRjqdcsduRkuMNxHD-0Mc16Xnu0IRFTDXbtXCDcnBxnCXzZuxRVsf8obC4WpparEESy119_Hu_KZXROv-qGt8h7Iv36kz_t6W1Wagb7caOUjCUJNgzdEusP0Lo'


def urllib_post():
    from openapi_client_urllib import ApiClient, Configuration, AuthenticateRequest, AuthenticationApi
    request = AuthenticateRequest(token=TOKEN)
    configuration = Configuration(host="https://devx1.symphony.com/login")

    api = AuthenticationApi(ApiClient(configuration=configuration))
    post = api.pubkey_authenticate_post(authenticate_request=request)
    print(post)


def aiohttp_post():
    from openapi_client_aio.api.authentication_api import AuthenticationApi
    from openapi_client_aio.api_client import ApiClient
    from openapi_client_aio.configuration import Configuration
    from openapi_client_aio.models.authenticate_request import AuthenticateRequest

    request = AuthenticateRequest(token=TOKEN)
    configuration = Configuration(host="https://devx1.symphony.com/login")
    api = AuthenticationApi(ApiClient(configuration=configuration))

    loop = asyncio.get_event_loop()
    post = loop.run_until_complete(api.pubkey_authenticate_post(authenticate_request=request, async_req=True).get())
    loop.close()

    print(post)


if __name__ == "__main__":
    aiohttp_post()
