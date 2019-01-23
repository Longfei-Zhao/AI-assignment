
# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np


class FastText(object):
    """ Implementation of the fasttext model. """

    def __init__(self, num_classes, embedding_dim, size_vocab, learning_rate):
        """Init the model with default parameters/hyperparameters."""
        self.num_classes = num_classes
        self.embedding_dim = embedding_dim
        self.size_vocab = size_vocab
        self.learning_rate = learning_rate

    def build_graph(self):
        """build the whole computation graph."""
        self.declare_placeholders()
        self.declare_variables()
        logit = self.inference()
        self.optimize(logit)
        self.predict(logit)
        self.compute_accuracy()

    def declare_placeholders(self):
        """ Declare the place holders here. Use tf.name_scope when possible."""
        # TODO
        with tf.name_scope('fast_text'):
            self.input_sens = tf.placeholder(
                tf.int32, shape=[None], name='input_sens')
            self.correct_label = tf.placeholder(
                tf.float32, shape=[self.num_classes, 1], name='correct_label')

    def declare_variables(self):
        """ Declare the variables here. Use tf.name_scope when possible."""
        # TODO
        with tf.name_scope('fast_text'):
            self.W = tf.Variable(
                tf.random_uniform([self.embedding_dim, self.num_classes]), name='W')
            self.b = tf.Variable(tf.random_uniform([self.num_classes, 1]), name='b')
            self.embeddings = tf.Variable(tf.random_uniform(
                [self.size_vocab, self.embedding_dim], -1.0, 1.0), name='embed')

    def inference(self):
        """Compute the logit"""
        # TODO: pass
        embed_seq = tf.nn.embedding_lookup(self.embeddings, self.input_sens)
        embed_mean = tf.reduce_mean(embed_seq, 0)
        mean_rep = tf.reshape(embed_mean, [1, self.embedding_dim])
        h = tf.matmul(mean_rep, self.W)
        h = tf.reshape(h, [self.num_classes, 1])
        y = tf.nn.softmax(h + self.b, dim=0)
        return y

    def optimize(self, logit):
        """Compute the logit. logit = W * h + b,
        where h is the mean of the word embedding in a sentence.
           Optionally you can also compute softmax(logit) here.
        """
        # TODO: pass
        cross_entropy = self.loss(logit)
        optimizer = tf.train.GradientDescentOptimizer(
            self.learning_rate)
        self.train_step = optimizer.minimize(cross_entropy, name='train_step')

    def compute_accuracy(self):
        """Evaluate the accuracy of the model against a test/validation set"""
        correct_prediction = tf.equal(
            self.prediction, tf.argmax(self.correct_label, 0))
        self.accuracy = tf.cast(
            correct_prediction, tf.float32, name='accuracy')

    def predict(self, logit):
        """ Predict label based on logit """
        self.prediction = tf.argmax(logit, 0)

    def loss(self, y):
        """Compute the cross entropy, given the logit."""
        cross_entropy = tf.reduce_mean(-tf.reduce_sum(self.correct_label * tf.log(y), reduction_indices=0))
        return cross_entropy
