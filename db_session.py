#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from db.db_setup import Base

engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()
