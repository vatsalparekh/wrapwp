from attrdict import AttrDict
import requests


class WordPress(object):
    def __init__(self, base_url, api_root='/wp-json'):
        self.base_url = base_url
        self.api_root = api_root
        self.api_url = self.base_url + self.api_root

    def __repr__(self):
        return '[' + self.base_url + ']'

    @property
    def wp_json(self):
        return AttrDict(requests.get(self.api_url).json())

    def fetch_meta(self):
        wp_json = self.wp_json
        self.meta = AttrDict({
            'name': wp_json.name,
            'description': wp_json.description,
            'url': wp_json.url,
            'home': wp_json.home,
            'gmt_offset': wp_json.gmt_offset,
            'timezone_string': wp_json.timezone_string
        })

    class Posts(object):
        pass

    class Pages(object):
        pass
