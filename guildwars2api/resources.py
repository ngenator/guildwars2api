import logging

from urllib.parse import urlencode


class GuildWars2APIError(Exception):
    pass


def raise_on_error(data):
    if 'error' in data:
        text = data.get('text', 'Unknown Error')
        raise GuildWars2APIError(text)


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

        url = self._build_url(**kwargs)
        r = self.session.get(url)
        data = r.json()
        raise_on_error(data)

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

        url_data = self.options.copy()
        url_data.update({
            'api_type': '/' if self.api_type is None else '/%s/' % self.api_type,
            'api_resource': self.api_class,
            'api_parameters': urlencode(kwargs),
        })

        url = "%(api_server)s/%(api_version)s%(api_type)s%(api_resource)s.json?%(api_parameters)s" % url_data
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


class WvWResource(Resource):
    api_type = 'wvw'


# class Events(Resource):
#     api_class = 'events'
#     api_return = True
# 
#     def get(self, world_id=None, map_id=None, event_id=None):
#         """
#         :param world_id: The world_id for the events
#         :param map_id: The map_id for the events
#         :param event_id: The event_id for the events
#         :return: List of events for the given world_id, map_id, and event_id
#         """
# 
#         return super(Events, self).get(world_id=world_id, map_id=map_id, event_id=event_id)


class EventNames(Resource, NameLookupMixin):
    api_class = 'event_names'


class MapNames(Resource, NameLookupMixin):
    api_class = 'map_names'


class WorldNames(Resource, NameLookupMixin):
    api_class = 'world_names'


class Matches(WvWResource, NoParamsMixin):
    api_class = 'matches'
    api_return = 'wvw_matches'


class MatchDetails(WvWResource):
    api_class = 'match_details'

    def get(self, match_id):
        """
        :param match_id: The match_id to get details for
        :return: The details for the given match_id
        """

        return super(MatchDetails, self).get(match_id=match_id)


class ObjectiveNames(WvWResource, NameLookupMixin):
    api_class = 'objective_names'


class Items(Resource, NoParamsMixin):
    api_class = 'items'
    api_return = True

class ItemsV2(Resource):
    api_class = 'items'
    
    def get(self, item_id=None, lang=None):
        """
        :param item_id: The item_id to get details for
        :param lang: The language the results will be returned in, supported languages: en, fr, de, es
        :return: Details about the item for the given item_id
        """
        return super(ItemsV2, self).get(item_id=item_id, lang=lang)
    
class ItemDetails(Resource):
    api_class = 'item_details'

    def get(self, item_id, lang=None):
        """
        :param item_id: The item_id to get details for
        :param lang: The language the results will be returned in, supported languages: en, fr, de, es
        :return: Details about the item for the given item_id
        """
        return super(ItemDetails, self).get(item_id=item_id, lang=lang)


class Recipes(Resource, NoParamsMixin):
    api_class = 'recipes'
    api_return = True


class RecipesV2(Resource):
    api_class = 'recipes'
    
    def get(self, recipe_id=None):
        """
        :param recipe_id: The recipe_id to get details for
        :return: The recipe for the given recipe_id
        """
        return super(RecipesV2, self).get(recipe_id=recipe_id)
    
    
class RecipeDetails(Resource):
    api_class = 'recipe_details'

    def get(self, recipe_id):
        """
        :param recipe_id: The recipe_id to get details for
        :return: The recipe for the given recipe_id
        """
        return super(RecipeDetails, self).get(recipe_id=recipe_id)


class GuildDetails(Resource):
    api_class = 'guild_details'

    def get_by_name(self, guild_name):
        """
        :param guild_name: The name of the guild to get details for
        """
        return super(GuildDetails, self).get(guild_name=guild_name)

    def get_by_id(self, guild_id):
        """
        :param guild_id: The id of the guild to get details for
        """
        return super(GuildDetails, self).get(guild_id=guild_id)


class Skins(Resource, NoParamsMixin):
    api_class = 'skins'
    api_return = True
    
class Skin_Details(Resource):
    api_class = 'skin_details'
    
    def get(self, skin_id):
        """
        :param recipe_id: The skin_id to get details for
        :return: The skin for the given skin_id
        """
        return super(Skin_Details, self).get(skin_id=skin_id)