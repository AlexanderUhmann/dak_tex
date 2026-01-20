col = 'enc_paym_15' 
T = X_pay.enc_paym_15
x00, x01 = T[(y==0) & (y_== 0)], T[ind_anom]  
x11, x01 = T[(y==1)], T[ind_anom]             
ind00 = (x00!=0) & (x00!=1) & (x00!=2) & (x00!=3) & (x00!=4) & (x00!=5)
ind01 = (x01!=0) & (x01!=1) & (x01!=2) & (x01!=3) & (x01!=4) & (x01!=5)
ind11 = (x11!=0) & (x11!=1) & (x11!=2) & (x11!=3) & (x11!=4) & (x11!=5)
x00, x11, x01 = x00[ind00], x11[ind11], x01[ind01]

def my_cdf(yl1, y2l1, step): 
    tm = max( max(yl1), max(y2l1) )
    F1,F2 = [], []
    for t in np.arange(0, tm+0.1, step):
        F1.append( yl1[(yl1>0)&(yl1<t)].shape[0] )
        F2.append( y2l1[(y2l1>0)&(y2l1<t)].shape[0] )
    F1, F2 = np.array(F1)/yl1[(yl1>0)].shape[0], np.array(F2)/y2l1[(y2l1>0)].shape[0]
    n1, n2 = yl1[yl1>0].shape[0], y2l1[y2l1>0].shape[0]
    K = max(abs(F1-F2))*np.sqrt( n1*n2/(n1+n2) )
    return F1, F2, K, tm
step = 0.01
F01, F11, K, tm = my_cdf( x01, x11, step )
print(K)