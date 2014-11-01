import requests

class CustomSearch:
    URL_TEMPLATE = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s"

    def __init__(self, api_key, search_engine_id):
        self.api_key = api_key
        self.search_engine_id = search_engine_id

    def get(self, params):
        params_string = ''.join(['&'+key+'='+value for key, value in params.iteritems()])
        final_url = self.URL_TEMPLATE % (self.api_key, self.search_engine_id) + params_string
        return requests.get(final_url).json()

    @classmethod
    def extract_pictures_urls(cls, resp):
        urls = []
        for item in resp[u'items']:
            try:
                urls.append(item[u'pagemap'][u'cse_image'][0][u'src'])
            except:
                pass
        return urls