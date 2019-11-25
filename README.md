# Reddit Machinelearning

This is a crude implementation of a recurrent neural network to generate comments, based on training data obtained from comments using the pushshift api (Real user's Reddit comments).

I thought it would be amusing to train the network to become a politcial commentator based on explosive reddit comments from /r/The_Donald. This has proven to be a hilarious and slightly depressing exercise, nevertheless very educational!


## Components
`data_pull.py` is a script I wrote to pull down some data to play with. We are using the pushshift api which allows us to query large amounts of reddit content, which gets served to us as json. We then parse the json to obtain the body of the comments & save them locally to a text file. - Line 30 and 34 contain sample queries to the pushshift api which will give us a bunch of reddit comments.

`rnn.py` implements a recurrent neural network using keras, with tensorflow as the backend. It was mostly written using information from blog posts and keras/tensorflow documentation. Due to my limited understanding of machine learning I leaned heavily on the documenation here and there was one particular blog post from which I borrowed most of the implementation. 
https://chunml.github.io/ChunML.github.io/project/Creating-Text-Generator-Using-Recurrent-Neural-Network/

Firstly, the script takes in the data, builds a featureset of characters used in the data and indexes all of the characters used with numbers. My understaing as to why this is done is beacuase machine learning models are easier to train with numbers. The data is later converted back to text from the output layer. The Data is then split into sequences to allow the model to predict the next character after any given character.

The script then builds an LSTM model using keras and then trains it with the datasets inputted. It then prints examples as it goes and saves the weights of the RNN every 10 epochs.

Using the aforementioned blog post and various other resources, I was able to build a machine learning model with multiple layers, train it with the reddit comment data and output some sample predicted comments.

I've been running this script on an AWS EC2 instance optimized for GPU machine learning.


## Educational and other resources used

https://keras.io/examples/lstm_text_generation/

https://github.com/pushshift/api

https://chunml.github.io/ChunML.github.io/project/Creating-Text-Generator-Using-Recurrent-Neural-Network/

https://www.tensorflow.org/tutorials/text/text_generation

https://aws.amazon.com/ (g4dn.4xlarge instance running Amazon Linux for GPU learning)

