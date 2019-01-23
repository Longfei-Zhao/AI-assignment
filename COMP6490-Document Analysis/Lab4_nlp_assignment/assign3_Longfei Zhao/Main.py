
# coding: utf-8

# !/usr/bin/python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

import sys
import getopt
import collections
import math
import os
import random
from nltk import word_tokenize
from random import shuffle

from models.FastText import FastText
from DataAPI import *

curr_path = os.path.abspath(__file__)
root_path = os.path.abspath(os.path.join(curr_path, os.pardir))
sys.path.append(str(root_path))

# It is encouraged to rewrite the hyperparameters as flags,
# and change main() accordingly.
# https://www.tensorflow.org/api_docs/python/tf/flags
learning_rate = 0.05
num_epochs = 3
embedding_dim = 10


def save_model_for_tensor_board():
    """It is a good practice to check you model with tensorboard"""


def eval(word_to_id, train_dataset, dev_dataset, test_dataset):
    """
    Train a fasttext model, evaluate it on the validation set after each epoch.
    After training, evaluate the final model on the test set.

    Args:
        word_to_id (dictionary) : word to id mapping
        train_dataset (Dataset) : labeled dataset for training
        dev_dataset (Dataset) : labeled dataset for validation
        test_dataset (Dataset) : labeled dataset for test

    """
    fast_text = FastText(num_classes, embedding_dim,
                         len(word_to_id), learning_rate)
    fast_text.build_graph()
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        for epoch in range(num_epochs):
            dataIterator = DataIter(train_dataset.sentences)
            dataIterator.shuffle()
            for index in dataIterator:
                fast_text.train_step.run(feed_dict={
                                         fast_text.input_sens: train_dataset.sentences[index], fast_text.correct_label: train_dataset.labels[index]})
            print('Epoch %d : validation accuracy = %s .' %
                  (epoch, compute_accuracy(fast_text, dev_dataset)))

        print('Accuracy on the test set : %s.' %
              compute_accuracy(fast_text, test_dataset))
        return predict(fast_text, test_dataset)


def compute_accuracy_for_minibatch(fast_text, eval_dataset):
    """
    Compuate accuracy on the eval_dataset in the batch mode.
    It is useful only for the bonus assignment.

    Args:
        fast_text (FastText) : an instance of fasttext model.
        eval_dataset (Dataset) : labeled dataset for evaluation.
    """
    eval_result = fast_text.accuracy.eval(feed_dict={
        fast_text.input_sens: eval_dataset.sentences,
        fast_text.correct_label: eval_dataset.labels})
    return eval_result


def compute_accuracy(fast_text, eval_dataset):
    """
    Compuate accuracy on the eval_dataset.
    It applies fasttext model to collect
    number of correctly predicted sentences,
    then average the number by the total
    number of sentences in the eval_dataset.

    Args:
        fast_text (FastText) : an instance of fasttext model.
        eval_dataset (Dataset) : labeled dataset for evaluation.
    """
    num_correct = 0
    for index in DataIter(eval_dataset.sentences):
        num_correct += fast_text.accuracy.eval(feed_dict={
                                               fast_text.input_sens: eval_dataset.sentences[index], fast_text.correct_label: eval_dataset.labels[index]})[0]
    print('#correct sentences is %s ' % num_correct)
    return num_correct / len(eval_dataset.sentences)


def predict(fast_text, test_dataset):
    """
    Predict labels for each sentence in the test_dataset.

    Args:
        fast_text (FastText) : an instance of fasttext model.
        test_dataset (Dataset) : labeled dataset to generate predictions.
    """
    test_results = []
    for index in DataIter(test_dataset.sentences):
        test_results.append(fast_text.prediction.eval(
            feed_dict={fast_text.input_sens: test_dataset.sentences[index]}))
    return test_results


def main(argv):
    trainSensFile = ''
    trainLabelFile = ''
    devSensFile = ''
    devLabelFile = ''
    testSensFile = ''
    testLabelFile = ''
    testResultFile = ''
    try:
        opts, args = getopt.getopt(argv, "hd:", ["dataFolder="])
    except getopt.GetoptError:
        print('fastText.py -d <dataFolder>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('fastText.py -d <dataFolder>')
            sys.exit()
        elif opt in ("-d", "--dataFolder"):
            trainSensFile = os.path.join(arg, 'sentences_train.txt')
            devSensFile = os.path.join(arg, 'sentences_dev.txt')
            testSensFile = os.path.join(arg, 'sentences_test.txt')
            trainLabelFile = os.path.join(arg, 'labels_train.txt')
            devLabelFile = os.path.join(arg, 'labels_dev.txt')
            testLabelFile = os.path.join(arg, 'labels_test.txt')
            testResultFile = os.path.join(os.path.join(
                root_path, 'tests'), 'test_results.txt')
        else:
            print("unknown option %s ." % opt)
    word_to_id = build_vocab(trainSensFile)
    train_dataset = read_labeled_dataset(
        trainSensFile, trainLabelFile, word_to_id)
    dev_dataset = read_labeled_dataset(devSensFile, devLabelFile, word_to_id)
    test_dataset = read_labeled_dataset(
        testSensFile, testLabelFile, word_to_id)
    test_results = eval(word_to_id, train_dataset, dev_dataset, test_dataset)
    write_results(test_results, testResultFile)


if __name__ == "__main__":
    main(sys.argv[1:])
