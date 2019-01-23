1. Installation of Tensorflow.
	 
   1.1 Install on your laptops.

    Tensorflow provides details installation guide on https://www.tensorflow.org/install/. Follow the one most suitable for your computer.

   1.2 Instructions for lab computers.

       Both tensorflow and NLTK are installed on lab machines.
       

2. Installation of NLTK
If you have never used NLTK, please follow the instructions in Section 3.1 of http://www.nltk.org/book/ch03.html to work on the example with Electronic books. If you have not installed NLTK before, you may need to install the tokenizer for news:
	import nltk
	nltk.download('punkt')


3. Starter code

The starter code contains a warm-up exercise (Warm-up Exercise.ipynb) for both tensorflow and NLTK. It is recommended if you are not familiar with them.

The fasttext model is partially implemented. Implement the methods which are left blank. It is encouraged to write tests before implementation. Taking the test of computing accuracy as an example, at least one test should be written for evaluating your computation graph.

Although mini-batch training will reduce variance of SGD, it is NOT required for this assignment. It is sufficient to train the model by updating model parameters right after computing gradient for a single sentence.

After implementing all methods, in your project folder, run the whole program with Main.py.

python Main.py -d data

Run the unit tests:

python tests/test.py



4. Coding style

It is recommended to follow the best practices of Tensorflow right from the beginning. Although you will not loose points if you do not follow the best practices, they may help you get a better job and reduce the amount of time for debugging. Here are some links of introducing the best practices of Tensorflow.

   * Best practice series : https://blog.metaflow.fr/tensorflow-a-proposal-of-good-practices-for-files-folders-and-models-architecture-f23171501ae3
   * Documentation: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
   * Example code: https://github.com/tensorflow/models/blob/master/tutorials/image/cifar10/cifar10.py


5. Data
There are 6 data files for the purpose of training, validation, and testing. Each row in sentences_<XXX>.txt contains an instance (a news title), whose label(category) is in the corresponding row in labels_<XXX>.txt.
 
sentences_train.txt : sentences for training, one row per instance.
labels_train.txt : classification labels for training, one row per instance.
sentences_dev.txt : sentences for development (validation) set, one row per instance.
labels_dev.txt : classification labels for development (validation) set, one row per instance.
sentences_test.txt : sentences for testing, one row per instance.
labels_test.txt : classification labels for testing, one row per instance. 
