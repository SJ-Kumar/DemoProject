import pandas as pd
import xlrd

class datafromexcel:
       
    df = pd.read_excel('Investment.xls', sheet_name=[2,3])  
    print("Successfully retrieved all excel data"); 
    
    df2 = df.copy()
    print(df2);
with pd.ExcelWriter('Investment.xls') as writer:
    
    pd.ExcelWriter (writer, sheet_name ='Sheet1')
    
    ##print(sheet.cell_value(0, 0))
    ##print(df.columns.name)
    
     
    
    