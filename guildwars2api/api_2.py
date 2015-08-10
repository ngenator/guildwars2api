from guildwars2api.resources import Resource, IDsLookupMixin, NoParamsMixin, IDAllMixin
from requests import sessions


class Skins(Resource, IDsLookupMixin):
    """
    Returns information about skins
    """
    
    api_class = 'skins'
    
    
class Recipes(Resource, IDsLookupMixin):
    """
    Returns information about recipes
    """
    
    api_class = 'recipes'
    

class Items(Resource, IDsLookupMixin):
    """
    Returns information about items
    """
    
    api_class = 'items'
    
    
class Materials(Resource, IDsLookupMixin):
    """
    Returns information about materials
    """
    
    api_class = 'materials'
    
    
class Search(Resource):
    """
    A search interface for recipes
    """
    
    api_type = 'recipes'
    api_class = 'search'
    
    def get_input(self, item_id=None):
        """
        :param item_id: The item_id when searching for recipes with an item as an ingredient
        :return: List of item_ids that has the input as an ingredient
        """
        
        return super(Search, self).get(input=item_id)
        
    def get_output(self, item_id=None):
        """
        :param item_id: The item id when searching for the recipes that craft an item.
        :return: List of item_ids that are used to make the searched item
        """
        
        return super(Search, self).get(output=item_id)
    
class Continents(Resource, IDsLookupMixin, IDAllMixin):
    """
    Returns a list of continents and information about each continent
    'floors' each continent contains a list of floors.
    """
    
    api_class = 'continents'
    floors = None
    
    class Floors(Resource, IDsLookupMixin, IDAllMixin):
        """
        Returns a list of floors and information about each floor
        'regions' each floor level contains a list of regions
        """
        
        api_type = 'continents'
        api_class = 'floors'    
        regions = None
        
        
        def get(self, continent_id, floor_ids=None, lang=None):
            """
            :param continent_id: the continent_id used to search for the given floor_id
            :param floor_id: the floor_id used to search for the given region_id
            :param lang: The language the results will be returned in, supported 
                        languages: en, fr, de, es
            :return: either a list of valid floor_ids or detailed info of given floor_ids
            """
            
            self.api_type = 'continents/' + str(continent_id)
            return super(Continents.Floors, self).get(ids=floor_ids, lang=lang)
        
        
        class Regions(Resource, IDsLookupMixin, IDAllMixin):
            """
            Returns a list of regions and information about each regions
            'maps' each region level contains a list of maps
            """
            
            api_type = 'continents'
            api_class = 'regions'
            maps = None
            
            
            def get(self, continent_id, floor_id, region_ids=None, lang=None):
                """
                :param continent_id: the continent_id used to search for the given floor_id
                :param floor_id: the floor_id used to search for the given region_id
                :param region_id: the region_id used to search for the given map_ids
                :param lang: The language the results will be returned in, supported 
                            languages: en, fr, de, es
                :return: either a list of valid region_ids or detailed info of given region_ids
                """
                self.api_type = 'continents/' + str(continent_id) + '/floors/' + str(floor_id)
                return super(Continents.Floors.Regions, self).get(ids=region_ids, lang=lang)
            
            
            class Maps(Resource, IDsLookupMixin, IDAllMixin):
                """
                Returns a list of maps and information about each map
                'sectors' each map level contains a list of sectors
                'pois' each map level contains a list of pois
                'tasks' each map level contains a list of tasks
                """
                api_type = 'continents'
                api_class = 'maps'
                
                sectors = None
                pois = None
                tasks = None
                
                
                def get(self, continent_id, floor_id, region_id, map_ids=None, lang=None):
                    """
                    :param continent_id: the continent_id used to search for the given floor_id
                    :param floor_id: the floor_id used to search for the given region_id
                    :param region_id: the region_id used to search for the given map_ids
                    :param map_ids: the map_ids to search for on the current region layer. If
                                no map_ids are given, a list of valid map_ids are given
                    :param lang: The language the results will be returned in, supported 
                                languages: en, fr, de, es
                    :return: either a list of valid map_ids or detailed info of given map_ids
                    """
                    
                    self.api_type = ('continents/' + str(continent_id) + '/floors/' + 
                                     str(floor_id) + '/regions/' + str(region_id))
                    return super(Continents.Floors.Regions.Maps, self).get(ids=map_ids, lang=lang)
                
                
                class Subresource(Resource, IDsLookupMixin, IDAllMixin):
                    """
                    Returns a list of choosen resource and information about each resource
                    Used to create the 3 sub-resources of maps: sectors, pois and tasks
                    """
                
                    api_type = 'continents'
                    api_class = None
                    
                    
                    def __init__(self, options, sessions, name):
                        self.api_class = name
                        super(Continents.Floors.Regions.Maps.Subresource, self).__init__(options, sessions)
                        
                        
                    def get(self, continent_id, floor_id, region_id, map_id, ids=None, lang=None):
                        """
                        :param continent_id: the continent_id used to search for the given floor_id
                        :param floor_id: the floor_id used to search for the given region_id
                        :param region_id: the region_id used to search for the given map_ids
                        :param map_ids: the map_id used to search for the given subresource
                        :param lang: The language the results will be returned in, supported 
                                    languages: en, fr, de, es
                        :return: either a list of valid subresource_ids or detailed information of given
                                subresource_ids
                        """
                        
                        self.api_type = ('continents/' + str(continent_id) + '/floors/' + 
                                     str(floor_id) + '/regions/' + str(region_id) + '/'  + '/maps/' + str(map_id))
                        return super(Continents.Floors.Regions.Maps.Subresource, self).get(ids=ids, lang=lang)
                    
                
                
class Maps(Resource, IDsLookupMixin):
    """
    Returns information about maps in the game
    """
    api_class ='maps'
    
    
class Build(Resource, NoParamsMixin):
    """
    Returns the current build id
    """
    api_class = 'build'
    
    
class Colors(Resource, IDsLookupMixin):
    """
    Returns information about dye colors
    """
    api_class = 'colors'
    
    
class Files(Resource, NoParamsMixin):
    """
    Returns commonly requested assets
    """
    api_class = 'files'
    