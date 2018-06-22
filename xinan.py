from rpy2.robjects import pandas2ri
pandas2ri.activate()
from rpy2.robjects.packages import importr
base = importr('base')
base.write.dbf(df)