import keras
import pandas as pd
import numpy as np
from keras.utils import plot_model
from keras.models import Model 
from keras.layers import Input, Dense
# from keras import Input

def main():
  """
  When input data is one-dimensional, such as for a Multilayer Perceptron, the shape must explicitly leave room for the shape of the minibatch size used when splitting the data when training the network.
  """
  visible = Input(shape=(10,))
  # Connecting to the output of visible to the input of hidden
  hidden1 = Dense(10, activation='relu')(visible)
  hidden2 = Dense(20, activation='relu')(hidden1)
  hidden3 = Dense(10, activation='relu')(hidden2)
  output = Dense(1, activation='sigmoid')(hidden3)

  model = Model(inputs=visible, outputs=output)
  model.summary()

  plot_model(model, to_file='../resources/multilayer_perceptron_graph.png')
  # pass

main()