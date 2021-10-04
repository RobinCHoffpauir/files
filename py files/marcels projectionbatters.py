import pandas as pd
from pybaseball.analysis.projections.marcels import MarcelProjectionsPitching
from pybaseball.analysis.projections.marcels import MarcelProjectionsBatting
from pybaseball.lahman import people
ppl = people()  # for merging player names onto the projections
ppl['Player'] = ppl['nameFirst'].str.cat(ppl['nameLast'], ' ')
marcel_batting = MarcelProjectionsBatting()
marcel_pitching = MarcelProjectionsPitching()
pitchers = marcel_pitching.projections(2020)
batters = marcel_batting.projections(2020)
pitchers = pd.merge(ppl[['playerID', 'Player']], pitchers, on='playerID', how='right')
batters = pd.merge(ppl[['playerID', 'Player']], batters, on='playerID', how='right')
y=input('what stat would you like to sort by: ')
z=batters.sort_values(y, ascending=False)
print(z)
input('press<enter>')
