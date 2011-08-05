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
BLOB_SHA = 'af431f20fc541ed6d5afede3e2dc7160f6f01f16'
ALT_BLOB_SHA = '85f120ee4dac60d0719fd51731e4199aa5a37df6'

class TreeBuilderTest(utils.BareRepoTestCase):

    def assertTreeEntryEqual(self, entry, sha, name, attributes):
        self.assertEqual(entry.sha, sha)
        self.assertEqual(entry.name, name)
        self.assertEqual(entry.attributes, attributes,
                         '0%o != 0%o' % (entry.attributes, attributes))

    def test_empty_treebuilder(self):
        builder = pygit2.TreeBuilder()
        self.assertTrue(builder)
        self.assertRaises(KeyError, lambda: builder['foo'])

    def test_treebuilder_from_tree(self):
        tree = self.repo[TREE_SHA]
        builder = pygit2.TreeBuilder(tree)
        self.assertTrue(tree['a'])
        ba = builder['a']    
        self.assertTrue(ba)
        self.assertTreeEntryEqual(tree['a'], ba.sha, ba.name, ba.attributes)

    def test_treebuilder_insert(self):
        # insert can both insert and update
        builder = pygit2.TreeBuilder()
        builder.insert("foo", BLOB_SHA, 0775)
        ba = builder['foo']    
        self.assertTrue(ba)
        self.assertEqual(ba.attributes, 0775)

        builder.insert("foo", BLOB_SHA, 0664)
        ba = builder['foo']    
        self.assertTrue(ba)
        self.assertEqual(ba.attributes, 0664)

        builder.insert("bar", BLOB_SHA, 0664)
        ba = builder['bar']    
        self.assertTrue(ba)
        self.assertTreeEntryEqual(ba, BLOB_SHA, 'bar', 0664)

        builder.insert("bar", ALT_BLOB_SHA, 0664)
        ba = builder['bar']    
        self.assertTrue(ba)
        self.assertTreeEntryEqual(ba, ALT_BLOB_SHA, 'bar', 0664)

if __name__ == '__main__':
  unittest.main()
