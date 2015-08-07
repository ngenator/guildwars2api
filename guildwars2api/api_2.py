from guildwars2api.resources import Resource, IDsLookupMixin


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
    api_class = 'continents'
    subresource = { "continent_id" : None, "floor_id" : None, "region_id" : None, "map_id" : None }
    
    def get_subclass_details(self, continent_id=None, floor_id=None, region_id=None, map_id=None, detail=None, detail_id=None, id_list=False):
        """
        Will default to none if the previous subresource is not set.  When id_list is set to true, then a query for
        ids will only appear, otherwise a detailed version of the id will be searched
        :param continent_id: The continent_id you would like to get information on
        :param floor_id: The floor_id you would like to get information on
        :param region_id: The region_id you would like to get information on
        :param map_id: The map_id you would like to get information on
        :param detail: Addtional info of the map, sectors, pois and tasks
        :return: None
        """
        if id_list:
            if continent_id:
                if floor_id:
                    self.api_subclass = str(continent_id)
                    if region_id:
                        self.api_subclass += '/floors/' + str(floor_id)
                        if map_id:
                            self.api_subclass += '/regions/' + str(region_id)
                            if (detail == "sectors" or detail == "pois" or detail == "tasks"):
                                self.api_subclass += '/maps/' + str(map_id)
                                if detail_id:
                                    self.api_subclass += "/" + detail
            return super(Continents, self).get()
        else:
            if continent_id:
                self.api_subclass = str(continent_id)
                if floor_id:
                    self.api_subclass += '/floors/' + str(floor_id)
                    if region_id:
                        self.api_subclass += '/regions/' + str(region_id)
                        if map_id:
                            self.api_subclass += '/maps/' + str(map_id)
                            if (detail == "sectors" or detail == "pois" or detail == "tasks"):
                                self.api_subclass += "/" + detail
                                if detail_id:
                                    self.api_subclass += "/" + detail_id
            return super(Continents, self).get()
    
    
    def get(self, ids=None):
        self.api_subclass=None
        return super(Continents, self).get(ids=ids)
    
    
    
    def get_all(self):
        """
        :return: All continents of the Guild Wars universe
        """
        
        return super(Continents, self).get(ids="all")
    
    
class Maps(Resource, IDsLookupMixin):
    api_class ='maps'
    
    