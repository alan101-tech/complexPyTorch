#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Mar 20 19:35:11 2019

@author: spopoff
"""


from torch.nn.functional import relu, max_pool2d, dropout, dropout2d





def complex_relu(input_r,input_i):
#    assert(input_r.size() == input_i.size())
    return relu(input_r), relu(input_i)

def complex_max_pool2d(input_r,input_i,kernel_size, stride=None, padding=0,
                                dilation=1, ceil_mode=False, return_indices=False):

    return max_pool2d(input_r, kernel_size, stride, padding, dilation, 
                      ceil_mode, return_indices), \
           max_pool2d(input_i, kernel_size, stride, padding, dilation, 
                      ceil_mode, return_indices)

def complex_dropout(input_r,input_i, p=0.5, training=True, inplace=False):
    return complex_dropout(input_r, p, training, inplace), \
           complex_dropout(input_r, p, training, inplace)


def complex_dropout2d(input_r,input_i, p=0.5, training=True, inplace=False):
    return complex_dropout2d(input_r, p, training, inplace), \
           complex_dropout2d(input_r, p, training, inplace)
