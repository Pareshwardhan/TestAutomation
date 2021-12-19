from APIObjects.BaseAPI import BaseAPI


class GetAPI(BaseAPI):

    def __init__(self,requests,api_url):
        super().__init__(requests,api_url)

    resource_current_temp="/data/2.5/weather"
    def get_temp_by_city(self,city):

        params_get_by_city={"q": city, "APPID": "94fee91783be78104bc6b937ef9fcd7c"}
        response_json=self.get_getresponse(self.resource_current_temp,params_get_by_city).json()
        return  float(response_json["main"]["temp"] - 273.15)

