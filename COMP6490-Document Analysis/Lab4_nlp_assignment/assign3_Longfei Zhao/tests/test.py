# coding: utf-8

#!/usr/bin/python

# https://docs.python.org/2/library/unittest.html

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import os
import tensorflow as tf
curr_path = os.path.abspath(__file__)
root_path = os.path.abspath(os.path.join(
    os.path.join(curr_path, os.pardir), os.pardir))
sys.path.append(str(root_path))

from models.FastText import FastText
from DataAPI import *

import unittest
import math


class TestDataAPI(unittest.TestCase):
    """Tests for Data API """

    def test_next(self):
        """ next should raise exception at the end of the input sequence"""
        data_iter = DataIter(np.arange(3))
        data_iter.next()
        data_iter.next()
        data_iter.next()
        with self.assertRaises(StopIteration):
            data_iter.next()

    def test_iter_data(self):
        """ test equivalence of iterator """
        data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        data_iter = DataIter(data)
        pre_array = []
        for indices in data_iter:
            pre_array.append(data[indices])
        self.assertTrue(np.array_equal(np.array(pre_array), data))


class TestModel(unittest.TestCase):
    """Tests for the computation graph based on layer outputs. Please add more tests for your model when necessary."""

    def test_accuracy(self):
        """ Evaluate the computation of accuracy without building the whole graph."""
        num_classes = 3
        model = FastText(num_classes, 5, 10, 0.1)
        y = tf.placeholder(tf.float32, shape=[num_classes, 1])
        model.predict(y)
        model.declare_placeholders()
        model.compute_accuracy()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            true_label = np.zeros(shape=(num_classes, 1), dtype=np.int)
            true_label[1] = 1
            example_y = np.array([[0.3], [0.5], [0.6]], dtype=np.float)
            rs = sess.run(model.accuracy, feed_dict={
                          y: example_y, model.correct_label: true_label})
            self.assertEqual(rs[0], 0)
            rs = sess.run(model.accuracy, feed_dict={y: np.array(
                [[0.3], [0.8], [0.6]], dtype=np.float), model.correct_label: true_label})
            self.assertEqual(rs[0], 1)

    # Implement tests for other parts of the computation graphs whenever possible.
    def test_accuracy2(self):
        """ Evaluate the computation of accuracy without building the whole graph."""
        num_classes = 3
        model = FastText(num_classes, 5, 10, 0.1)
        y = tf.placeholder(tf.float32, shape=[num_classes, 1])
        model.predict(y)
        model.declare_placeholders()
        model.compute_accuracy()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            true_label = np.zeros(shape=(num_classes, 1), dtype=np.int)
            true_label[2] = 1
            example_y = np.array([[0.3], [0.5], [0.6]], dtype=np.float)
            rs = sess.run(model.accuracy, feed_dict={
                          y: example_y, model.correct_label: true_label})
            self.assertEqual(rs[0], 1)
            rs = sess.run(model.accuracy, feed_dict={y: np.array(
                [[0.3], [0.8], [0.6]], dtype=np.float), model.correct_label: true_label})
            self.assertEqual(rs[0], 0)


if __name__ == '__main__':
    unittest.main()
