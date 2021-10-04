import pybaseball as pb
from pb import statcast
import pandas as pd
x=input(int('enter date make sure to include quotes, enternothing for yesterdays stats (yyyy-mm-dd): '))
Df=pd.DataFrame(statcast(start_dt=x,end_dt=None))
print(Df)
input("<enter>")
