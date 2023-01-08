import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sn
import math

#step 1 read in the data
os.getcwd()
os.chdir("C:\\Users\\georg\\OneDrive\\Desktop\\data projects\\")
df = pd.read_csv("data.csv")
df.head()

#step 2 cleaning the data
a=0
for i in range(7,11):
  for j in df[df.columns[i]]:
    if(math.isnan(j)==True):
      df.drop(a, axis=0, inplace=True)
    a=a+1
  df=df.reset_index()
  a=0
print(df)

#step 3 organize the data
df=df.drop_duplicates()
#there are no duplicates so im going to group by zip code to start plotting
A=df['Zip']
zips=[A[0]]
for i in A:
  for j in range(len(zips)):
    if(i==zips[j]):
      break
    elif(j==len(zips)-1):
      zips.append(i)
print(len(zips)) #just want to see how many zipcodes i'm working with

#now we can group all the data by zip code
#only group zipcodes with 5 or more data points (19 zipcodes)
zip12206=pd.DataFrame(df[2:10][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip12601=pd.DataFrame(df[14:19][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip14212=pd.DataFrame(df[20:27][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip14211=pd.DataFrame(df[28:40][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip14208=pd.DataFrame(df[41:48][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip14213=pd.DataFrame(df[48:58][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip14215=pd.DataFrame(df[58:69][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip14207=pd.DataFrame(df[71:79][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip12078=pd.DataFrame(df[79:86][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip14611=pd.DataFrame(df[86:91][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip14621=pd.DataFrame(df[100:106][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip12010=pd.DataFrame(df[106:114][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip13501=pd.DataFrame(df[115:130][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip13502=pd.DataFrame(df[130:143][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip13205=pd.DataFrame(df[147:160][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip13204=pd.DataFrame(df[164:174][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip13208=pd.DataFrame(df[177:189][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip12550=pd.DataFrame(df[191:205][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip12180=pd.DataFrame(df[205:213][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])
zip12401=pd.DataFrame(df[215:220][:],columns=['index', 'County', 'County Code', 'Year', 'Zip', 'Tests', 'Less than 5 mcg/dL', '5-10 mcg/dL', '10 – 15 mcg/dL', '15 + mcg/dL', 'Total Elevated Blood Levels' , 'Percent', 'Rate per 1,000', 'Zip Code Location', 'County Location'])


#step 4 Visualizing the data

#create visualizations (Multi plot)
#on the x-axis we have time (in years) & on the y we have led in blood levels (number of people with exposure)
plt.clf()
fig, axes = plt.subplots(5, 4, sharex=True, figsize=(4,4))
fig.suptitle('Lead Levels for All Zip Codes')

X1=zip12206[zip12206.columns[3]] #time in years
Y1=(1/zip12206[zip12206.columns[5]])*((zip12206[zip12206.columns[6]]*2.5)+(zip12206[zip12206.columns[7]]*7.5)+(zip12206[zip12206.columns[8]]*12.5)+(zip12206[zip12206.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X2=zip12601[zip12601.columns[3]] #time in years
Y2=(1/zip12601[zip12601.columns[5]])*((zip12601[zip12601.columns[6]]*2.5)+(zip12601[zip12601.columns[7]]*7.5)+(zip12601[zip12601.columns[8]]*12.5)+(zip12601[zip12601.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X3=zip14212[zip14212.columns[3]] #time in years
Y3=(1/zip14212[zip14212.columns[5]])*((zip14212[zip14212.columns[6]]*2.5)+(zip14212[zip14212.columns[7]]*7.5)+(zip14212[zip14212.columns[8]]*12.5)+(zip14212[zip14212.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X4=zip14211[zip14211.columns[3]] #time in years
Y4=(1/zip14211[zip14211.columns[5]])*((zip14211[zip14211.columns[6]]*2.5)+(zip14211[zip14211.columns[7]]*7.5)+(zip14211[zip14211.columns[8]]*12.5)+(zip14211[zip14211.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X5=zip14208[zip14208.columns[3]] #time in years
Y5=(1/zip14208[zip14208.columns[5]])*((zip14208[zip14208.columns[6]]*2.5)+(zip14208[zip14208.columns[7]]*7.5)+(zip14208[zip14208.columns[8]]*12.5)+(zip14208[zip14208.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X6=zip14213[zip14213.columns[3]] #time in years
Y6=(1/zip14213[zip14213.columns[5]])*((zip14213[zip14213.columns[6]]*2.5)+(zip14213[zip14213.columns[7]]*7.5)+(zip14213[zip14213.columns[8]]*12.5)+(zip14213[zip14213.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X7=zip14215[zip14215.columns[3]] #time in years
Y7=(1/zip14215[zip14215.columns[5]])*((zip14215[zip14215.columns[6]]*2.5)+(zip14215[zip14215.columns[7]]*7.5)+(zip14215[zip14215.columns[8]]*12.5)+(zip14215[zip14215.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X8=zip14207[zip14207.columns[3]] #time in years
Y8=(1/zip14207[zip14207.columns[5]])*((zip14207[zip14207.columns[6]]*2.5)+(zip14207[zip14207.columns[7]]*7.5)+(zip14207[zip14207.columns[8]]*12.5)+(zip14207[zip14207.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X9=zip12078[zip12078.columns[3]] #time in years
Y9=(1/zip12078[zip12078.columns[5]])*((zip12078[zip12078.columns[6]]*2.5)+(zip12078[zip12078.columns[7]]*7.5)+(zip12078[zip12078.columns[8]]*12.5)+(zip12078[zip12078.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X10=zip14611[zip14611.columns[3]] #time in years
Y10=(1/zip14611[zip14611.columns[5]])*((zip14611[zip14611.columns[6]]*2.5)+(zip14611[zip14611.columns[7]]*7.5)+(zip14611[zip14611.columns[8]]*12.5)+(zip14611[zip14611.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X11=zip14621[zip14621.columns[3]] #time in years
Y11=(1/zip14621[zip14621.columns[5]])*((zip14621[zip14621.columns[6]]*2.5)+(zip14621[zip14621.columns[7]]*7.5)+(zip14621[zip14621.columns[8]]*12.5)+(zip14621[zip14621.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X12=zip12010[zip12010.columns[3]] #time in years
Y12=(1/zip12010[zip12010.columns[5]])*((zip12010[zip12010.columns[6]]*2.5)+(zip12010[zip12010.columns[7]]*7.5)+(zip12010[zip12010.columns[8]]*12.5)+(zip12010[zip12010.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X13=zip13501[zip13501.columns[3]] #time in years
Y13=(1/zip13501[zip13501.columns[5]])*((zip13501[zip13501.columns[6]]*2.5)+(zip13501[zip13501.columns[7]]*7.5)+(zip13501[zip13501.columns[8]]*12.5)+(zip13501[zip13501.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X14=zip13502[zip13502.columns[3]] #time in years
Y14=(1/zip13502[zip13502.columns[5]])*((zip13502[zip13502.columns[6]]*2.5)+(zip13502[zip13502.columns[7]]*7.5)+(zip13502[zip13502.columns[8]]*12.5)+(zip13502[zip13502.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X15=zip13205[zip13205.columns[3]] #time in years
Y15=(1/zip13205[zip13205.columns[5]])*((zip13205[zip13205.columns[6]]*2.5)+(zip13205[zip13205.columns[7]]*7.5)+(zip13205[zip13205.columns[8]]*12.5)+(zip13205[zip13205.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X16=zip13204[zip13204.columns[3]] #time in years
Y16=(1/zip13204[zip13204.columns[5]])*((zip13204[zip13204.columns[6]]*2.5)+(zip13204[zip13204.columns[7]]*7.5)+(zip13204[zip13204.columns[8]]*12.5)+(zip13204[zip13204.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X17=zip13208[zip13208.columns[3]] #time in years
Y17=(1/zip13208[zip13208.columns[5]])*((zip13208[zip13208.columns[6]]*2.5)+(zip13208[zip13208.columns[7]]*7.5)+(zip13208[zip13208.columns[8]]*12.5)+(zip13208[zip13208.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X18=zip12550[zip12550.columns[3]] #time in years
Y18=(1/zip12550[zip12550.columns[5]])*((zip12550[zip12550.columns[6]]*2.5)+(zip12550[zip12550.columns[7]]*7.5)+(zip12550[zip12550.columns[8]]*12.5)+(zip12550[zip12550.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X19=zip12180[zip12180.columns[3]] #time in years
Y19=(1/zip12180[zip12180.columns[5]])*((zip12180[zip12180.columns[6]]*2.5)+(zip12180[zip12180.columns[7]]*7.5)+(zip12180[zip12180.columns[8]]*12.5)+(zip12180[zip12180.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

X20=zip12401[zip12401.columns[3]] #time in years
Y20=(1/zip12401[zip12401.columns[5]])*((zip12401[zip12401.columns[6]]*2.5)+(zip12401[zip12401.columns[7]]*7.5)+(zip12401[zip12401.columns[8]]*12.5)+(zip12401[zip12401.columns[9]]*17.5)) #y axis percentage (temperary dumby variable)

axes[0,0].set_title('12206')
axes[0,0].plot(X1,Y1)

axes[0,1].set_title('12601')
axes[0,1].plot(X2,Y2)

axes[0,2].set_title('14212')
axes[0,2].plot(X3,Y3)

axes[0,3].set_title('14211')
axes[0,3].plot(X4,Y4)

axes[1,0].set_title('14208')
axes[1,0].plot(X5,Y5)

axes[1,1].set_title('14213')
axes[1,1].plot(X6,Y6)

axes[1,2].set_title('14215')
axes[1,2].plot(X7,Y7)

axes[1,3].set_title('14207')
axes[1,3].plot(X8,Y8)

axes[2,0].set_title('12078')
axes[2,0].plot(X9,Y9)

axes[2,1].set_title('14611')
axes[2,1].plot(X10,Y10)

axes[2,2].set_title('14621')
axes[2,2].plot(X11,Y11)

axes[2,3].set_title('12010')
axes[2,3].plot(X12,Y12)

axes[3,0].set_title('13501')
axes[3,0].plot(X13,Y13)

axes[3,1].set_title('13502')
axes[3,1].plot(X14,Y14)

axes[3,2].set_title('13204')
axes[3,2].plot(X15,Y15)

axes[3,3].set_title('13208')
axes[3,3].plot(X16,Y16)

axes[4,0].set_title('12550')
axes[4,0].plot(X17,Y17)

axes[4,1].set_title('12180')
axes[4,1].plot(X18,Y18)

axes[4,2].set_title('12401')
axes[4,2].plot(X19,Y19)

axes[4,3].set_title('12401')
axes[4,3].plot(X20,Y20)

plt.show()

#Step 5 Make predictions from the data (machine learning)
#given that this is time series data I think a basic linear or loggistic regression would be most effective at making predictions



#step 6 we can augment new data from other sources to try and determine why some regeions have higher lead levels than others

#step 7 lets test our prediction on new data (Model evaluation)

#step 8 we can tell a story with this data and use our visuals & predections to help convey the message that we are trying to send
#lets do this via statistical analysis (i.e is there a correlation between lead and economic hardship)

#step 9 Analyse outliars and see what we can learn from them

#step 10 make suggestions that are feasible and can have the greatest impact with minimal costs
