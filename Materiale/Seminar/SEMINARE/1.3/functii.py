import pandas as pd


def salvare(x,linii=None,coloane=None,out="out.cvs"):
    t=pd.DataFrame(x,linii,coloane)
    t.to_csv(out)
