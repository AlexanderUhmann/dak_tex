X_train, X_test, Y_train, Y_test = train_test_split( df, y_, test_size=0.25, random_state=0)
epochs = 20 
model = keras.Sequential()            
model.add(keras.Input(shape=(19,)))  
model.add(Dense(32, activation='relu'))   
model.add(keras.layers.Dense(1, activation='sigmoid')) 
opt = keras.optimizers.Adam(learning_rate=0.005)
metrics = keras.metrics.BinaryAccuracy(name="accuracy", dtype=None, threshold=0.5)
model.compile(optimizer=opt, loss='mse', metrics=metrics)
fit_history = model.fit(X_train, Y_train, 
                        batch_size = 128, 
                        validation_data = (X_test, Y_test),
                        epochs = epochs)