# WEEK 1 

## Representational Learning using Autoencoders.

### Question 1
Use the Fashion MNIST data set and train a basic autoencoder to reconstruct images.
Train the model using x_train as both the input and the target. The encoder should
learn to compress the dataset from 784 dimensions to the latent space, and the 
decoder should learn to reconstruct the original images.
Let the autoencoder have two Dense layers: 
1. an encoder, which compresses the images into a 64 dimensional latent 
vector, use reLU as activation function.
2. and a decoder, that reconstructs the original image from the latent space, 

use sigmoid as activation function.
Once the model is trained for at least 10 epochs , with loss function as mean square 
error, test it by encoding and decoding images from the test set. Display original and 
reconstructed images.


### Question 2
Train an autoencoder to detect anomalies using the ECG5000 dataset. 
Plot and observe a normal ECG vs an anomalous ECG.
Design and Train an autoencoder on the normal rhythms only, then use it to 
reconstruct all the data.
The autoencoder is trained using only the normal ECGs, but is evaluated using the full 
test set. Classify an ECG as anomalous if the reconstruction error is greater than one 
standard deviation from the normal training examples