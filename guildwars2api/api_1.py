from guildwars2api.resources import Resource, NoParamsMixin, NameLookupMixin
from math import floor

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


class Items(Resource, NoParamsMixin):
    api_class = 'items'
    api_return = True
    
    
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
    
    
class RecipeDetails(Resource):
    api_class = 'recipe_details'

    def get(self, recipe_id):
        """
        :param recipe_id: The recipe_id to get details for
        :return: The recipe for the given recipe_id
        """
        return super(RecipeDetails, self).get(recipe_id=recipe_id)


class Skins(Resource, NoParamsMixin):
    api_class = 'skins'
    api_return = True
    
class Skin_Details(Resource):
    api_class = 'skin_details'
    
    def get(self, skin_id, lang=None):
        """
        :param skin_id: The skin_id to get details for
        :return: The skin for the given skin_id
        """
        return super(Skin_Details, self).get(skin_id=skin_id, lang=lang)
    
    
class WvWResource(Resource):
    api_type = 'wvw'
    
    
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
    
    
class Continents(Resource, NameLookupMixin):
    api_class = "continents"
    
    
class Maps(Resource):
    api_class = "maps"
    
    def get(self, map_id=None):
        """
        :param map_id: The map_id to get details for
        :return: The details of the given map
        """
        
        return super(Maps, self).get(map_id=map_id)
    
class Map_Floor(Resource):
    api_class = "map_floor"
    
    def get(self, continent_id, floor, lang=None):
        """
        :param continent_id: The continent_id to get details for
        :floor floor: The floor of the continenet to get details for
        :param lang: The language the results will be returned in, supported languages: en, fr, de, es
        :return: The details of the map floor.
        """
        
        return super(Map_Floor, self).get(continent_id=continent_id, floor=floor, lang=lang)
    

class Build(Resource, NoParamsMixin):
    api_class = "build"
    
    
class Colors(Resource, NameLookupMixin):
    api_class = "colors"
    

class Files(Resource, NoParamsMixin):
    api_class = "files"
    
    