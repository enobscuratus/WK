#!/usr/bin/python
# -*- coding: utf-8 -*-


import MySQLdb as mdb
from user_input_mod import *

def connectdb()

  con = mdb.connect(get_mysqlhost(), get_mysqlusr(), get_mysqlpw(), get_mysqldb())
