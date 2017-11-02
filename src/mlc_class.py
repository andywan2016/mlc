import csv


#life table class define

class life_table_csv:
      

   
   def __init__(self):
      life_table=[]
      with open('../data/life_table.csv','r') as f:
         reader=csv.reader(f)
         for row in reader:
            life_table.append(int(row[1]))
      self.table=life_table  

   def print_table(self):
      print(self.table)
      
#the life talbe class initialized with a static array
class life_table_array:
   
   
   def __init__(self):
      self.interest=0.06
      
      #the array is from 2008 life table 's life numbers.
      self.table=[100000,99341,99295,99267,99245,99228,99213,99199,99187,99176,99167,99158,99150,99138,99118,99089,99050,99002,98944,98878,98804,98722,98632,98536,98438,98341,98245,98150,98056,97960,97863,97763,97660,97554,97443,97328,97207,97080,96944,96798,96639,96468,96281,96076,95850,95602,95331,95038,94719,94374,93999,93592,93151,92678,92173,91635,91062,90453,89801,89104,88356,87552,86690,85766,84777,83720,82585,81364,80052,78649,77153,75563,73865,72043,70090,68006,65792,63449,60970,58343,55562,52644,49607,46454,43176,39797,36341,32823,29284,25774,22347,19062,15971,13123,10557,8303,6373,4766,3467,2451,1681]     


class MLC:
#this class include the functions in mlc


   def __init__(self,age,table):
   #constructor function which assign age and time table  
      self.age=age
      self.table=table.table
      self.interest=table.interest

   def lx(self,year):
   #get number of lives
     try:
        return self.table[year]
     except IndexError:
        print("age out range of life table")
   
   #get the death number of a year
   def dx(self,year):
      try:
         return self.table[year]-self.table[year+1]
      except IndexError:
         print("life age out of range")
   
#get the probablity of death for a year
   def qx(self,year):
      try:
         return float(self.dx(year))/self.lx(year)
      except IndexError:
         print("life age out of range")
   
#nPx the probablity of in age x  survial  in n years 
   def pn_x(self,year,term):
      try:
         return float(self.lx(year+term))/self.lx(year)
      except IndexError:
         print("age out of range")

#EPV(Expected Present Value ) Function
   def EPV(self,year,term):
      return self.pn_x(year,term)/((1+self.interest)**term)
      



#Term Insurance(Without Endowment) Function
   def Ax_n_1(self,age,term):
      output=0
      for i in range(1,term+1):
         qx_n_1=self.pn_x(age,i-1)*self.qx(age+i-1)
	 discount_factor=(1/(1+self.interest))**i
         output=output+qx_n_1*discount_factor	       
            
      return output

# Endowment Function(=Term Insurance + EPV)
   def Ax_n(self,age,term):
      return self.Ax_n_1(age,term)+self.EPV(age,term)




#Anuity, using recursive function      
   def ax_n(self,age,term):
      return (1-self.Ax_n(age,term))/(self.interest/(1+self.interest))
    
    
    # if term==0:
      #   return 1
      #else: 
#	 return (self.ax_n(age-1,term+1)-1)/(self.interest*self.pn_x(age-1,age))	 

   def net_p(self,age,term):
      return self.Ax_n(age,term)/self.ax_n(age,term)


#Below part are for testing 
if __name__=="__main__":
   new_table=life_table_array()
  # print(new_table.table[1])
   #new_table.print_table()
   new_MLC=MLC(3,new_table)
  # print(new_MLC.dx(0))
  # print(new_MLC.qx(0))
   #print(new_MLC.pn_x(20,10))
   #print(new_MLC.Ax_n_1(20,25))
   #print(new_MLC.Ax_n(20,25))
   print("at age 40, 20 year endowment of $100,000 premium is: ")
   print(1000000*new_MLC.net_p(40,20))



