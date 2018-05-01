#!/usr/bin/python
# coding: utf-8

# Created by:   Leticia Portella Nascimento
# Created on:   25/11/2014
# Updated on:   --
# Project:      programinha maroto
# Main Script:  prealpha_15


import numpy as np
from scipy.optimize import curve_fit
import scipy
import csv
import os

import sys

pathpath = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
os.chdir(pathpath)

def FitFunc(x, a, b):
	return a*(x**b)

#parinput = parametro de input ( xLOA, xBEAM...)

def MyRegressionCurve(navio,entrada,parinput,value):
    if navio == 'Bulk Carrier':
    	name = 'bulk_data'
    elif navio =='Containership':
    	name = 'cont_data'
    elif navio == 'General Cargo':
    	name = 'general_data'

    if entrada == 'ROM':
        method = 'ROM'
    elif entrada == 'P50':
    	method ='P50'
    elif entrada == 'P75':
    	method = 'P75'

    a = {}
    if parinput == 'DWT':
    	inn = ['LOA','Lpp','Beam','Depth','Draft','Displ','WLatLoad','WLatBal','WTrvLoad','WTrvBal']
    	a['DWT'] = value
    elif parinput=='TEU':
        inn = ['LOA','Lpp','Beam','Depth','Draft','Displ','WLatLoad','WLatBal','WTrvLoad','WTrvBal']
    	a['DWT'] = value
    	parinput = 'DWT'
    elif parinput == 'LOA':
    	inn = ['DWT','Lpp','Beam','Depth','Draft','Displ','WLatLoad','WLatBal','WTrvLoad','WTrvBal']
    	a['LOA'] = value
    elif parinput == 'Lpp':
    	inn = ['DWT','LOA','Beam','Depth','Draft','Displ','WLatLoad','WLatBal','WTrvLoad','WTrvBal']
    	a['Lpp'] = value
    elif parinput == 'Beam':
    	inn = ['DWT','LOA','Lpp','Depth','Draft','Displ','WLatLoad','WLatBal','WTrvLoad','WTrvBal']
    	a['Beam'] = value
    elif parinput == 'Depth':
    	inn = ['DWT','LOA','Lpp','Beam','Draft','Displ','WLatLoad','WLatBal','WTrvLoad','WTrvBal']
    	a['Depth'] = value
    elif parinput == 'Draft':
    	inn = ['DWT','LOA','Lpp','Beam','Depth','Displ','WLatLoad','WLatBal','WTrvLoad','WTrvBal']
    	a['Draft'] = value
    elif parinput == 'Displ':
    	inn = ['DWT','LOA','Lpp','Beam','Depth','Draft','WLatLoad','WLatBal','WTrvLoad','WTrvBal']
    	a['Displ'] = value

    try:
        arq = open(eval('\'' + name + '_' + entrada + '.csv\''), 'rb')
    except IOError:
        return 'error'
           
    DWT =[]
    LOA = []
    Lpp = []
    Beam = []
    Depth = []
    Draft = []
    Displ = []
    WLatLoad = []
    WLatBal=[]
    WTrvLoad = []
    WTrvBal=[]


    mycsv = list(csv.reader(arq, delimiter=';'))
 

    for i in mycsv[1:]:
        DWT.append(float(i[0]))
        LOA.append(float(i[1]))
        Lpp.append(float(i[2]))
        Beam.append(float(i[3]))
        Depth.append(float(i[4]))
        Draft.append(float(i[5]))
        Displ.append(float(i[6]))
        WLatLoad.append(float(i[7]))
        WLatBal.append(float(i[8]))
        WTrvLoad.append(float(i[9]))
        WTrvBal.append(float(i[10]))

    p0 = [8,0.5]
    for y in inn:
        wii = scipy.array(eval(y))
        woo = scipy.array(eval(parinput))
        fitParams,fitCovar = curve_fit(FitFunc,woo,wii,p0=None)
        value = float(value)
        #result = fitParams[0]*value**fitParams[1]
        result = fitParams[0]*np.power(value,fitParams[1])
        a[y] = str(round(result,2))
    return a



