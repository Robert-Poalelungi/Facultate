import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pandas as pd
from bokeh.io import show as showb
from bokeh.models import GeoJSONDataSource, HoverTool, \
    LinearColorMapper, CategoricalColorMapper, ColorBar, BasicTicker, Ticker
from bokeh.plotting import figure
import bokeh.palettes as palete_bokeh
from bokeh.transform import linear_cmap


# def corelograma(t, vmin=-1, vmax=1, titlu="Corelatii variabile-componente"):
#     fig = plt.figure(figsize=(9, 8))
#     assert isinstance(fig, plt.Figure)
#     ax = fig.add_subplot(1, 1, 1)
#     assert isinstance(ax, plt.Axes)
#     ax.set_title(titlu, fontsize=16, color='b')
#     ax_ = sb.heatmap(t, vmin=vmin, vmax=vmax, cmap="RdYlBu", annot=True, ax=ax)
#     ax_.set_xticklabels(t.columns, rotation=30, ha="right")


def show():
    plt.show()


def plot_varianta(alpha, nrcomp, procent_minim_varianta, x_label="Components", titlu="Scree Plot"):
    fig = plt.figure(figsize=(13, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 18, "color": "b"})
    ax.set_xlabel(x_label, fontdict={"fontsize": 14, "color": "b"})
    ax.set_ylabel("Variance", fontdict={"fontsize": 14, "color": "b"})
    m = len(alpha)
    x = np.arange(1, m + 1)
    ax.set_xticks(x)
    ax.plot(x, alpha)
    ax.axhline(1, c='g', label="Kaiser")
    if nrcomp[1] is not np.NaN:
        ax.axhline(alpha[nrcomp[1] - 1], c='m', label="Variance Percent > " + str(procent_minim_varianta) + "%")
    if nrcomp[2] is not np.NaN:
        ax.axhline(alpha[nrcomp[2] - 1], c='c', label="Cattell")
    if len(nrcomp) == 4:
        ax.axhline(alpha[nrcomp[3] - 1], c='r', label="Bartlett")
    ax.scatter(x, alpha, c='r')
    ax.legend()


def corelograma(t, vmin=-1, vmax=1, titlu="Factor Loadings"):
    fig = plt.figure(figsize=(9, 18))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontsize=16, color='b')
    ax_ = sb.heatmap(t, vmin=vmin, vmax=vmax, cmap="RdYlBu", annot=True, ax=ax)
    ax_.set_xticklabels(t.columns, rotation=30, ha="right")
    ax_.set_yticklabels(t.index, rotation=30, va="top")
    plt.savefig("corelograma")


def plot_corelatii(t, var1, var2, titlu="Corelatii variabile-componente", aspect='auto'):
    print("plot")
    fig = plt.figure(figsize=(9, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(var1, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var2, fontdict={"fontsize": 12, "color": "b"})
    ax.set_aspect(aspect)
    u = np.arange(0, np.pi * 2, 0.01)
    ax.plot(np.cos(u), np.sin(u))
    ax.plot(0.7 * np.cos(u), 0.7 * np.sin(u), c='c')
    ax.axvline(0)
    ax.axhline(0)
    ax.scatter(t[var1], t[var2], c="r")
    for i in range(len(t)):
        ax.text(t[var1].iloc[i], t[var2].iloc[i], t.index[i])


def plot_instante(x, y, var1, var2, z, titlu="Plot componente", aspect='auto'):
    fig = plt.figure(figsize=(13, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(var1, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var2, fontdict={"fontsize": 12, "color": "b"})
    ax.set_aspect(aspect)
    ax.axvline(0)
    ax.axhline(0)
    ax.scatter(x, y, c="r")
    for i in range(len(z)):
        ax.text(x[i], y[i], z[i])


def scatter_3d(x, y, z, var1, var2, var3, labels, titlu="Scatterplot 3d",aspect='auto'):
    fig = plt.figure(titlu, figsize=(10, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1, projection="3d")
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(var1,fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var2,fontdict={"fontsize": 12, "color": "b"})
    ax.set_zlabel(var3,fontdict={"fontsize": 12, "color": "b"})
    ax.set_aspect(aspect)
    ax.scatter(x, y, z, c="r")
    for i in range(len(labels)):
        ax.text(x[i], y[i], z[i], labels[i])


def harta(shp, camp_legatura, t, titlu="Harta scoruri",
          axe=False, min_max_comun=False):
    variabile_harta = list(t)
    if min_max_comun:
        custom_vmin = np.min(t[variabile_harta].values)
        custom_vmax = np.max(t[variabile_harta].values)
    shp1 = pd.merge(shp, t, left_on=camp_legatura, right_index=True)
    for v in variabile_harta:
        f = plt.figure(titlu + "-" + v, figsize=(10, 7))
        ax = f.add_subplot(1, 1, 1)
        ax.set_title(titlu + "-" + v, fontdict={"fontsize": 18, "color": "b"})
        if not axe:
            ax.set_xticklabels([])
            ax.set_xticks([])
            ax.set_yticklabels([])
            ax.set_yticks([])
        if min_max_comun:
            shp1.plot(v, cmap="cool", ax=ax, legend=True, vmin=custom_vmin, vmax=custom_vmax)
        else:
            shp1.plot(v, cmap="cool", ax=ax, legend=True)


def plot_bokeh(shp, camp_legatura, tip_camp_legatura, campuri_informatii, tabel_date, camp_harta, tip_camp, titlu="",
               legenda=True):
    if tip_camp_legatura == "Numeric":
        left = np.array([str(i) for i in shp[camp_legatura]], dtype=np.int64)
    else:
        left = [str(i) for i in shp[camp_legatura]]
    shp[camp_legatura] = left

    gdf = pd.merge(shp, tabel_date, left_on=camp_legatura, right_index=True)

    rect = gdf.bounds
    minx = rect['minx'].min()
    miny = rect['miny'].min()
    maxx = rect['maxx'].max()
    maxy = rect['maxy'].max()
    asp = (maxx - minx) / (maxy - miny)
    campuri = list(gdf)
    valori = list(set(gdf[camp_harta]))
    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
    latime = 1000
    inaltime = int(latime / asp)
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
    showb(p)
