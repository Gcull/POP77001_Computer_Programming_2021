# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:35:12 2021

@author: gcull
"""

options(jupyter.rich_display = FALSE)

l <- list(
    mapply(assign, letters, 1:26),
    A = array(1:60, c(5,2,3)),
    M = matrix(1:50, c(10,5))
)

l