# 变量初始化过程包括路径、变量名
path="C:/Users/Youlin Zhu/Desktop/" #文件所在目标路径

input_filename = "pressure.profile" #文件名
output_filename = "pressure_c.txt" 
final_filename = "2.xlsx"

#将初始文件首行连续空格转化为一个写入一个新文件output_filename
import pandas as pd
f=open (path+input_filename,"r+")
f1=open (path+output_filename,"w")
data=f.readlines()
for line in data:
    if line[0]==" ":
        f1.write(line[1:])
    else:
        f1.write(line[0:])

f.close()



#数据按空格分列后转化为数值写入excel,column为表头（第一行）名称
df = pd.read_csv(path+output_filename)
column='# Chunk-averaged data for fix pressure_profile and group v_pressurexx'
df= df[column].str.split(" ",expand=True)
df.iloc[2:,:]=df.iloc[2:,:].apply(pd.to_numeric)
df.to_excel(path+final_filename,index=False,header=False)


# import openpyxl as op
# wb = op.load_workbook('C:/Users/Youlin Zhu/Desktop/2.xlsx')
# ws = wb['Sheet1']
# for row in ws:
#     for cell in row:
#         float(cell)
# wb.save('C:/Users/Youlin Zhu/Desktop/3.xlsx')

# wb =op.load_workbook(final_filename) #原始数据文件      
# ws=wb["Sheet1"]             #sheet名称


# def fullfill():
#     row=ws.max_row
#     for i in range(1,row+1): 
#         if ws.cell(i,1).value is None:
#             if ws.cell(i,2).value==1:
#                 ws.cell(i,1).value=ws.cell(i-1,1).value/5000
#             else:
#                 ws.cell(i,1).value=ws.cell(i-1,1).value
#             if ws.cell(i+1,2).value is  None:
#                 print("数据填充完毕，谢谢")
                       
# fullfill()  
# wb.save("pressure_full.xlsx")  