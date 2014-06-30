#!/usr/bin/python
# -*- coding: utf-8 -*-


import MySQLdb as mdb
from user_input_mod import *

class mysql(object):

  def connectdb(): #establish connection to mysql

    db_host = get_mysqlhost()
    db_user = get_mysqlusr()
    db_pass = get_mysqlpw()
    db_name = get_mysqldb()
    con = mdb.connect(db_host, db_user, db_pass, db_name)

  def insertframe(): #insert panda dataframe into mysql
  
  def removeframe(): #remove matched dataframe from mysql, accepting type frame
  
  def createtable(): #create table in MYSQL for insertion
  
  def removetable(): #remove table in MYSQL
  
  #TODO: ADD MORE MANIPULATORS
