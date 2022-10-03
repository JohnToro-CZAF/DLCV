import keras
import pandas as pd
import numpy as np
from keras import Sequential, Activation

class Model(Sequential):
  def __init__(self):
    super().__init__()
    self.layer1 = Dense(5, input_dim=2)
    self.activation1 = Activation('relu')
    self.layer2 = Dense(1)
    self.activation2 = Activation('sigmoid')
    self.add([self.layer1, self.activation1, self.layer2, self.activation2])
    # pass
  

def main():
  model = Sequential()
  model.add(Dense(5, input_dim=2))
  model.add(Activation('relu'))
  model.add(Dense(1))
  model.add(Activation('sigmoid'))
  # model.compile(optimizer='sgd', loss='mean_squared_error')
  algorithm = SGD(lr=0.1, momentum=0.3)
  model.compile(optimizer=algorithm, loss='mean_squared_error', metrics=['accuracy'])
  history = model.fit(X, y, batch_size=10, epochs=100)

  # pass

if __main__ == '__main__':
  main()