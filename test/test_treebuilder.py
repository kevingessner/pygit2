#!/usr/bin/env python
#
# Copyright 2010 Google, Inc.
#
# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2,
# as published by the Free Software Foundation.
#
# In addition to the permissions in the GNU General Public License,
# the authors give you unlimited permission to link the compiled
# version of this file into combinations with other programs,
# and to distribute those combinations without any restriction
# coming from the use of this file.  (The General Public License
# restrictions do apply in other respects; for example, they cover
# modification of the file, and distribution when not linked into
# a combined executable.)
#
# This file is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.  If not, write to
# the Free Software Foundation, 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301, USA.

"""Tests for TreeBuilder objects."""

__author__ = 'dborowitz@google.com (Dave Borowitz), kevin@fogcreek.com (Kevin Gessner)'

import operator
import unittest

import pygit2
import utils

TREE_SHA = '967fce8df97cc71722d3c2a5930ef3e6f1d27b12'

class TreeBuilderTest(utils.BareRepoTestCase):

    def assertTreeEntryEqual(self, entry, sha, name, attributes):
        self.assertEqual(entry.sha, sha)
        self.assertEqual(entry.name, name)
        self.assertEqual(entry.attributes, attributes,
                         '0%o != 0%o' % (entry.attributes, attributes))

    def test_empty_treebuilder(self):
        pass

    def test_treebuilder_from_tree(self):
        tree = self.repo[TREE_SHA]
        builder = pygit2.TreeBuilder(tree)
        self.assertTrue(tree['a'])
        self.assertTrue(builder['a'])
        self.assertTreeEntryEqual(tree['a'], builder['a'])

if __name__ == '__main__':
  unittest.main()
