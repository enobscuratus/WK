#!/usr/bin/python
# -*- coding: utf-8 -*-


import MySQLdb as mdb
from user_input_mod import *

def connectdb():

  db_host = get_mysqlhost()
  db_user = get_mysqlusr()
  db_pass = get_mysqlpw()
  db_name = get_mysqldb()
  con = mdb.connect(db_host, db_user, db_pass, db_name)
