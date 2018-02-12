import folium


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


def read_location_file(path, dict_it, break_line):
    """
    (str,dict,int) ->None

    Creates map and puts all of the layers and pointers
    the pointer with "fim" is for those marks with 1 film
    and the "oscar" mark is for more popular spots
    """
    map_films = folium.Map()
    pp_fg = folium.FeatureGroup(name='Population')
    fg = folium.FeatureGroup(name="Regular spots")
    fpp = folium.FeatureGroup(name="Popular spots")
    fg_p = folium.FeatureGroup(name="UkraineBorders")

    fg_p.add_child(
        folium.GeoJson(data=open('jsonfiles/UKR.geo.json', 'r',
                                 encoding="utf-8").read(), ))
    with open(path, 'r', encoding="utf-8", errors="ignore") as file_films:
        file_films.readline()
        line = file_films.readline()
        count = 0
        count_films = 1

        while line:
            if count == break_line:
                break
            try:
                line = file_films.readline()
                for key, value in dict_it.items():
                    if key == line.split("\t")[0]:
                        full_value = ""
                        for location in value:
                            location = debugstr(location)
                            full_value += \
                                "{}) <a href=\"https://www.google." \
                                "com.ua/search?q={}\">{}" \
                                "</a><br>" \
                                "".format(count_films, location, location)
                            count_films += 1
                        count_films = 1
                        count += 1
                        print("[{}:{}]".format(count, break_line))
                        if len(value) > 1:
                            icon_url = 'files/img.png'
                            size = (40, 50)
                            iconn = folium.features.CustomIcon(icon_url,
                                                               icon_size=size)
                            fpp.add_child(
                                folium.Marker
                                (location=[float(line.split("\t")[1]),
                                           float(line.split("\t")[2])],
                                 icon=iconn,
                                 popup="<small>All films"
                                       " on this location<br><bold>{}"
                                       "</bold></small>".format(
                                     full_value)))
                        else:
                            size = (40, 40)
                            icon_url = 'files/camera.png'
                            iconn = folium.features.CustomIcon(icon_url,
                                                               icon_size=size)
                            fg.add_child(
                                folium.Marker(
                                    location=[float(line.split("\t")[1]),
                                              float(line.split("\t")[2])],
                                    icon=iconn,
                                    popup="<small>All films on this"
                                          " location<br><bold>{}"
                                          "</bold></small>".format(
                                        full_value)))
            except UnicodeEncodeError:
                continue
            except ValueError:
                continue
    pp_fg.add_child(folium.GeoJson(open('jsonfiles/world.json', 'r',
                                        encoding='utf-8-sig').read(),
                                   lambda x: {'fillColor': 'yellow'
                                   if x['properties']['POP2005'] <
                                      10000000 else 'blue'
                                   if x['properties']['POP2005'] <
                                      20000000 else 'red'}))
    fg_p.add_child(
        folium.GeoJson(data=open('jsonfiles/UKR.geo.json', 'r',
                                 encoding="utf-8").read(), ))
    map_films.add_child(fpp)
    map_films.add_child(fg_p)
    map_films.add_child(fg)
    map_films.add_child(pp_fg)
    map_films.add_child(folium.LayerControl())
    map_films.save("mapOfFilms.html")
