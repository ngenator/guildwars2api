import logging

from urllib.parse import urlencode



class GuildWars2APIError(Exception):
    """
    Exception upon recieving bad error, usually due to bad url link.
    'url' is the url that recieved bad data
    """
    def __init__(self, url):
        self.url = url
    def __str__(self):
        return repr(self.url)


def raise_on_error(data, url):
    """
    :param data: data recieved from the Guild Wars 2 api server
    """
    if 'error' in data:
        text = data.get('text', 'Unknown Error')
        raise GuildWars2APIError(url)


class Resource(object):
    """
    GuildWars2 API Resource

    `api_type` determines the relative url of the resource
    `api_class` determines the json resource being requested
    `api_return` determines the name of the object the api is expected to return, if set to True, uses `api_class` value
    """

    api_type = None
    api_class = None
    api_return = None
    url = None
    
    def __init__(self, options, session):
        """
        :param options:
        :param session:
        :raise: LookupError on missing `api_class` property
        """

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug('options:%s' % str(options))

        self.options = options
        self.session = session

        if self.api_class is None:
            raise LookupError("The `api_class` property needs to be set on %s" % self.__class__.__name__)


    def get(self, **kwargs):
        """
        Get the data from the API and return the values
        """

        self.url = self._build_url(**kwargs)
        r = self.session.get(self.url)
        data = r.json()
        raise_on_error(data, self.url)
        
        if self.api_return is not None and self.api_return in data:
            return data[self.api_return]
        elif self.api_return == True and self.api_class in data:
            return data[self.api_class]
        else:
            return data


    def _build_url(self, **kwargs):
        """
        Build the correct URL
        """
        # If any keyword arguments are empty, remove from list
        result = {}
        result.update((k, v) for k, v in kwargs.items() if v is not None)
                
                
        url_data = self.options.copy()
        url_data.update({
            'api_type': '/' if self.api_type is None else '/%s/' % self.api_type,
            'api_resource': self.api_class,
            'api_parameters': urlencode(result, safe=","),
        })

        url = "%(api_server)s/%(api_version)s%(api_type)s%(api_resource)s?%(api_parameters)s" % url_data
        self.logger.debug('url:%s' % url)

        return url
        
        
class NameLookupMixin(object):
    """
    Mixin for resources that only take a lang parameter and return a list of id/name mappings
    """

    def get(self, lang=None):
        """
        :param lang: The language to return, currently supported languages: en, fr, de, es
        :return: List of names with their corresponding id for the given language
        """

        return super(NameLookupMixin, self).get(lang=lang)


class NoParamsMixin(object):
    """
    Mixin for resources that don't take parameters
    """

    def get(self):
        return super(NoParamsMixin, self).get()


class IDsLookupMixin(object):
    """
    Mixin for resources that can take a list of ids or a single ID and the lang parameter and then returns 
    a list of id/name mappings
    """
    def get(self, ids=None, lang=None):
        """
        :param ids: A list of ids to look up
        :param lang: The language to return, currently supported languages: en, fr, de, es
        :return: Either returns a list of ids or detailed info of searched id
        """
         
        return super(IDsLookupMixin, self).get(ids=ids, lang=lang)
        
    def get(self, id=None, lang=None):
        """
        :param ids: A list of ids to look up
        :param lang: The language to return, currently supported languages: en, fr, de, es
        :return: Either returns a list of ids or detailed info of searched id
        """
        
        return super(IDsLookupMixin, self).get(id=id, lang=lang)
        
        
        