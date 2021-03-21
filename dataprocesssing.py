#该代码实现对于目标文件夹下pressure.profile的遍历、数据处理及绘图，作者Youlin 
#运行前记得关闭excel、txt等程序的占用

import pandas as pd
import os

input_filename = "pressure.profile" #原始数据文件名
mergespace_file = "mergespace.txt"  #合并空格后文件名
parse_file = "parse.xlsx"           #分列后文件名
fullfill_file="fullfill.xlsx" 
cut_file='cut.xlsx'      #填充后文件名


# 变量初始化过程包括路径、变量名
def main():
    rootdir=r"D:\Youlin Zhu\2021实验室\分子动力学\数据处理\strainrate"
    global list
    list = os.listdir(rootdir)

    for i in range(len(list)):
        global path
        path = os.path.join(rootdir,list[i])
        print ("我正在"+path+"下处理！")
        data_processing()
        
# 将初始文件首行连续空格转化为一个写入一个新文件mergespace_filename
def mergespace():
    f=open (path+'/'+input_filename,"r")
    f1=open(path+'/'+mergespace_file,"w")
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
    df = pd.read_csv(path+'/'+mergespace_file)
    column='# Chunk-averaged data for fix pressure_profile and group v_pressurexx'
    df= df[column].str.split(" ",expand=True)
    df.iloc[2:,:]=df.iloc[2:,:].apply(pd.to_numeric)
    df1=df.drop(labels=range(0,1),axis=0)
    df1.to_excel(path+'/'+parse_file,index=False,header=0)  

#填充时间，根据步长转化为ps
def fullfill():
    df=pd.read_excel(path+'/'+parse_file,header=0)
    k=df.shape[0]
    for i in range(k):
        if pd.isna(df.iloc[i,0]):
            if df.iloc[i,1]==1:
                df.iloc[i,0]=df.iloc[i-1,0]/1000
            else:
                df.iloc[i,0]=df.iloc[i-1,0]
                
#删除最后一个切片数据
def cut_lastbin():                
    df.to_excel(path+'/'+fullfill_file,index=False)  
    def cut_lastbin():
    df=pd.read_excel(path+'/'+fullfill_file,header=0)
    k=df.shape[0]
    index_to_drop=[]
    index_to_drop.append(k-1)
    for i in df.index:
        if df.iloc[i,0]>200:
            index_to_drop.append(i-1)
    df.drop(df.index[index_to_drop],inplace=True)
    df.to_excel(path+'/'+cut_file,index=False)

#调用数据处理       
def data_processing():
    mergespace()
    parse()
    fullfill()
    cut_lastbin

#运行主函数，等待收获数据
main()    
print("帮你处理了{}个文件，有点辛苦".format(len(list)))