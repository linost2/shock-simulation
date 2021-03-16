
#抽取整数秒数据
def extract_int(): 
    wb2 = Workbook()
    ws2 = wb.active
    m=1#新表初始列坐标
    l=1#新表初始行坐标
    wb =load_workbook("path+fullfill_file") #读取保存的文件          
    ws =wb["Sheet1"]  
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
    wb2.save("path+fullfill_file") 
        
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
 