#!/usr/bin/python
# coding: utf-8

# Created by:   Leticia Portella Nascimento
# Created on:   14/02/2014
# Updated on:   --
# Project:      programinha maroto
# Main Script:  prealpha_15

import matplotlib.pyplot as plt
import csv
import sys
import os


pathpath = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
os.chdir(pathpath)


def Basic_Graph(navio, xpoint, ypoint, dado_x, dado_y):

    if navio == 'Bulk Carrier':
        file_ROM = open('bulk_data_ROM.csv','rb')
        file_P50 = open('bulk_data_P50.csv','rb')
        file_P75 = open('bulk_data_P75.csv','rb')

    elif navio == 'Containership':
        file_ROM = open('cont_data_ROM.csv','rb')
        file_P50 = open('cont_data_P50.csv','rb')
        file_P75 = open('cont_data_P75.csv','rb')
        
    elif navio == 'General Cargo':
        file_ROM = open('general_data_ROM.csv','rb')
        file_P50 = open('general_data_P50.csv','rb')
        file_P75 = open('general_data_P75.csv','rb')

    DWT_ROM =[]
    LOA_ROM = []
    Lpp_ROM = []
    Beam_ROM = []
    Depth_ROM = []
    Draft_ROM = []
    Displ_ROM = []
    DWT_P50 =[]
    LOA_P50 = []
    Lpp_P50 = []
    Beam_P50 = []
    Depth_P50 = []
    Draft_P50 = []
    Displ_P50 = []
    DWT_P75 =[]
    LOA_P75 = []
    Lpp_P75 = []
    Beam_P75 = []
    Depth_P75 = []
    Draft_P75 = []
    Displ_P75 = []

    
    mycsv_ROM = list(csv.reader(file_ROM, delimiter=';'))
    for i in mycsv_ROM[1:]:
        DWT_ROM.append(float(i[0]))
        LOA_ROM.append(float(i[1]))
        Lpp_ROM.append(float(i[2]))
        Beam_ROM.append(float(i[3]))
        Depth_ROM.append(float(i[4]))
        Draft_ROM.append(float(i[5]))
        Displ_ROM.append(float(i[6]))
    mycsv_P50 = list(csv.reader(file_P50, delimiter=';'))
    for i in mycsv_P50[1:]:
        DWT_P50.append(float(i[0]))
        LOA_P50.append(float(i[1]))
        Lpp_P50.append(float(i[2]))
        Beam_P50.append(float(i[3]))
        Depth_P50.append(float(i[4]))
        Draft_P50.append(float(i[5]))
        Displ_P50.append(float(i[6]))
    mycsv_P75 = list(csv.reader(file_P75, delimiter=';'))
    for i in mycsv_P75[1:]:
        DWT_P75.append(float(i[0]))
        LOA_P75.append(float(i[1]))
        Lpp_P75.append(float(i[2]))
        Beam_P75.append(float(i[3]))
        Depth_P75.append(float(i[4]))
        Draft_P75.append(float(i[5]))
        Displ_P75.append(float(i[6]))

    xdata_ROM = dado_x + '_ROM'
    ydata_ROM = dado_y + '_ROM'
    xdata_P50 = dado_x + '_P50'
    ydata_P50 = dado_y + '_P50'
    xdata_P75 = dado_x + '_P75'
    ydata_P75 = dado_y + '_P75'

    ROM_data= plt.scatter(eval(xdata_ROM), eval(ydata_ROM), color = 'blue')
    P50_data = plt.scatter(eval(xdata_P50), eval(ydata_P50), color = 'black')
    P75_data = plt.scatter(eval(xdata_P75), eval(ydata_P75), color = 'green')
    calc_data = plt.scatter(xpoint,ypoint,color='red')
    plt.legend((ROM_data, P50_data, P75_data, calc_data),
               ('Original Data from ROM', 'Original Data from PIANC (50% Conf. Limit)', 'Original Data from PIANC (75% Conf. Limit)', 'Calculated Data'),
               loc = 'upper left',
               scatterpoints=1,
               fontsize=12)
    if dado_y == 'Displ': dado_y = 'Displacement'
    plt.xlabel(dado_x, fontsize=14)
    plt.ylabel(dado_y,fontsize=14)
    plt.show()


 
