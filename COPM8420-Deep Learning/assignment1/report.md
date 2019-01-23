#### benefit of this technique
1. don't need to retrain

#### Introdction the data set

This data set is from a total of 43 people, 30 contributed to the training set and different 13 to the test set. There are 3823 instance in train set and 1797 instance in test set. For each image, it is a 32x32 bitmap, which is divided into nonoverlapping 4x4 blocks. Therefore, The number of features will be 64 and each element is an integer in the range 0 to 16. The output class is an integer in the range 0 to 9.

#### Valid reasons for choosing the data set
1. Handwritten Recognition is a classic problem for ML.
2. NRT just somehow improve overfitting problem. For this paper, obviously we cannot significantly improve neural network through pruning redundant hidden units. Instead of, we try to figure out the minimum neural network for certain problem, which should not reduce performance. Therefore, we should choose a dataset which can easily get a good model using simple NN with .

### Model design
#### Neural network structure
In this paper, I use PyTorch to build a simple feed-forward two-layer network. the number of input feature is 64 and the number of output class is 10. Hidden layer size will be a hyper-parameter. There are some details,
1. I use tanh() for activation function instead of sigmoid() from the original paper. Since the range of tanh() output is from -1 to 1, we don't need to normalize the result to 0.5. According Deep Learning Specialization [3], tanh() is always better than sigmoid().
2. Besides, I use Adam method [4] for optimization, since it would converge fastly.
3. CrossEntropyLoss() for cost function.
4. a new funtion hidden_layer() for getting the result of hidden layer units.

#### Performance of the neural network


#### Remove method

1. For each unit, I build a vector , which contains this unit's output for all train example.
2. I calculate the angle of any two units just like the original paper. Notice that if a unit is removed, we don't use this unit in later angle calculation.
3. If the angle is smaller than 15, we remove one of the unit and add it's weight which is from hidden layer to output layer to another one. For simpleness, I just change those redundant units' weight to 0 instead of truely remove them from the whole neural network. Since we think those two units have similar structure or behaviour from input layer to hidden layer, we don't need to deal with weight from input layer to hidden layer, otherwise we should focus on weight from hidden layer to output weight.
4. If the angle is larger than 175, instead of remove both of units as the original paper, I choose to remove one of the unit and minus it's weight weight which is from hidden layer to output layer to another one.

If
Good level of problem complexity
Clear and valid investigation aims
Model design that clearly serves the purpose of the investigations
Appropriate measures used to determine the performance of the neural network and
predictions
Good explanation of the model design
Appropriate choice for the inputs and outputs of the prediction model with valid reasons
Evidence of good understanding of the relevant literature
### Results and Discussion
original hidden units: 100
Number of epochs: 1000

removed units: 8
accuracy: 96.38 -> 96.44

We can use this method to prune some units and get a smaller neural network without retraining. However, the number of units removed is not satisfying and it's far from the minimum neural network for this certain problem.

Practical problems
1. distribution of input
2. also use test set to remove redundant units.
3. hidden layer behaviour is 比我们想象的复杂且不可预测。

Good methods used to evaluate the model including an appropriate split of the train, test /
validation data
Good level of detail used to analyse results
Conclusion and Future Work ( /2)
Appropriate conclusion of the work
Appropriate work suggested to extend and/or improve the work
