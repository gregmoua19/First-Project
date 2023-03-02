import pandas as pd
import numpy as np
test = ["first name",2,3,4,5,6,7,8,9],["stuff i bought",8,7,6,5,4,3,2,1]
test_Data = pd.DataFrame(test)
print(test_Data)
print("\n")


#print(test_Data[0][0])
print(test_Data.to_numpy())
#for i in range(len(test)):
#    print(i)
#    for j in range(len(test[i])):
#        print(test[i][j])