from guildwars2api.resources import Resource, IDsLookupMixin
from requests import sessions


class Skins(Resource, IDsLookupMixin):
    api_class = 'skins'
    
    
class Recipes(Resource, IDsLookupMixin):
    api_class = 'recipes'
    

class Items(Resource, IDsLookupMixin):
    api_class = 'items'
    
    
class Materials(Resource, IDsLookupMixin):
    api_class = 'materials'
    
    
class Search(Resource):
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
    
class Continents(Resource, IDsLookupMixin):
    """
        'floors' each continent contains a layer of floors.
    """
    
    api_class = 'continents'
    floors = None
    
    class Floors(Resource, IDsLookupMixin):
        """
        
        """
        
        api_type = 'continents'
        api_class = 'floors'    
        regions = None
        
        
        def get(self, continent_id, floor_ids=None, lang=None):
            """
            :
            """
            self.api_type = 'continents/' + str(continent_id)
            return super(Continents.Floors, self).get(ids=floor_ids, lang=lang)
        
        
        def get_all(self):
            """
            :return: All continents of the Guild Wars universe
            """
        
            return super(Continents, self).get(ids="all")
        
        
        class Regions(Resource, IDsLookupMixin):
            """
            
            """
            
            api_type = 'continents'
            api_class = 'regions'
            maps = None
            
            
            def get(self, continent_id, floor_id, region_ids=None, lang=None):
                """
                :
                """
                self.api_type = 'continents/' + str(continent_id) + '/floors/' + str(floor_id)
                return super(Continents.Floors.Regions, self).get(ids=region_ids, lang=lang)
            
            
            class Maps(Resource, IDsLookupMixin):
                """
                
                """
                api_type = 'continents'
                api_class = 'maps'
                
                sectors = None
                pois = None
                tasks = None
                
                
                def get(self, continent_id, floor_id, region_id, map_ids=None, lang=None):
                    """
                    :
                    """
                    self.api_type = ('continents/' + str(continent_id) + '/floors/' + 
                                     str(floor_id) + '/regions/' + str(region_id))
                    return super(Continents.Floors.Regions.Maps, self).get(ids=map_ids, lang=lang)
                
                
                class Subresource(Resource, IDsLookupMixin):
                    """
                    
                    """
                
                    api_type = 'continents'
                    api_class = None
                    
                    
                    def __init__(self, options, sessions, name):
                        self.api_class = name
                        super(Continents.Floors.Regions.Maps.Subresource, self).__init__(options, sessions)
                        
                        
                    def get(self, continent_id, floor_id, region_id, map_id, ids=None, lang=None):
                        """
                        :
                        """
                        self.api_type = ('continents/' + str(continent_id) + '/floors/' + 
                                     str(floor_id) + '/regions/' + str(region_id) + '/'  + '/maps/' + str(map_id))
                        return super(Continents.Floors.Regions.Maps.Subresource, self).get(ids=ids, lang=lang)
                    
                
                
class Maps(Resource, IDsLookupMixin):
    api_class ='maps'
    
    