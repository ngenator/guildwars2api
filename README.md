GuildWars2API
=============

A Python wrapper for the [Guild Wars 2 API](https://forum-en.guildwars2.com/forum/community/api/API-Documentation/first#post2028044).

### Installation
* Clone the repo, run `python setup.py install`
* Import the API client `from guildwars2api.client import GuildWars2API`
* Use the client to interact with the API

### Usage

```python
import random

from guildwars2api.client import GuildWars2API

api = GuildWars2API(api_version=v1)

# Get the list of event names
event_names = api.event_names.get(lang="en")
print "event names", len(event_names)

# Turn it into a dict
event_name_lookup = dict((e['id'], e['name']) for e in event_names)

# Get a random event, find out it's name, and add it to the event
event = random.choice(events)
event['event_name'] = event_name_lookup.get(event['event_id'], None)
print "event", event

# Get the list of matches
matches = api.matches.get()
print "matches", len(matches)

# Get the details for a random match
match_details = api.match_details.get(random.choice(matches)['wvw_match_id'])
print "match details", match_details

api = GuildWars2API(api_version=v2)

# Get the details of a tasks on a map using the continent_id, floor_id, region_id, map_id and task_id
tasks = api.continents.floors.regions.maps.tasks.get(1, 1, 1, 26, 554) 

```


#### LICENSE

![CC SA](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)

GuildWars2API by Daniel Ng is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.
