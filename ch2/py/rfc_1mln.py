from sklearn.ensemble import RandomForestClassifier

X_train, X_test, Y_train, Y_test = train_test_split(X_pay, y_, test_size=0.25, random_state=0)
rfc = RandomForestClassifier()
rfc.fit(X_train, Y_train)

y_pred_train = rfc.predict(X_train)
y_proba_train = rfc.predict_proba(X_train)

y_pred_test = rfc.predict(X_test)
print(classification_report(Y_train, y_pred_train))
print(classification_report(Y_test,  y_pred_test))