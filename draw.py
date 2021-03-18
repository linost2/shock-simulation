#该绘图代码根据需要筛选数据进行绘图，格式调整以及保存，作者Youlin Zhu

#导入绘图库，表格文件路径及名称
import matplotlib.pyplot as plt

path=r"D:\Youlin Zhu\2021实验室\分子动力学\数据处理\strainrate\sample60\"
fullfill_file="fullfill.xlsx"

#定位最负压力（层裂）时刻的坐标-速度数据绘图，参数按需修改
def draw_fixtime_curve():
    
    df=pd.read_excel(path+fullfill_file,sheet_name=0, header=0,index_col=0)
    goal_xaxis="Coord1"
    goal_yaxis="c_vx[1]"
    Tsp=df.idxmin()["v_pressurexx"] #定位时刻，可手动改为 XX (ps)
    xaxis=df.loc[Tsp,goal_xaxis].values
    yaxis=df.loc[Tsp,goal_yaxis].values
    
    plt.figure(num=1)
    plt.plot(xaxis,yaxis,color='blue',linewidth=1.5)
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.xticks([200,400,600,800,1000]，fontproperties = 'Times New Roman', size = 14)
    plt.yticks([0,2,4,6,8],[0,0.2,0.4,0.6,0.8]，fontproperties = 'Times New Roman', size = 14)
    plt.xlabel("Position (nm)",fontdict={'family' : 'Times New Roman', 'size'   : 16})
    plt.ylabel("Velocity Z (km/s)"，fontdict={'family' : 'Times New Roman', 'size'   : 16})
    #plt.savefig(r"C:\Users\Youlin Zhu\Desktop\1.tiff"，dpi=600) #保存
    
#提取自由表面速度数据绘图，参数按需修改  
def draw_freesurfaceVelocity():
    axistime=[]
    axisvelocity=[]
    df=pd.read_excel(path+fullfill_file,sheet_name=0)
    k=df.shape[0]
    for i in range(k):
    if df.iloc[i,0]>200:
        axistime.append(df1.iloc[i-1,0])
        axisvelocity.append(df1.iloc[i-1,8])
        
    plt.figure(num=2)        
    plt.plot(axistime,axisvelocity,color='purple',linewidth=1.5)
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.yticks([0,2,4,6,8,10],[0,0.2,0.4,0.6,0.8,1.0],fontproperties = 'Times New Roman', size = 14)
    plt.xlabel("Time (ps)",fontdict={'family' : 'Times New Roman', 'size'   : 16})
    plt.ylabel("Velocity Z (km/s)",fontdict={'family' : 'Times New Roman', 'size'   : 16})
    #plt.savefig(r"C:\Users\Youlin Zhu\Desktop\1.tiff",dpi=600)
 
draw_fixtime_curve()
draw_freesurfaceVelocity() 