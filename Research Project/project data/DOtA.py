# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:25:48 2018

@author: manor
"""
import dota2
api_key = '9B53B2492EAF3E55B5E39475921D0945'
dota = dota2.Dota2(api_key)
test = dota.find_match_history(matches_requested = 1000)