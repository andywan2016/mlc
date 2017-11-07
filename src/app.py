from mlc_class import life_table_array,MLC



def find_premiun(age):
   life_table=life_table_array()
   mlc=MLC(20,life_table)
   xPn_list=[abs(mlc.pn_x(age,x)-0.975) for x in range(19)]
   index=0
   pivot=xPn_list.index(min(xPn_list))
   print(pivot)
   G=100000*mlc.discount(pivot)/mlc.a_n(pivot)

   return G


if __name__=='__main__':
   print(find_premiun(40))	

