import random
from mlc_class import life_table_array,MLC



def simulation(mlc_obj,start_yr,yr_steps):
   for i in range(yr_steps):
      rand_num=random.uniform(0,1)	   
      qx=mlc_obj.qx(start_yr+i)
      if rand_num<qx:
         return [start_yr+i,'dead']
      else:
	 continue      
   return [start_yr+yr_steps,'survive']
   

if __name__=='__main__':
   life_table=life_table_array()
   mlc=MLC(30,life_table)
   
   for i in range(20):
      print(simulation(mlc,30,20))
