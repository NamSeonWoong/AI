import keras
import numpy

x= numpy.array([0,1,2,3,4])
y= x*2+1

model = keras.models.Sequential()
model.add(keras.layers.Dense(1,input_shape=(1,)))
model.compile('SGD','mse')

model.fit(x[:],y[:], epochs=10000,verbose=0)

print('Targets:',y[:])
print('Predictions:',model.predict(x[:].flatten()))