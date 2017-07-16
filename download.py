import urllib2
i=1					#change it to any  value according to your url
while True:
	chr=str(i)
	ret = urllib2.urlopen("your URL"+chr+".jpg")  #this checks  for response  
	if ret.code == 200:
    		urllib2.urlretrieve("your url"+chr+".jpg",chr+".jpg") #this downloads in your current  directory
	i=i+1              #its infinite loop unless u want to make it  finite
