#绘图代码:某时刻下参数（应力、温度、冲击方向速度）随切片位置分布的曲线绘制
import matplotlib.pyplot as plt
path=r"D:\Youlin Zhu\2021实验室\分子动力学\数据处理\strainrate\sample60\"
fullfill_file="fullfill.xlsx"

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
    #plt.xticks([200,400,600,800,1000])
    #plt.yticks([0,2,4,6,8],[0,0.2,0.4,0.6,0.8])
    plt.xlabel("Position (nm)",)
    plt.ylabel("Velocity Z (km/s)")
    #plt.savefig() 
    
    
def draw_freesurfaceVelocity():
    axistime=[]
    axisvelocity=[]
    df=pd.read_excel(path+fullfill_file,sheet_name=0)
    k=df.shape[0]
    for i in range(k):
    if df.iloc[i,0]>200:
        axistime.append(df1.iloc[i-1,0])
        axisvelocity.append(df1.iloc[i-1,8])
        
    plt.figure(num=1)
    plt.plot(axistime,axisvelocity)
    plt.plot(axistime,axisvelocity,color='purple',linewidth=1.5)
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    #plt.xticks([200,400,600,800,1000])
    plt.yticks([0,2,4,6,8],[0,0.2,0.4,0.6,0.8])
    plt.xlabel("Time (ps)",)
    plt.ylabel("Velocity Z (km/s)")
    
    #plt.savefig()    
    