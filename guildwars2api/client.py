import requests

from guildwars2api.resources import Events, EventNames, MapNames, WorldNames, Matches, MatchDetails, ObjectiveNames


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

        self.events = Events(self.options, self.session)
        self.event_names = EventNames(self.options, self.session)
        self.map_names = MapNames(self.options, self.session)
        self.world_names = WorldNames(self.options, self.session)
        self.matches = Matches(self.options, self.session)
        self.match_details = MatchDetails(self.options, self.session)
        self.objective_names = ObjectiveNames(self.options, self.session)
