import requests
import csv
from bs4 import BeautifulSoup
from datetime import date, timedelta

def dscrape(url1):

    url = 'http://www.zulubet.com/tips-' + url1 + '.html'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    name = list()
    st = 0
    l = 31
    wii = 0

    a = soup.find_all('td')

    b = soup.find_all('script')

    c = soup.find_all('td', attrs={'class': 'prob2 prediction_full'})

    d = soup.find_all('td', attrs={'class': 'aver_odds_full'})

    e = soup.find_all('td', attrs={'align': 'center'})

    for i in range(25, len(a), 17):
        if a[i - 1].text.startswith('user'):
            name.append(str(a[i].text).strip())

    with open('DB/' + url1 + '.csv', 'w') as csvfile:
        sw = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        sw.writerow([
            'ID',
            'Match_name',
            'Date_Time',
            'Prediction_1',
            'Prediction_X',
            'Prediction_2',
            'Average_1',
            'Average_X',
            'Average_2',
            'Final_Result',
            'Value_1',
            'Value_X',
            'Value_2',
            'Probability_1',
            'Probability_X',
            'Probability_2',
            'Edge_1',
            'Edge_X',
            'Edge_2',
            ])
        i = 0
        for j in range(len(name)):
            if len(name[j]) > 2:
                p1 = float(str(c[i].text).split('%')[0])
                if p1<4:
                	p1=1
                p2 = float(str(c[i + 1].text).split('%')[0])
                if p2<4:
                	p2=1
                p3 = float(str(c[i + 2].text).split('%')[0])
                if p3<4:
                	p3=1
                a1 = float(100 / (100 / float(d[i + 1].text) - 3))
                if a1<1:
                	p1=1
                	a1=100
                if a1>100:
                	p1=1
                	a1=100
                a2 = float(100 / (100 / float(d[i + 2].text) - 3))
                if a2<1:
                	p2=1
                	a2=100
                if a2>100:
                	p2=1
                	a2=100
                a3 = float(100 / (100 / float(d[i + 3].text) - 3))
                if a3<1:
                	p3=1
                	a3=100
                if a3>100:
                	p3=1
                	a3=100
                v1 = p1 * a1 / 100
                v2 = p2 * a2 / 100
                v3 = p3 * a3 / 100
                q1 = 100 / a1
                q2 = 100 / a2
                q3 = 100 / a3
                ed1 = p1 - q1
                ed2 = p2 - q2
                ed3 = p3 - q3
                sw.writerow([
                    str(st),
                    str(name[j]),
                    str(b[6 + j].text)[10:27],
                    str(p1),
                    str(p2),
                    str(p3),
                    str(a1)[0:4],
                    str(a2)[0:4],
                    str(a3)[0:4],
                    str(e[l].text),
                    str(v1)[0:4],
                    str(v2)[0:4],
                    str(v3)[0:4],
                    str(q1)[0:4],
                    str(q2)[0:4],
                    str(q3)[0:4],
                    str(ed1)[0:4],
                    str(ed2)[0:4],
                    str(ed3)[0:4],
                    ])
                l = l + 13
                i = i + 3
                st = st + 1


def opendata(url1, edg, h,fod, od1, od2):
    sum2=[0,0]
    with open('DB/' + url1 + '.csv', 'r') as csvfile:
        cs = csv.reader(csvfile, delimiter=',')
        for i in cs:
            try:
                if i[0] == 'ID':
                	continue
            except:
            	continue
            #changes
            wilo="LOSS"
            idd=str(i[0])
            datt=str(i[2])
            name=str(i[1])
            fr=str(i[9])
            if len(fr.strip())<2:
            	continue
            fr1=int((fr.split(':'))[0])
            fr2=int((fr.split(':'))[1])
            p1 = float(i[3])
            p2 = float(i[4])
            p3 = float(i[5])
            a1 = float(i[6])
            a2 = float(i[7])
            a3 = float(i[8])
            v1 = float(i[10])
            v2 = float(i[11])
            v3 = float(i[12])
            q1 = float(i[13])
            q2 = float(i[14])
            q3 = float(i[15])
            ed1 = float(i[16])
            ed2 = float(i[17])
            ed3 = float(i[18])

            with open('temp2.csv', 'a') as csvfile:
            					sw = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            					sw.writerow([
            						idd,
            						name,
            						datt,
            						str(p1),
            						str(p2),
            						str(p3),
            						str(a1),
            						str(a2),
            						str(a3),
            						fr,
            						str(v1),
            						str(v2),
            						str(v3),
            						str(q1),
            						str(q2),
            						str(q3),
            						str(ed1),
            						str(ed2),
            						str(ed3),])

            if (h=="HOME") and (od1<=a1) and (od2>=a1):
            	if(ed1>=edg):

            		if (fod=="NA"):
            			if(fr1>fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            				#change
            			sum2[0]=sum2[0]+1
            			f=open("temp.csv",'a')
            			f.write(name+','+str(ed1)+','+fr+','+wilo+','+str(a1)+'\n') #change
            			f.close()
            			
            		elif (fod=="FAV"):
            			if(fr1>fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            				#change
            			sum2[0]=sum2[0]+1
            			if(q1>q2) and (q1>q3):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed1)+','+fr+','+wilo+','+str(a1)+'\n') #change 
            				f.close()
            				
            		elif (fod=="DOG"):
            			if(fr1>fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            				#change
            			sum2[0]=sum2[0]+1
            			if(q1<q2) and (q1<q3):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed1)+','+fr+','+wilo+','+str(a1)+'\n') #change
            				f.close()
            				
            if (h=="DRAW") and (od1<=a2) and (od2>=a2):
            	if(ed2>=edg):
            		if(fr1==fr2):
            			sum2[1]=sum2[1]+a2
            			wilo="WIN"
            		sum2[0]=sum2[0]+1
            		f=open("temp.csv",'a')
            		f.write(name+','+str(ed2)+','+fr+','+wilo+','+str(a2)+'\n') #change
            		f.close()

            				
            elif (h=="AWAY") and (od1<=a3) and (od2>=a3):
            	if(ed3>=edg):
            		if (fod=="NA"):
            			if(fr1<fr2):
            				sum2[1]=sum2[1]+a3
            				wilo="WIN"
            				#change
            			sum2[0]=sum2[0]+1
            			f=open("temp.csv",'a')
            			f.write(name+','+str(ed3)+','+fr+','+wilo+','+str(a3)+'\n') #change
            			f.close()
            			
            		elif (fod=="FAV"):
            			if(fr1<fr2):
            				sum2[1]=sum2[1]+a3
            				wilo="WIN"
            				#change
            			sum2[0]=sum2[0]+1
            			if(q3>q2) and (q3>q1):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed3)+','+fr+','+wilo+','+str(a3)+'\n') #change
            				f.close()
            				
            		elif (fod=="DOG"):
            			if(fr1<fr2):
            				sum2[1]=sum2[1]+a3
            				wilo="WIN"
            				#change
            			sum2[0]=sum2[0]+1
            			if(q3<q1) and (q3<q2):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed3)+','+fr+','+wilo+','+str(a3)+'\n') #change
            				f.close()
            				
            elif (h=="ALL") and (od1<=a2) and (od2>=a2) and (od1<=a1) and (od2>=a1) and (od1<=a3) and (od2>=a3):
            	
            	if(ed1>=edg):

            		sum2[0]=sum2[0]+1
            		if (fod=="NA"):
            			if(fr1>fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            			f=open("temp.csv",'a')
            			f.write(name+','+str(ed1)+','+fr+','+wilo+','+str(a1)+'\n') #change
            			f.close()
            			
            		elif (fod=="FAV"):
            			if(fr1>fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            			
            			if(q1>q2) and (q1>q3):
            				
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed1)+','+fr+','+wilo+','+str(a1)+'\n') #change
            				f.close()
            				
            		elif (fod=="DOG"):
            			if(fr1>fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            			if(q1<q2) and (q1<q3):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed1)+','+fr+','+wilo+','+str(a1)+'\n') #change
            				f.close()
            				

            	if(ed3>=edg):

            		sum2[0]=sum2[0]+1
            		if (fod=="NA"):
            			if(fr1<fr2):
            				sum2[1]=sum2[1]+a3
            				wilo="WIN"
            			f=open("temp.csv",'a')
            			f.write(name+','+str(ed3)+','+fr+','+wilo+','+str(a3)+'\n') #change
            			f.close()
            			
            		elif (fod=="FAV"):
            			if(fr1<fr2):
            				sum2[1]=sum2[1]+a3
            				wilo="WIN"
            			if(q3>q2) and (q3>q1):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed3)+','+fr+','+wilo+','+str(a3)+'\n') #change
            				f.close()
            				
            		elif (fod=="DOG"):
            			if(fr1<fr2):
            				sum2[1]=sum2[1]+a3
            				wilo="WIN"
            			if(q3<q1) and (q3<q2):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed3)+','+fr+','+wilo+','+str(a3)+'\n') #change
            				f.close()
            				

            	if(ed2>=edg):

            		sum2[0]=sum2[0]+1
            		if (fod=="NA"):
            			if(fr1==fr2):
            				sum2[1]=sum2[1]+a2
            				wilo="WIN"
            			f=open("temp.csv",'a')
            			f.write(name+','+str(ed2)+','+fr+','+wilo+','+str(a2)+'\n') #change
            			f.close()
            			
            		elif (fod=="FAV"):
            			if(fr1==fr2):
            				sum2[1]=sum2[1]+a2
            				wilo="WIN"
            			if(q2>q1) and (q2>q1):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed2)+','+fr+','+wilo+','+str(a2)+'\n') #change
            				f.close()
            				
            		elif (fod=="DOG"):
            			if(fr1==fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            			if(q2<q1) and (q2<q3):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed2)+','+fr+','+wilo+','+str(a2)+'\n') #change
            				f.close()
            				

            elif (h=="1X") and (od1<=(a2+a1)/2) and (od2>=(a2+a1)/2):

            	pr=p1+p2
            	pro=q1+q2
            	edd=pr-pro
            	if(edd>=edg):
            		if (fod=="NA"):
            			if(fr1>=fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            				#change
            			sum2[0]=sum2[0]+1
            			f=open("temp.csv",'a')
            			f.write(name+','+str(edd)[0:4]+','+fr+','+wilo+','+str((a1+a2)/2)+'\n') #change
            			f.close()
            			
            		elif (fod=="FAV"):
            			if(fr1>=fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            				#change+a2
            			sum2[0]=sum2[0]+1
            			
            			if(q1>q2) and (q1>q3):
            				
            				f=open("temp.csv",'a')
            				f.write(name+','+str(edd)[0:4]+','+fr+','+wilo+','+str((a1+a2)/2)+'\n') #change
            				f.close()
            				
            		elif (fod=="DOG"):
            			if(fr1>=fr2):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            				#change+a2
            			sum2[0]=sum2[0]+1
            			if(q1<q2) and (q1<q3):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(edd)[0:4]+','+fr+','+wilo+','+str((a1+a2)/2)+'\n') #change
            				f.close()

            elif(h=="12") and (od1<=(a3+a1)/2) and (od2>=(a3+a1)/2):
            	if(ed1>=edg):
            		if (fod=="NA"):
            			if((fr1>fr2) or (fr1<fr2)):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            				#change+a3
            			sum2[0]=sum2[0]+1
            			f=open("temp.csv",'a')
            			f.write(name+','+str(ed1)+','+fr+','+wilo+','+str(a1)+'\n') #change
            			f.close()
            			
            		elif (fod=="FAV"):
            			if((fr1>fr2) or (fr1<fr2)):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            				#change+a3
            			sum2[0]=sum2[0]+1
            			
            			if(q1>q2) and (q1>q3):
            				
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed1)+','+fr+','+wilo+','+str(a1)+'\n') #change
            				f.close()
            				
            		elif (fod=="DOG"):
            			if((fr1>fr2) or (fr1<fr2)):
            				sum2[1]=sum2[1]+a1
            				wilo="WIN"
            				#change+a3
            			sum2[0]=sum2[0]+1
            			if(q1<q2) and (q1<q3):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed1)+','+fr+','+wilo+','+str(a1)+'\n') #change
            				f.close()
            				

            	if(ed3>=edg):
            		if (fod=="NA"):
            			if((fr1>fr2) or (fr1<fr2)):
            				sum2[1]=sum2[1]+a3
            				wilo="WIN"
            				#change+a3
            			sum2[0]=sum2[0]+1
            			f=open("temp.csv",'a')
            			f.write(name+','+str(ed3)+','+fr+','+wilo+','+str(a3)+'\n') #change
            			f.close()
            			
            		elif (fod=="FAV"):
            			if((fr1>fr2) or (fr1<fr2)):
            				sum2[1]=sum2[1]+a3
            				wilo="WIN"
            				#change+a3
            			sum2[0]=sum2[0]+1
            			if(q3>q2) and (q3>q1):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed3)+','+fr+','+wilo+','+str(a3)+'\n') #change
            				f.close()
            				
            		elif (fod=="DOG"):
            			if((fr1>fr2) or (fr1<fr2)):
            				sum2[1]=sum2[1]+a3
            				wilo="WIN"
            				#change+a3
            			sum2[0]=sum2[0]+1
            			if(q3<q1) and (q3<q2):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(ed3)+','+fr+','+wilo+','+str(a3)+'\n') #change
            				f.close()


            elif (h=="X2") and (od1<=(a2+a3)/2) and (od2>=(a2+a3)/2):
            	pr=p3+p2
            	pro=q3+q2
            	edd=pr-pro
            	if(edd>=edg):
            		if (fod=="NA"):
            			if(fr1<=fr2):
            				sum2[1]=sum2[1]+a2
            				wilo="WIN"
            				#change+a3
            			sum2[0]=sum2[0]+1
            			f=open("temp.csv",'a')
            			f.write(name+','+str(edd)[0:4]+','+fr+','+wilo+','+sstr((a3+a2)/2)+'\n') #change
            			f.close()
            			
            		elif (fod=="FAV"):
            			if(fr1<=fr2):
            				sum2[1]=sum2[1]+a2
            				wilo="WIN"
            				#change+a3
            			sum2[0]=sum2[0]+1
            			if(q3>q2) and (q3>q1):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(edd)[0:4]+','+fr+','+wilo+','+str((a3+a2)/2)+'\n') #change
            				f.close()
            				
            		elif (fod=="DOG"):
            			if(fr1<=fr2):
            				sum2[1]=sum2[1]+a2
            				wilo="WIN"
            				#change+a3
            			sum2[0]=sum2[0]+1
            			if(q3<q1) and (q3<q2):
            				f=open("temp.csv",'a')
            				f.write(name+','+str(edd)[0:4]+','+fr+','+wilo+','+str((a3+a2)/2)+'\n') #change
            				f.close()
            				          
            				 	
        return sum2
of="1"
date1=str("15-04-2017").strip().split("-")
date2=str("15-04-2017").strip().split("-")
edg=float(10)
h=input("enter home/draw/away/all/1x/x2/12: ")
fod=input("enter fav or dog: ")
od1=float(input("Enter odd value(min): ")) #change
od2=float(input("Enter odd value(max): ")) #change

d1 = date(int(date1[2]), int(date1[1]), int(date1[0]))  # start date
d2 = date(int(date2[2]), int(date2[1]), int(date2[0]))
f1=open("temp.csv",'w')
f1.close()
with open('temp2.csv', 'w') as csvfile:
        sw = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        sw.writerow([
            'ID',
            'Match_name',
            'Date_Time',
            'Prediction_1',
            'Prediction_X',
            'Prediction_2',
            'Average_1',
            'Average_X',
            'Average_2',
            'Final_Result',
            'Value_1',
            'Value_X',
            'Value_2',
            'Probability_1',
            'Probability_X',
            'Probability_2',
            'Edge_1',
            'Edge_X',
            'Edge_2',
            ])
delta = d2 - d1         # timedelta
sum1=[0,0]
if (of=='0'):
    for i in range(delta.days + 1):
    	j=str(d1 + timedelta(days=i))
    	dat=j.split("-")
    	date1=str(dat[2]+'-'+dat[1]+'-'+dat[0])
    	dscrape(date1)
    	su=opendata(date1, edg, h, fod, od1, od2) #change
    	sum1[0]=sum1[0]+su[0]
    	sum1[1]=sum1[1]+su[1]
else:
    for i in range(delta.days + 1):
    	j=str(d1 + timedelta(days=i))
    	dat=j.split("-")
    	date1=str(dat[2]+'-'+dat[1]+'-'+dat[0])
    	try:
    		su=opendata(date1, edg, h, fod, od1, od2) #change
    	except:
    		print(date1, "not in database")
    	sum1[0]=sum1[0]+su[0]
    	sum1[1]=sum1[1]+su[1]
f=open("temp.csv",'r')
read = csv.reader(f,delimiter = ",")
total=0
for i in read:
	total=total+1
print("total winnings = ", str(sum1[1])[0:5])#changed
print("total bets = ", sum1[0])
print("net winnings = ", str(sum1[1]-sum1[0])[0:5]) #changed
