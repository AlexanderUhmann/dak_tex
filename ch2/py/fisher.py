def transform_f(r, R, n):    
    if n > 3:
        return 0.5*np.log(((1+r)/(1-r))*((1-R)/(1+R)))*np.sqrt(n-3)
    else:
        return 0

mth = 17
n_all, n_nod, n_def, n_ano = X_pay.shape[0], len(ind_nod), len(ind_def), len(ind_ano) 
R_all, r_nod, r_def, r_ano = all_c[mth], nod_c[mth], def_c[mth], ano_c[mth]
transform_f(r_nod, R_all, n_nod), transform_f(r_def, R_all, n_def ), transform_f(r_ano, R_all, n_ano )