from keras.utils import plot_model
from keras.models import Model
from keras.layers import Input, Dense, Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D

def main():
  visible = Input(shape=(64, 64, 1))
  conv1 = Conv2D(32, (4,4), activation='relu')(visible)
  pool1 = MaxPooling2D()(conv1)
  conv2 = Conv2D(16, (4,4), activation='relu')(pool1)
  pool2 = MaxPooling2D()(conv2)
  flat1 = Flatten()(pool2)
  hidden1 = Dense(10, activation='relu')(flat1)
  output = Dense(1, activation='sigmoid')(hidden1)

  model = Model(inputs=visible, outputs=output)

  model.summary()
  plot_model(model, to_file='../resources/convolutional_neural_network.png')
  pass  

main()
