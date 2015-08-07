from guildwars2api.resources import Resource, IDsLookupMixin


class Skins(Resource, IDsLookupMixin):
    api_class = 'skins'
    
    
class Recipes(Resource, IDsLookupMixin):
    api_class = 'recipes'
    

class Items(Resource, IDsLookupMixin):
    api_class = 'items'
    
    
class Materials(Resource, IDsLookupMixin):
    api_class = 'materials'
    