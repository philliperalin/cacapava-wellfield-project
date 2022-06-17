import welltestpy as wtp
import csv
import numpy as np

#def calc_T(dataframe):
#loading data
with open('../data/IRITANI-data.csv', 'rt') as f:
    reader = csv.reader(f)
    data = list(reader)

#setting the campaign
field = wtp.FieldSite("Caçapava")
campaign = wtp.Campaign(fieldsite=field, 
    name="wellfield implementation")

print(data)

r = 1
c = 0
#creating the pumping test
campaign.add_well(name=data[r][0], 
    radius=0.1,
    coordinates=(0.0, 0.0))
campaign.add_well(name='owell', 
    radius=0.1,
    coordinates=(0.0, 0.1))
rate = np.array(data[r][9]).astype(float)
pumptest = wtp.PumpingTest(name='pumping', 
    pumpingwell=data[r][0], 
    pumpingrate=rate)

#adding data to the pumping test
pumptest.add_steady_obs(well='owell',
    observation=np.array(data[r][6]).astype(float))

#adding the pumping test to the campaign
campaign.addtests(pumptest)

#transmissivity estimate
estimation = wtp.estimate.Thiem(name=data[r][0],
    campaign=campaign, 
    generate=True)
estimation.run(folder='./estimations/', 
    dbname=data[r][0]+'_db', 
    traceplotname=data[r][0]+'_paratrace.pdf', 
    fittingplotname=data[r][0]+'_fit.pdf', 
    interactplotname=data[r][0]+'_interact.pdf', 
    estname=data[r][0]+'_estimate.txt')
