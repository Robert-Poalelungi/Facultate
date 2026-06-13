import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from sklearn.metrics import silhouette_samples, silhouette_score

# graficele folosite la seminar si curs
def correlogram(matrix=None, dec=2, title='Corelograma', valmin=-1, valmax=1):
    plt.figure(title, figsize=(15, 11))
    plt.title(title, fontsize=16, color='k', verticalalignment='bottom')
    sb.heatmap(data=np.round(matrix, dec), vmin=valmin, vmax=valmax, cmap='bwr', annot=True)

def intensitateaLegatura(matrix=None, dec=2, title='Intensitate legatura'):
    plt.figure(title, figsize=(15, 11))
    plt.title(title, fontsize=16, color='k', verticalalignment='bottom')
    sb.heatmap(data=np.round(matrix, dec), cmap='Blues', annot=True)

def correlCircle(matrix=None, V1=0, V2=1, dec=1,
                 XLabel=None, YLabel=None, minVal=-1, maxVal=1, title='Correlation Circle'):
    plt.figure(title, figsize=(8, 8))
    plt.title(title, fontsize=14, color='k', verticalalignment='bottom')
    T = [t for t in np.arange(0, np.pi*2, 0.01)]
    X = [np.cos(t) for t in T]
    Y = [np.sin(t) for t in T]
    plt.plot(X, Y)
    plt.axhline(y=0, color='g')
    plt.axvline(x=0, color='g')
    if XLabel==None or YLabel==None:
        if isinstance(matrix, pd.DataFrame):
            plt.xlabel(matrix.columns[V1], fontsize=14, color='k', verticalalignment='top')
            plt.ylabel(matrix.columns[V2], fontsize=14, color='k', verticalalignment='bottom')
        else:
            plt.xlabel('Var '+str(V1+1), fontsize=14, color='k', verticalalignment='top')
            plt.ylabel('Var '+str(V2+1), fontsize=14, color='k', verticalalignment='bottom')
    else:
        plt.xlabel(XLabel, fontsize=14, color='k', verticalalignment='top')
        plt.ylabel(YLabel, fontsize=14, color='k', verticalalignment='bottom')

    if isinstance(matrix, np.ndarray):
        plt.scatter(x=matrix[:, V1], y=matrix[:, V2], c='r')
        for i in range(matrix.shape[0]):
            plt.text(x=matrix[i, V1], y=matrix[i, V2], s='(' +
                    str(np.round(matrix[i, V1], dec))
                     + ', ' + str(np.round(matrix[i, V2], dec)) + ')')

    if isinstance(matrix, pd.DataFrame):
        plt.scatter(x=matrix.iloc[:, V1], y=matrix.iloc[:, V2], c='b')
        for i in range(matrix.values.shape[0]):
            plt.text(x=matrix.iloc[i, V1], y=matrix.iloc[i, V2], s='(' +
                    str(np.round(matrix.iloc[i, V1], dec))
                     + ', ' + str(np.round(matrix.iloc[i, V2], dec)) + ')')


def principalComponents(eigenvalues=None, XLabel='Principal components', YLabel='Eigenvalues (variance)',
                        title='Varianta explicata de componentele principale'):
    plt.figure(title, figsize=(13, 8))
    plt.title(title, fontsize=14, color='k', verticalalignment='bottom')
    plt.xlabel(XLabel, fontsize=14, color='k', verticalalignment='top')
    plt.ylabel(YLabel, fontsize=14, color='k', verticalalignment='bottom')
    components = ['C'+str(j+1) for j in range(eigenvalues.shape[0])]
    plt.plot(components, eigenvalues, 'bo-')
    plt.axhline(y=1, color='r')

def plot_silhouette(x, partitia, titlu, cmap='viridis'):
    """
    Generates a silhouette plot for cluster validation.

    :param x: Data points
    :param partitia: Cluster labels
    :param titlu: Plot title
    :param cmap: Colormap
    """
    n_clusters = len(np.unique(partitia))
    silhouette_avg = silhouette_score(x, partitia)
    sample_silhouette_values = silhouette_samples(x, partitia)

    y_lower = 10
    plt.figure(figsize=(10, 6))

    for i in range(n_clusters):
        # Sort silhouette values for cluster i
        ith_cluster_silhouette_values = sample_silhouette_values[partitia == i]
        ith_cluster_silhouette_values.sort()

        # Compute bar height
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        # Fill plot with color
        color = plt.get_cmap(cmap)(float(i) / n_clusters)
        plt.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    plt.title(f"{titlu} (Avg Silhouette Score: {silhouette_avg:.2f})")
    plt.xlabel("Silhouette Scores")
    plt.ylabel("Cluster")
    plt.axvline(x=silhouette_avg, color="red", linestyle="--")
    plt.grid(True)
    plt.show()

def plot_indecsi_silhouette(x, partitia, culori, metoda):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(1, 1, 1)
    cmap = LinearSegmentedColormap.from_list("cmap", culori, len(culori))
    plot_silhouette(x, partitia, "Plot scoruri Silhouette. Metoda:" + metoda, cmap=cmap)
    plt.savefig("out/Silhouette_P_" + str(len(culori)))


def scatter(t, var1, var2, g, culori, titlu="Plot partitie"):
    fig = plt.figure(titlu, figsize=(13, 7))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1, aspect=1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    if g is not None:
        clase = np.unique(g)
        q = len(clase)
        for i in range(q):
            t_ = t[g == clase[i]]
            ax.scatter(t_[var1], t_[var2], color=culori[i], label=clase[i])
        tg = t.groupby(by=g).mean()
        ax.scatter(tg[var1], tg[var2], c=culori, marker="s", s=300, alpha=0.5)
        if len(t) < 50:
            for i in range(len(t)):
                ax.text(t[var1].iloc[i], t[var2].iloc[i], t.index[i])
    ax.legend()
    plt.savefig("out/Plot_P_" + str(len(culori)))


def histograme(t, variabila, partitie, culori):
    fig = plt.figure(figsize=(9, 7))
    assert isinstance(fig, plt.Figure)
    fig.suptitle("Histograme pentru variabila " + variabila)
    clase = np.unique(partitie)
    q = len(clase)
    min_max = (t[variabila].min(), t[variabila].max())
    ax = fig.subplots(1, q, sharey=True)
    for i in range(q):
        axe = ax[i]
        assert isinstance(axe, plt.Axes)
        axe.set_xlabel(str(clase[i]))
        axe.hist(t[partitie == clase[i]][variabila], range=min_max, color=culori[i], rwidth=0.9)
    plt.savefig("out/Hist_P_" + str(q) + "_" + variabila)


def elbow(d, plot=True):
    m = len(d)
    # diferentele dintre distante
    y = d[1:] - d[:m - 1]
    k_max = np.argmax(y)
    k = m - k_max
    if plot:
        fig = plt.figure(figsize=(9, 7))
        ax = fig.add_subplot(1, 1, 1)
        assert isinstance(ax, plt.Axes)
        ax.set_title("Elbow", fontdict={"fontsize": 16, "color": "b"})
        ax.set_xlabel("Jonctiuni",color="m")
        ax.set_ylabel("Distante",color="m")
        ax.plot(np.arange(1,m+1),d)
        ax.scatter(k_max+1, d[k_max], alpha=0.5, s=100, c="g",label="Partitia cu "+str(k) + " clusteri")
        ax.axhline(d[k_max],c="c")
        ax.axhline(d[k_max+1], c="c")
        ax.legend()
        plt.savefig("./dataOUT/Elbow_"+str(k))
    return k_max, k

def show():
    plt.show()
