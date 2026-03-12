from sklearn.ensemble import GradientBoostingClassifier

X_train, X_test, Y_train, Y_test = train_test_split(X_pay, y_, test_size=0.25, random_state=0)
boost_gr = GradientBoostingClassifier()
boost_gr.fit(X_train, Y_train)

y_pred_train = boost_gr.predict(X_train)
y_proba_train = boost_gr.predict_proba(X_train)
y_pred_test = boost_gr.predict(X_test)
y_proba_test = boost_gr.predict_proba(X_test)

y_pred_test = boost_gr.predict(X_test)
print(classification_report(Y_train, y_pred_train))
print(classification_report(Y_test,  y_pred_test))