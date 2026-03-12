all_c, nod_c, def_c, ano_c = [], [], [], []
month = []
for i in range(1, X_pay.shape[1]):
    all_c.append(np.corrcoef(np.array(X_pay).T[i-1], np.array(X_pay).T[i])[0,1])
    ind_nod = np.where(y_==0)[0]
    nod_c.append(np.corrcoef(np.array(X_pay).T[i-1][ind_nod], np.array(X_pay).T[i][ind_nod])[0,1])
    ind_def = np.where(y==1)[0]
    def_c.append( np.corrcoef(np.array(X_pay).T[i-1][ind_def], np.array(X_pay).T[i][ind_def])[0,1])
    ind_ano = ind_anom
    ano_c.append( np.corrcoef(np.array(X_pay).T[i-1][ind_ano], np.array(X_pay).T[i][ind_ano])[0,1])
    month.append(i)

mth = 0
n_all, n_nod, n_def, n_ano = X_pay.shape[0], len(ind_nod), len(ind_def), len(ind_ano) 
R_all, r_nod, r_def, r_ano = all_c[mth], nod_c[mth], def_c[mth], ano_c[mth]
transform_f(r_nod, R_all, n_nod), transform_f(r_def, R_all, n_def), transform_f(r_ano, R_all, n_ano)