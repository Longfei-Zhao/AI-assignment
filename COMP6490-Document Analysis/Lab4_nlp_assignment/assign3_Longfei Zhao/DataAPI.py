# coding: utf-8

# !/usr/bin/python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import math
import os
import random

from collections import namedtuple
import numpy as np
from nltk import word_tokenize

label_to_id = {'World': 0, 'Entertainment': 1, 'Sports': 2}
num_classes = 3
unknown_word_id = 0

Dataset = namedtuple('Dataset', 'sentences labels')


# The methods in this module is made for illustration purpose.
# A more practical and scalable solution is described in
# https://www.tensorflow.org/versions/r1.3/programmers_guide/datasets.

def create_label_vec(label):
    """Create one hot representation for the given label.

    Args:
        label(str): class name
    """
    label_id = label_to_id[label.strip()]
    label_vec = np.zeros((num_classes, 1), dtype=np.int)
    label_vec[label_id] = 1
    return label_vec


def tokenize(sens):
    """Write the method documentation here.
    """
    return word_tokenize(sens)


def map_token_seq_to_word_id_seq(token_seq, word_to_id):
    """ Write your documents here.
    """
    return [map_word_to_id(word_to_id, word) for word in token_seq]


def map_word_to_id(word_to_id, word):
    """ Map words to its ids

    Args:
        word_to_id (dictionary) : map word to id
        word (str) : a word to look up
    """
    if word in word_to_id:
        return word_to_id[word]
    else:
        return unknown_word_id


def build_vocab(sens_file_name):
    """Write the method documentation here. """
    data = []
    with open(sens_file_name) as f:
        for line in f.readlines():
            tokens = tokenize(line)
            data.extend(tokens)
    print('size of token sequence is %s. ' % len(data))
    count = [['$UNK$', unknown_word_id]]
    sorted_counts = collections.Counter(data).most_common()
    count.extend(sorted_counts)
    word_to_id = dict()
    for word, _ in count:
        word_to_id[word] = len(word_to_id)
    print("Unknown word id is %s ." % word_to_id['$UNK$'])
    print('size of vocabulary is %s. ' % len(word_to_id))
    return word_to_id


def read_labeled_dataset(sens_file_name, label_file_name, word_to_id):
    """ Read a labeled dataset into an instance of Dataset

    Args:
        sens_file_name (str) : sentence file path
        label_file_name (str) : label file path
        word_to_id (dictionary) : map word to ids
    """
    with open(sens_file_name) as sens_file, open(label_file_name) as label_file:
        data = []
        data_labels = []
        for label in label_file:
            sens = sens_file.readline()
            word_id_seq = map_token_seq_to_word_id_seq(
                tokenize(sens), word_to_id)
            data.append(word_id_seq)
            data_labels.append(create_label_vec(label))
        print("read %d sentences from %s ." % (len(data), sens_file_name))
        labeled_set = Dataset(sentences=data, labels=data_labels)
        return labeled_set


def write_results(test_results, result_file):
    """Write test results into file.

       Args:
           test_results (list) : a list of predicted class indices
           result_file (str) : file path for the results.
    """
    with open(result_file, mode='w') as f:
        for r in test_results:
            f.write("%d\n" % r)


class DataIter:
    """ Use indices to iterate through a dataset. """

    def __init__(self, dataset, batch_size=1):
        self.dataset_size = len(dataset)
        self.shuffle_indices = np.arange(self.dataset_size)
        self.inst_num = 0
        self.batch_size = batch_size
        self.num_batches_per_epoch = int(
            (self.dataset_size - 1) / self.batch_size) + 1

    def __iter__(self):
        return self

    def next(self):
        """ return index of the next sentence. """

        if self.inst_num < self.dataset_size:
            i = self.shuffle_indices[self.inst_num]
            self.inst_num += 1
            return i
        else:
            raise StopIteration

    def next_batch(self):
        """ return indices for the next batch. Useful for minibatch learning.
            For mini-batch training, it is insufficient to just return indices
            of sentences.
            Padding needs to be applied to ensure that the input tensor for
            each batch is of
            the same size.
            Example of padding: https://www.tensorflow.org/tutorials/seq2seq
        """

        if self.inst_num < self.num_batches_per_epoch:
            start_index = self.inst_num * self.batch_size
            end_index = min((self.inst_num + 1) *
                            self.batch_size, self.dataset_size)
            self.inst_num += 1
            return self.shuffle_indices[start_index: end_index]
        else:
            raise StopIteration

    def shuffle(self):
        """ Shuffle the data indices for training"""

        self.shuffle_indices = np.random.permutation(self.shuffle_indices)
        self.inst_num = 0
