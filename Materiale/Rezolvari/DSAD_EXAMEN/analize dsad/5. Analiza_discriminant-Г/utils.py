import matplotlib.pyplot as plt
import seaborn as sb


def plot_instante(z, k1, k2, zg, y, clase):
    fig = plt.figure(figsize=(13, 8))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title("Plot instante si criterii in axe discriminante",
                 fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel("z" + str(k1 + 1), fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel("z" + str(k2 + 1), fontdict={"fontsize": 12, "color": "b"})

    ax.set_aspect(1)

    sb.scatterplot(x=z[:, k1], y=z[:, k2], hue=y, hue_order=clase, ax=ax)
    sb.scatterplot(x=zg[:, k1], y=zg[:, k2], hue=clase, marker="s", s=225, ax=ax, legend=False)

    plt.show()


def distributie(z, k, y, clase):
    fig = plt.figure(figsize=(13, 8))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title("Distributie in axa " + str(k + 1),
                 fontdict={"fontsize": 16, "color": "b"})

    for each in clase:
        sb.kdeplot(x=z[y == each, k], fill=True, label=each, ax=ax)
    ax.legend()
    plt.show()
