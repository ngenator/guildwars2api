import requests

from guildwars2api.resources import (GuildDetails, EventNames, MapNames, WorldNames, Matches, MatchDetails, 
                                     ObjectiveNames, Items, ItemDetails, Recipes, RecipeDetails, ItemsV2, 
                                     RecipesV2, Skins, Skin_Details)


class GuildWars2API(object):
    """
    Guild Wars 2 API wrapper for python
    """

    API_SERVER = "https://api.guildwars2.com"
    API_VERSION = "v1"

    def __init__(self, api_server=API_SERVER, api_version=API_VERSION):
        """
        :param api_server: The location of the Guild Wars 2 API
        :param api_version: The Guild Wars 2 API Version
        """

        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Guild Wars 2 Python API Wrapper', 'Accept': 'application/json'})
        self.options = {
            'api_server': api_server,
            'api_version': api_version,
        }

        if (api_version == 'v2'):
            self.items = self._prepare(ItemsV2)
            self.recipes = self._prepare(RecipesV2)
        elif (api_version =='v1'):
            self.items = self._prepare(Items)
            self.recipes = self._prepare(Recipes)
            self.event_names = self._prepare(EventNames)
            self.map_names = self._prepare(MapNames)
            self.world_names = self._prepare(WorldNames)
            self.matches = self._prepare(Matches)
            self.match_details = self._prepare(MatchDetails)
            self.objective_names = self._prepare(ObjectiveNames)
            self.item_details = self._prepare(ItemDetails)
            self.recipe_details = self._prepare(RecipeDetails)
            self.guild_details = self._prepare(GuildDetails)
            self.skins = self._prepare(Skins)
            self.skin_details = self._prepare(Skin_Details)
            # self.events = self._prepare(Events)
        else: # Default to v1
            self.items = self._prepare(Items)
            self.recipes = self._prepare(Recipes)
            self.event_names = self._prepare(EventNames)
            self.map_names = self._prepare(MapNames)
            self.world_names = self._prepare(WorldNames)
            self.matches = self._prepare(Matches)
            self.match_details = self._prepare(MatchDetails)
            self.objective_names = self._prepare(ObjectiveNames)
            self.item_details = self._prepare(ItemDetails)
            self.recipe_details = self._prepare(RecipeDetails)
            self.guild_details = self._prepare(GuildDetails)
            self.skins = self._prepare(Skins)
            self.skin_details = self._prepare(Skin_Details)
            # self.events = self._prepare(Events)
    
    def _prepare(self, resource):
        return resource(self.options, self.session)

