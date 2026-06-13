import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if t[v].isna().any():
            if is_numeric_dtype(t[v]):
                t[v].fillna(value=t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)


class acp():
    def __init__(self, t, v):
        assert isinstance(t, pd.DataFrame)
        self.__x = t[v].values
        self.v = v

    @property
    def x(self):
        return self.__x

    def fit(self, std=True, nlib=0, procent_minimal=80):
        n, m = self.x.shape
        x_ = self.__x - np.mean(self.__x, axis=0)
        if std:
            x_ = x_ / np.std(self.__x, axis=0)
        r_v = (1 / (n - nlib)) * x_.T @ x_
        valp, vecp = np.linalg.eig(r_v)
        # print(valp,vecp.T,sep="\n")
        k = np.flip(np.argsort(valp))
        self.__alpha = valp[k]
        self.__a = vecp[:, k]
        self.__c = x_ @ self.__a
        procent_cumulat = np.cumsum(self.alpha) * 100 / sum(self.__alpha)
        k1 = np.where(procent_cumulat > procent_minimal)[0][0] + 1
        if std:
            k2 = len(np.where(self.__alpha > 1)[0])
        else:
            k2 = np.NAN
        eps = self.__alpha[:m - 1] - self.__alpha[1:]
        sigma = eps[:m - 2] - eps[1:]
        exista_negative = sigma < 0
        if any(exista_negative):
            k3 = np.where(exista_negative)[0][0] + 2
        else:
            k3 = np.NAN
        self.__criterii = (k1, k2, k3)
        if std:
            self.__r = self.a * np.sqrt(self.alpha)
        else:
            self.__r = np.corrcoef(x_, self.c, rowvar=False)[:m, m:]

    @property
    def r(self):
        return self.__r

    @property
    def criterii(self):
        return self.__criterii

    @property
    def alpha(self):
        return self.__alpha

    @property
    def a(self):
        return self.__a

    @property
    def c(self):
        return self.__c

    def tabelare_varianta(self):
        varianta_cumulata = np.cumsum(self.__alpha)
        procent_varianta = self.__alpha * 100 / sum(self.alpha)
        procent_cumulat = np.cumsum(procent_varianta)
        return pd.DataFrame(
            {
                "Varianta": self.__alpha,
                "Procent varianta": procent_varianta,
                "Varianta cumulata": varianta_cumulata,
                "Procent cumulat": procent_cumulat
            }, ["C" + str(i) for i in range(1, len(self.__alpha) + 1)]
        )
