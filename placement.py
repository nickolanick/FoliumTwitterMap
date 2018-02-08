import folium
import random
from locathion_finder import find_location


def layer_placement(dict_locations):
    """
    dict() --> None
    Puts all three layers the Markers Population And UKRAINE!
    the population is 3 colors (depends on the amount of people)

    """
    map_films = folium.Map()
    pp_fg = folium.FeatureGroup(name='Population')
    fg = folium.FeatureGroup(name="Markers")
    fg_p = folium.FeatureGroup(name="UkraineBorders")

    fg_p.add_child(
        folium.GeoJson(data=open('jsonfiles/UKR.geo.json', 'r',
                                 encoding="utf-8").read(), ))
    for key, value in dict_locations.items():

        full_value = ""
        for location in range(len(value)):
            value[location] = debugstr(value[location])
            full_value += "{}) <a href=\"#\">{}</a><br>" \
                .format(str(location + 1), value[location])
        latitude, longtitude = key
        fg.add_child(folium.Marker
                     (location=
                      [latitude,
                       longtitude],
                      popup="<small>All films on this location<br><bold>{}"
                            "</bold></small>".format(
                          full_value),
                      icon=folium.Icon(
                          color=('#%06X' % random.randint(0, 256 ** 3 - 1)),
                          icon_color=
                          ('#%06X' % random.randint(0, 256 ** 3 - 1)))))
    pp_fg.add_child(folium.GeoJson(open('jsonfiles/world.json', 'r',
                                        encoding=
                                        'utf-8-sig').read(),
                                   lambda x: {'fillColor': 'yellow'
                                   if x['properties']['POP2005'] <
                                      10000000 else 'blue'
                                   if x['properties']['POP2005'] <
                                      20000000 else 'red'}))
    map_films.add_child(fg)
    map_films.add_child(fg_p)
    map_films.add_child(pp_fg)
    map_films.add_child(folium.LayerControl())
    map_films.save("new.html")


def debugstr(element):
    """
    Find the " ' in the str and replaces them
    And lets Html read the file correctly
    """
    if "'" in element:
        element = element.replace("'", "")
    if "\"" in element:
        element = element.replace("\"", "")
    return element


def map_placement(dict_map, limit_data):
    count = 0
    dict_final = dict()
    bool_exit = False

    for key, value in dict_map.items():
        if bool_exit:
            break
        for location in value:
            print("[{}:{}]".format(count, limit_data))
            if count >= limit_data:
                bool_exit = True
                break
            count += 1
            try:
                try:
                    latitude, longitude = find_location(location)
                except IndexError:
                    continue

                if dict_final.get((latitude, longitude), False):
                    dict_final[(latitude, longitude)].append(key)
                else:
                    dict_final[(latitude, longitude)] = [key]

            except AttributeError:
                continue
    return dict_final
