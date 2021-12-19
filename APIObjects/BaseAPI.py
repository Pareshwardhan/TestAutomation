class BaseAPI:
    def __init__(self,requests,api_url):
        self.requests=requests
        self.endpoint=api_url

    def get_getresponse(self,resource,params):
        url=self.endpoint+resource
        return self.requests.get(url, params=params)
