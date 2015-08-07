from guildwars2api.resources import Resource


class Skins(Resource):
    api_class = 'skins'
    
    def get(self, skin_id=None, lang=None):
        """
        :param skin_id: The skin_id to get details for
        :return: The skin for the given skin_id
        """
        return super(Skins, self).get(skin_id=skin_id, lang=lang)
    
    
class Recipes(Resource):
    api_class = 'recipes'
    
    def get(self, recipe_id=None):
        """
        :param recipe_id: The recipe_id to get details for
        :return: The recipe for the given recipe_id
        """
        return super(Recipes, self).get(recipe_id=recipe_id)

class Items(Resource):
    api_class = 'items'
    
    def get(self, item_id=None, lang=None):
        """
        :param item_id: The item_id to get details for
        :param lang: The language the results will be returned in, supported languages: en, fr, de, es
        :return: Details about the item for the given item_id
        """
        return super(Items, self).get(item_id=item_id, lang=lang)