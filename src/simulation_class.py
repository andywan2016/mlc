import random
import pandas as pd
from mlc_class import life_table_array,MLC



def simulation(mlc_obj,start_yr,yr_steps,insurance,premiun):
   for i in range(yr_steps):
      rand_num=random.uniform(0,1)	   
      qx=mlc_obj.qx(start_yr+i)
      if rand_num<qx:
         return {'age':start_yr+i,'status':'dead','profit':mlc_obj.actual_profit(insurance,premiun,i+1,True)}
      else:
	 continue      
   return {'age':start_yr+yr_steps,'status':'survive','profit':mlc_obj.actual_profit(insurance,premiun,yr_steps,False)}
   

# simluation n times and return value
def sim_times(n,mlc_obj,start_yr,yr_steps,insurance,premiun):
  output=[]
  for i in range(n):
    sim_result=simulation(mlc_obj,start_yr,yr_steps,insurance,premiun)
    output.append(sim_result)
   # print(output)
    
  return pd.DataFrame(output) 
    
def pos_percen(df):
   return df.loc[df['profit']>0]


if __name__=='__main__':
   life_table=life_table_array()
   mlc=MLC(30,life_table)
   
   #for i in range(100):
     # print(simulation(mlc,40,20,100000,8210))
   result=sim_times(10000,mlc,50,20,100000,16735)
   count=pos_percen(result)
   print(count.shape)
