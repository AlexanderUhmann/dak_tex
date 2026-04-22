rfc = RandomForestClassifier(criterion='entropy', 
                             max_depth=30, 
                             min_samples_leaf=10,
                             min_samples_split=10,
                             max_features='log2',
                             n_estimators=40, 
                             random_state=42)
rfc.fit(X_train, Y_train)
rfc.score(X_train, Y_train), rfc.score(X_test, Y_test)
y_pred_train = rfc.predict(X_train)
y_pred_test = rfc.predict(X_test)
print(classification_report(Y_train, y_pred_train))
print(classification_report(Y_test,  y_pred_test))