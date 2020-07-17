#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os


Home = os.path.expanduser('~')
carpetas = os.listdir(Home)
for RutaABS, Directorio, Archivo in os.walk(Home):
    try:
        print(RutaABS,Directorio,Archivo)
    except Except as e:
        print(str(e))