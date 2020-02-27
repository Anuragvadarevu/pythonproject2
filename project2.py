
#created a class name as car
class car:
	#constructor
    def __init__(self,effiency):
        self.effiency=effiency
        self.fuel=0
      
        #opening the text file 'FuelEffic.txt'  which contain tank capcity and miles per gallon and reading them
        infile=open("FuelEffic.txt","r")
        #storing the lines of txt file in new varible called line
        line=infile.readlines()
        
        #just taking the integer values from the txt file string them in new variables
        self.millage=float(line[0].split(' ')[3])
        self.sizeoftank=float(line[1].split(' ')[4])
        #calculating total distance in miles
        self.totaldistance=self.millage*self.sizeoftank
  
     #defining methods  
    def drive(self,distance):
		
        gasafterdrive= self.fuel-((self.effiency*self.fuel)-distance)/self.effiency
        self.fuel=self.fuel-gasafterdrive

        
       
        
      
    def getfuellevel(self):
        return self.fuel
  
    def addGas(self,gas):
        self.fuel=self.fuel+gas
        if(self.fuel>self.sizeoftank):                                                                
            self.fuel=self.sizeoftank 
	
       
       
 


	
a=20
myhybrid=car(a)

#infinityloop 
while True:
	#opening  the new file 
	infile1=open("LogFuel.txt","w")
			
	#displaying the menu
	print('select from the below menu ')
	print('         1. see current fuel')
	print('         2.drive')
	print('         3.add gas ')
	print('         4.exit')
	infile1.write("select from the below menu")
	infile1.write("1.see current fuel")
	infile1.write("2.drive")
	infile1.write("3.add gas")
	infile1.write("4.exit")
	value=int(input('enter the option you prefer: '))
	print('entered option is',value)
	#we will find the level of fuel
	if value==1:
		infile1.write('Input is 1\n')
		infile1.write("The current fuel level is "+str(myhybrid.getfuellevel())+'')
		
		print('level of gas is: ',myhybrid.getfuellevel())
		print('')
	#by selecting option 2 we will store how much distance we want to travel
	if value==2:
		print('')
		print('How many miles to Drive? :')
		print('')
		b=float(input())
		myhybrid.drive(b)
		n=myhybrid.totaldistance-b
		print('you can drive '+str(b)+'  still   '+str(n)+'  miles are left')
		infile1.write('Input is 2\n')
		infile1.write("numberof miles to drive"+str(b)+"")
		infile1.write("you can drive: "+str(b)+"")		
		
			
	if value==3:
		print('How much gas to Add: ')
		print('')
		c=float(input('no of gallons to be added: '))
		myhybrid.addGas(c)
		print('gas added is',myhybrid.getfuellevel(),'gallons')
		infile1.write('')
		infile1.write('Input is 3\n')
		infile1.write("numberof gallons to be added"+str(c)+"")		
	if value==4:
		infile1.write('')
		
		infile1.write('Input is 4\n')
		infile1.write('exit')
		print('exit')
		exit()
   
