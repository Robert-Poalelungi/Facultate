import geopandas as gp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tk_gui as gui
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, HoverTool, \
    LinearColorMapper, CategoricalColorMapper, ColorBar, BasicTicker, Ticker
from bokeh.plotting import figure
import bokeh.palettes as palete_bokeh
from bokeh.transform import linear_cmap

def plot_map(nume_fisier_shape, S, coduri, titlu="Harta scoruri", clasificator=False):
    m = np.shape(S)[1]
    shp = gp.GeoDataFrame.from_file(nume_fisier_shape)
    campuri_shape = [shp.columns[i] for i in range(0, len(shp.columns))]
    camp_legatura = gui.Check(campuri_shape, "Selectati variabila index")[0]
    t = pd.DataFrame(data={'coduri': coduri})
    for i in range(m):
        t.insert(1, 'v' + str(i + 1), S[:, i], allow_duplicates=True)
    shp1 = pd.merge(shp, t, left_on=camp_legatura, right_on='coduri')
    for i in range(m):
        f = plt.figure(titlu + str(i + 1), figsize=(8, 7))
        f1 = f.add_subplot(1, 1, 1)
        f1.set_title(titlu + str(i + 1))
        if clasificator:
            shp1.plot('v' + str(i + 1), cmap='Reds', ax=f1, legend=True, scheme='fisher_jenks')
        else:
            shp1.plot('v' + str(i + 1), cmap='Reds', ax=f1, legend=True)

def plot_bokeh(nume_fisier_shape=None, tabel_date=None, titlu="", legenda=True):
    if tabel_date is None:
        gdf = gp.GeoDataFrame.from_file(nume_fisier_shape)
    else:
        shp = gp.GeoDataFrame.from_file(nume_fisier_shape)
        l1, l2 = gui.Check2(list(shp), list(tabel_date), "Selectati campurile de legatura:")
        c1 = l1[0]
        tip_camp_c1 = gui.Combo(["Numeric", "Categorial"], "Tip camp " + c1)
        if tip_camp_c1 == "Numeric":
            left = np.array([str(i) for i in shp[c1]], dtype=np.int64)
        else:
            left = [str(i) for i in shp[c1]]
        shp[c1] = left
        c2 = l2[0] if len(l2) != 0 else tabel_date.index.name
        gdf = pd.merge(shp, tabel_date, left_on=c1, right_on=c2)

    # Calcul aspect-ratio pentru harta
    # proprietatea bounds a obiectului GeoDataFrame gdf are minim si maxim pe x si y
    # rect este de tip DataFrame
    rect = gdf.bounds
    minx = rect['minx'].min()
    miny = rect['miny'].min()
    maxx = rect['maxx'].max()
    maxy = rect['maxy'].max()
    asp = (maxx - minx) / (maxy - miny)
    campuri = list(gdf)
    camp_harta = gui.Combo(campuri, "Campul harta:")
    tip_camp = gui.Combo(["Numeric", "Categorial"], "Tip camp:")
    campuri_informatii = gui.Check(campuri, "Campuri informatii:")
    valori = list(set(gdf[camp_harta]))
    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
    latime = 1000
    inaltime = np.int(latime / asp)
    p = figure(title=titlu, tools=TOOLS, x_axis_location=None, y_axis_location=None,
               width=latime, height=inaltime)
    p.grid.grid_line_color = None
    if tip_camp == "Numeric":
        json = gdf.to_json()
        geo_src = GeoJSONDataSource(geojson=json)
        paleta_mea = palete_bokeh.viridis(128)
        cmap = LinearColorMapper(palette=paleta_mea)
        mapper = linear_cmap(field_name=camp_harta,
                             palette=paleta_mea, low=min(valori), high=max(valori))
        color_bar = ColorBar(color_mapper=mapper['transform'], ticker=BasicTicker(),
                             label_standoff=12, border_line_color=None, location=(0, 0))
        p.add_layout(color_bar, place='right')
        p.patches('xs', 'ys', fill_alpha=0.7,
                  fill_color={'field': camp_harta, 'transform': cmap},
                  line_color='black', line_width=0.5, source=geo_src)
    else:
        paleta_mea = palete_bokeh.viridis(len(valori))
        if legenda:
            k = 0
            for v in valori:
                json = gdf[gdf[camp_harta] == v].to_json()
                geo_src = GeoJSONDataSource(geojson=json)
                p.patches('xs', 'ys', fill_alpha=0.7, fill_color=paleta_mea[k],
                          line_color='black', line_width=0.5, source=geo_src, legend=v)
                k += 1
        else:
            json = gdf.to_json()
            geo_src = GeoJSONDataSource(geojson=json)
            # str_valori = [str(v) for v in valori]
            color_mapper = CategoricalColorMapper(factors=valori, palette=paleta_mea)
            p.patches('xs', 'ys', fill_alpha=0.7,
                      fill_color={'field': camp_harta, 'transform': color_mapper},
                      line_color='black', line_width=0.5, source=geo_src)

    hover = p.select_one(HoverTool)
    hover.point_policy = 'follow_mouse'
    informatii = []
    for camp in campuri_informatii:
        informatii.append((camp, '@' + camp))
    informatii.append((camp_harta, '@' + camp_harta))
    hover.tooltips = informatii
    show(p)
