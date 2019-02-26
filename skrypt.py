import csv
freq=5180
def skan(freq):
	with open('xxx.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=",", quotechar="'")
		count=0
		power=0
		signal=0
		for row in spamreader:
			a =  (row[2])
			a=int(a[0:4])
			if( freq == a):
				signal = int(row[3])
				power = power + signal
				count+=1
		print("Suma sieci w częstoliwości",freq,"",count)
		print("Suma siły sygnału",power)
while(freq<5710):
	print (skan(freq))
	freq+=20
