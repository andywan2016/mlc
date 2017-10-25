import csv


#life table class define

class life_table:
   def __init__(self):
      life_table=[]
      with open('../data/life_table.csv','r') as f:
         reader=csv.reader(f)
         for row in reader:
            life_table.append(int(row[1]))
      self.table=life_table  

   def print_table(self):
      print(self.table)
      



class MLC:
#this class include the functions in mlc


   def __init__(self,age,table):
   #constructor function which assign age and time table  
      self.age=age
      self.table=table.table

   def get_lx(self):
   #get number of lives
     try:
        return self.table[self.age]
     except IndexError:
        print("age out range of life table")

   def get_dx(self)
      try:
         return self.table[self.age+1]-self.table[self.age]
      except IndexError:
         print("life age out of range")

   def term_insurance(self,term_years):
      



new_table=life_table()
#new_table.print_table()
new_MLC=MLC(3,new_table)
print(new_MLC.get_lx())
