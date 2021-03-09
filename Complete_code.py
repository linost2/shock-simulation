# 变量初始化过程包括路径、变量名
path="C:/Users/Youlin Zhu/Desktop/" #文件所在目标路径
input_filename = "pressure.profile" #文件名
mergespace_file = "pressure_c.txt" 
parse_file = "2.xlsx"
fullfill_file=""
extract_file=""
Vz_extract_file=""

# 将初始文件首行连续空格转化为一个写入一个新文件output_filename
import pandas as pd
from openpyxl import *
def mergespace():
    f=open (path+input_filename,"r+")
    f1=open (path+mergespace_file,"w")
    data=f.readlines()
    for line in data:
        if line[0]==" ":
            f1.write(line[1:])
        else:
            f1.write(line[0:])

    f.close()
    f1.close()



#数据按空格分列后转化为数值写入excel,column为表头（第一行）名称
def parse():
    df = pd.read_csv(path+mergespace_file)
    column='# Chunk-averaged data for fix pressure_profile and group v_pressurexx'
    df= df[column].str.split(" ",expand=True)
    df.iloc[2:,:]=df.iloc[2:,:].apply(pd.to_numeric)
    df.to_excel(path+parse_file,index=False,header=False)

#填充时间，根据步长转化为ps
def fullfill():
    row=ws.max_row
    for i in range(1,row+1): 
        if ws.cell(i,1).value is None:
            if ws.cell(i,2).value==1:
                ws.cell(i,1).value=ws.cell(i-1,1).value/1000 #除数为：1ps/以fs为单位的步长
            else:
                ws.cell(i,1).value=ws.cell(i-1,1).value
            if ws.cell(i+1,2).value is  None:
                print("数据填充完毕，谢谢")
                



def extract_int():
    m=1#新表初始列坐标
    l=1#新表初始行坐标
    wb =load_workbook("path+fullfill_file") #读取保存的文件          
    ws=wb["Sheet1"]  
    for j in range(1,1000000):
        if str(ws.cell(j,1).value).isdigit() and ws.cell(j,1).value<100：
        #筛条件可更改，当前为小于100的整数
        #抽取列可更改，当前为1，3，6
            ws2.cell(l,m).value=ws.cell(j,1).value
            ws2.cell(l,m+1).value=ws.cell(j,3).value
            ws2.cell(l,m+2).value=ws.cell(j,6).value
            l+=1
            if ws.cell(j+1,1).value!=ws.cell(j,1).value:
                m+=3
                l=1
           
        if ws.cell(j+1,2).value is  None:
                print("数据提取完毕，谢谢")
                break

wb =load_workbook(path+parse_file) #原始数据文件      
ws=wb["Sheet1"]                       
fullfill()  
wb.save("path+fullfill_file") 
wb2 = Workbook()
ws2 = wb2.active
extract_int()
wb2.save("path+extract_file")#根据抽取列确定所提取信息文件名
print("搞定！")
wb3 =load_workbook(Vz_extract_file)   
ws=wb3["Sheet1"]   

#抽取自由面速度Vz
 
def extract_Vz():                    
    j=0                              
    row=ws.max_row
    for i in range(2,row):        
        if ws.cell(i,2).value==1:     #每次循环从1开始，始终不变
            k=ws.cell(i-1,2).value-2  #获得每次循环第一个位置加上对应该循环中个数即为最后一个值（n+m-1)
            j+=1 #获得循环的次数
            mylog = open('recode.txt', mode = 'a',encoding='utf-8')  #写入数据到txt文件第一步
            print(j*0.04,ws.cell(i+k,5).value/10)  #j乘数为跨度×步长除以1000，单位ps
            print(j*0.04,ws.cell(i+k,5).value/10,file=mylog)  #写入数据到txt，写入数据到txt文件第二步，file数据写入txt中
            # ~ ws["Gj"].value=ws.cell(i+k,5).value/10
            # ~ wb.save("p.xlsx") 
    #----当最后一个循环结束，下一个循环第一位为空，结束程序----
        if ws.cell(i,2).value is None: 
            print("数据读取完毕，谢谢")
            # ~ print("数据读取完毕，谢谢",file=mylog) #写入数据到txt文件第三步，file数据写入txt中
            mylog.close()	#写入数据到txt文件第四步，关闭这个变量并储存
            break

