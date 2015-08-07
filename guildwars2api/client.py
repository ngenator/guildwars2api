import requests

import guildwars2api.api_2 as v2
import guildwars2api.api_1 as v1

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
            self.items = self._prepare(v2.Items)
            self.recipes = self._prepare(v2.Recipes)
            self.skins = self._prepare(v2.Skins)
        elif (api_version =='v1'):
            self.items = self._prepare(v1.Items)
            self.recipes = self._prepare(v1.Recipes)
            self.recipe_details = self._prepare(v1.RecipeDetails)
            self.item_details = self._prepare(v1.ItemDetails)
            self.skins = self._prepare(v1.Skins)
            self.skin_details = self._prepare(v1.Skin_Details)
            self.matches = self._prepare(v1.Matches)
            self.match_details = self._prepare(v1.MatchDetails)
            self.objective_names = self._prepare(v1.ObjectiveNames)
            self.event_names = self._prepare(v1.EventNames)
            self.map_names = self._prepare(v1.MapNames)
            self.world_names = self._prepare(v1.WorldNames)
            self.guild_details = self._prepare(v1.GuildDetails)
            self.continents = self._prepare(v1.Continents)
            self.maps = self._prepare(v1.Maps)
            self.map_floor = self._prepare(v1.Map_Floor)
            self.build = self._prepare(v1.Build)
        else:
            raise ValueError("Only v1 or v2 accepted")
    
    def _prepare(self, resource):
        return resource(self.options, self.session)

