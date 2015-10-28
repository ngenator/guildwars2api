GuildWars2API
=============

A Python wrapper to simplify use of the official [Guild Wars 2 API](https://forum-en.guildwars2.com/forum/community/api/API-Documentation/first#post2028044).

[TOC]

### Installation
1. Clone the repository
2. Navigate to the local copy of the repository in command line
3. Run `python setup.py install` to set up the library (For users with more complex Python installations, see [Python documentation](https://docs.python.org/3.2/install/index.html))
4. When importing, use `from guildwars2api.client import GuildWars2API`

### Sample code
```python
from guildwars2api.client import GuildWars2API

# Set wrapper to Version 1 endpoints
api = GuildWars2API(api_version='v1')

# Print the number of ongoing WvW matches
matches = api.matches.get()
print("Matches", len(matches))

# Set wrapper to Version 2 endpoints
api = GuildWars2API(api_version='v2')

# Get the details of a specific task with the following inputs:
# continent_id, floor_id, region_id, map_id, and task_id
tasks = api.continents.floors.regions.maps.tasks.get(1, 1, 1, 26, 554)
```

### Supported API Version 2 Endpoints
As of 10/27/15, the following v2 endpoints are available:

#####Items
* [items](http://wiki.guildwars2.com/wiki/API:2/items): Returns information about items
* [materials](http://wiki.guildwars2.com/wiki/API:2/materials): Returns information about materials
* [recipes](http://wiki.guildwars2.com/wiki/API:2/recipes): Returns information about recipes
* [recipes/search](http://wiki.guildwars2.com/wiki/API:2/recipes/search): A search interface for recipes
* [skins](http://wiki.guildwars2.com/wiki/API:2/skins): Returns information about skins

#####Game Mechanics
* [specializations](http://wiki.guildwars2.com/wiki/API:2/specializations): Returns information about specializations
* [traits](http://wiki.guildwars2.com/wiki/API:2/traits): Returns information about traits

#####Map Information
* [continents](http://wiki.guildwars2.com/wiki/API:2/continents): Returns a list of continents and information about each continent
* [floors](http://wiki.guildwars2.com/wiki/API:2/floors): Returns detailed information about a map floor
* [maps](http://wiki.guildwars2.com/wiki/API:2/maps): Returns information about maps in the game

#####Miscellaneous
* [build](http://wiki.guildwars2.com/wiki/API:2/build): Returns the current build id
* [colors](http://wiki.guildwars2.com/wiki/API:2/colors): Returns information about dye colors
* [files](http://wiki.guildwars2.com/wiki/API:2/files): Returns commonly requested assets

### Supported API Version 1 Endpoints
As of 10/27/15, the following v1 endpoints are available:

#####Dynamic Events
* [event_names](http://wiki.guildwars2.com/wiki/API:1/event_names): Returns a list of localized event names
* [map_names](http://wiki.guildwars2.com/wiki/API:1/map_names): Returns a list of localized map names
* [world_names](http://wiki.guildwars2.com/wiki/API:1/world_names): Returns a list of localized world names
* [event_details](http://wiki.guildwars2.com/wiki/API:1/event_details): Returns detailed information about events

#####Guilds
* [guild_details](http://wiki.guildwars2.com/wiki/API:1/guild_details): Returns detailed information about a guild

#####Items
* [items](http://wiki.guildwars2.com/wiki/API:1/items): Returns a list of discovered items
* [item_details](http://wiki.guildwars2.com/wiki/API:1/item_details): Returns detailed information about an item
* [recipes](http://wiki.guildwars2.com/wiki/API:1/recipes): Returns a list of discovered recipes
* [recipe_details](http://wiki.guildwars2.com/wiki/API:1/recipe_details): Returns detailed information about a recipe
* [skins](http://wiki.guildwars2.com/wiki/API:1/skins): Returns a list of skins
* [skin_details](http://wiki.guildwars2.com/wiki/API:1/skin_details): Returns detailed information about a skin

#####Map Information
* [continents](http://wiki.guildwars2.com/wiki/API:1/continents): Returns a list of continents and information about each continent
* [maps](http://wiki.guildwars2.com/wiki/API:1/maps): Returns a list of maps in the game
* [map_floor](http://wiki.guildwars2.com/wiki/API:1/map_floor): Returns detailed information about a map floor

#####World vs. World
* [wvw/matches](http://wiki.guildwars2.com/wiki/API:1/wvw/matches): Returns the currently running WvW matches
* [wvw/match_details](http://wiki.guildwars2.com/wiki/API:1/wvw/match_details): Returns details about a WvW match
* [wvw/objective_names](http://wiki.guildwars2.com/wiki/API:1/wvw/objective_names): Returns a list of WvW objective names

#####Miscellaneous
* [build](http://wiki.guildwars2.com/wiki/API:1/build): Returns the current build id
* [colors](http://wiki.guildwars2.com/wiki/API:1/colors): Returns a list of dyes in the game
* [files](http://wiki.guildwars2.com/wiki/API:1/files): Returns commonly requested assets

### License

![CC SA](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)

GuildWars2API by Daniel Ng is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.
