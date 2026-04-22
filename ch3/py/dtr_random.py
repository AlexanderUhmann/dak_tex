dtree = DecisionTreeClassifier(criterion='entropy', 
                               max_depth=25, 
                               max_features='log2',
                               min_samples_leaf=10, 
                               min_samples_split=10,
                               random_state=42)
dtree.fit(X_train, Y_train) 
dtree.score(X_train, Y_train), dtree.score(X_test, Y_test)
y_pred_train = dtree.predict(X_train)
y_pred_test = dtree.predict(X_test)
print(classification_report(Y_train, y_pred_train))
print(classification_report(Y_test,  y_pred_test))