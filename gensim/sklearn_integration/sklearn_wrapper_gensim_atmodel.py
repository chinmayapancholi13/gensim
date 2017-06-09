#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 Radim Rehurek <radimrehurek@seznam.cz>
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl.html
#
"""
Scikit learn interface for gensim for easy use of gensim with scikit-learn
Follows scikit-learn API conventions
"""
import numpy as np

from gensim import models
from gensim.sklearn_integration import base_sklearn_wrapper
from sklearn.base import TransformerMixin, BaseEstimator


class SklearnWrapperATModel(models.AuthorTopicModel, base_sklearn_wrapper.BaseSklearnWrapper, TransformerMixin, BaseEstimator):
    """
    Base AuthorTopic module
    """

    def __init__(self, num_topics=100, id2word=None, author2doc=None, doc2author=None,
            chunksize=2000, passes=1, iterations=50, decay=0.5, offset=1.0,
            alpha='symmetric', eta='symmetric', update_every=1, eval_every=10,
            gamma_threshold=0.001, serialized=False, serialization_path=None,
            minimum_probability=0.01, random_state=None):
        """
        Sklearn wrapper for AuthorTopic model. Class derived from gensim.models.AuthorTopicModel
        """
        self.corpus = None
        self.num_topics = num_topics
        self.id2word = id2word
        self.author2doc = author2doc
        self.doc2author = doc2author
        self.chunksize = chunksize
        self.passes = passes
        self.iterations = iterations
        self.decay = decay
        self.offset = offset
        self.alpha = alpha
        self.eta = eta
        self.update_every = update_every
        self.eval_every = eval_every
        self.gamma_threshold = gamma_threshold
        self.serialized = serialized
        self.serialization_path = serialization_path
        self.minimum_probability = minimum_probability
        self.random_state = random_state

    def get_params(self, deep=True):
        """
        Returns all parameters as dictionary.
        """
        return {"corpus": self.corpus, "num_topics": self.num_topics, "id2word": self.id2word,
                "author2doc": self.author2doc, "doc2author": self.doc2author, "chunksize": self.chunksize,
                "passes": self.passes, "iterations": self.iterations, "decay": self.decay,
                "offset": self.offset, "alpha": self.alpha, "eta": self.eta, "update_every": self.update_every,
                "eval_every": self.eval_every, "gamma_threshold": self.gamma_threshold,
                "serialized": self.serialized, "serialization_path": self.serialization_path,
                "minimum_probability": self.minimum_probability, "random_state": self.random_state}

    def set_params(self, **parameters):
        """
        Set all parameters.
        """
        super(SklearnWrapperATModel, self).set_params(**parameters)

    def fit(self, X, y=None):
        """
        Fit the model according to the given training data.
        """
        pass

    def transform(self, docs):
        """
        """
        pass

    def partial_fit(self, X):
        """
        Train model over X.
        """
        pass
