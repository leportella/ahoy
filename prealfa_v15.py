#!/usr/bin/python
# coding: utf-8

# Created by:   Leticia Portella Nascimento
# Created on:   14/02/2014
# Updated on:   25/11/2014
# Project:      programinha maroto
# Version:	15

import wx
import sys
import csv
import os
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


pathpath = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
os.chdir(pathpath)

from vessel_size import MyRegressionCurve
# import waterway_functions
# import optimoor_functions
from Graphs import *


class App(wx.App):

    def OnInit(self):
        self.frame1 = MainWindow(parent=None, id=-1) #creating the frame
        self.frame1.Show()
        self.SetTopWindow(self.frame1)
        return True

class MainWindow(wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Ahoy!', size=(200,200))
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour((237,240,241))
        
        #definindo os botes
        self.button1 = wx.Button(self.panel, label='Vessel Dimensions', pos=(20,15), size=(150,30))
        #self.button2 = wx.Button(self.panel, label='Waterway Project', pos=(20,45), size=(150,30))
        #self.button3 = wx.Button(self.panel, label='Optimoor Processing Results', pos=(20,75), size=(150,30))
        
        #fazendo o bind dos botes com o vento  
        self.Bind(wx.EVT_BUTTON, self.OnButton1Click, self.button1)
        #self.Bind(wx.EVT_BUTTON, self.OnButton2Click, self.button2)
        #self.Bind(wx.EVT_BUTTON, self.OnButton3Click, self.button3)
        favicon = wx.Icon('teste.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        self.SetIcon(favicon)

    def OnButton1Click(self, event):
        self.frame2 = Vessel_Dimensions(parent=None, id=-1)
        self.frame2.Show()

    # def OnButton2Click(self, event):
    #     self.frame3 = Waterway_Project(parent=None, id=-1)
    #     self.frame3.Show()
        
    # def OnButton3Click(self,event):
    #     self.frame4 = OptResults(parent=None, id=-1)
    #     self.frame4.Show()

class Functions():
    def SetMenu():
        #criando o menu
        statusBar = self.CreateStatusBar()
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menu1.Append(wx.NewId(), "&Exit", "Leaves the program")
        menuBar.Append(menu1, "&File")
        self.SetMenuBar(menuBar)

class Vessel_Dimensions(wx.Frame):
        
    def __init__(self, parent, id):
        wx.Frame.__init__(self, wx.GetApp().TopWindow, id, 'Ahoy! - Calculate Vessel Dimensions', size=(850,600))
        favicon = wx.Icon('teste.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        self.SetIcon(favicon)   
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour((237,240,241))
        
        #Functions.SetMenu()
        
        #definindo a janela
        #self.titulo = wx.StaticText(self.panel, label="CALCULATES VESSEL DIMENSIOS", pos=(300,5))
        
        #INPUTS
        self.chooseTipo = wx.StaticText(self.panel, label="Vessel Type", pos=(20,20))
        tipos = ['Bulk Carrier','Containership','General Cargo']
        self.listaTipos = wx.ComboBox(self.panel, choices=tipos, size=(100,20), pos=(20,40),style=wx.TE_PROCESS_ENTER)
        self.lista = wx.ComboBox(self.panel, choices=[],size=(100,20), pos=(240,40),style=wx.TE_PROCESS_ENTER)
        self.listaTipos.Bind(wx.EVT_COMBOBOX, self.onCombo)
        self.choose = wx.StaticText(self.panel, label="Input Data", pos=(140,20))
        self.value1 = wx.TextCtrl(self.panel, value= 'type a value',size=(100, 20), pos=(140,40))
        method = ['ROM', 'PIANC 50% Confidence Limit','PIANC 75% Confidence Limit']
        self.method = wx.ComboBox(self.panel, choices=method,size=(150,20), value='ROM', pos=(360,40),style=wx.TE_PROCESS_ENTER)
        self.methodchoose = wx.StaticText(self.panel, label="Method based on...", pos=(360,20))

        #resultados
        self.textDWT = wx.StaticText(self.panel, label="DWT = ", pos=(20,100))
        self.resultDWT = wx.StaticText(self.panel, label="", pos=(120,100))
        self.textLOA = wx.StaticText(self.panel, label="LOA = ", pos=(20,150))
        self.resultLOA = wx.StaticText(self.panel, label="", pos=(120,150))
        self.textLpp = wx.StaticText(self.panel, label="Lpp =", pos=(20,200))
        self.resultLpp = wx.StaticText(self.panel, label="", pos=(120,200))
        self.textBeam = wx.StaticText(self.panel, label="Beam =", pos=(20,250))
        self.resultBeam = wx.StaticText(self.panel, label="", pos=(120,250))
        self.text = wx.StaticText(self.panel, label="Depth =", pos=(20,300))
        self.resultDepth = wx.StaticText(self.panel, label="", pos=(120,300))
        self.textDraft = wx.StaticText(self.panel, label="Draft =", pos=(20,350))
        self.resultDraft = wx.StaticText(self.panel, label="", pos=(120,350))
        self.textDispl = wx.StaticText(self.panel, label="Displacement =", pos=(20,400))
        self.resultDispl = wx.StaticText(self.panel, label="", pos=(120,400))
            
        #areas emersas
        self.textWTrvBal = wx.StaticText(self.panel, label="Maximum Emerged Transversal Area = ", pos=(240,100))
        self.resultWTrvBal = wx.StaticText(self.panel, label="", pos=(440,100))
        self.textWTrvLoad = wx.StaticText(self.panel, label="Minimum Emerged Transversal Area = ", pos=(240,150))
        self.resultWTrvLoad = wx.StaticText(self.panel, label="", pos=(440,150))
        self.textWLatBal = wx.StaticText(self.panel, label="Maximum Emerged Lateral Area = ", pos=(240,200))
        self.resultWLatBal = wx.StaticText(self.panel, label="", pos=(440,200))
        self.textWLatLoad = wx.StaticText(self.panel, label="Minimum Emerged Lateral Area = ", pos=(240,250))
        self.resultWLatLoad = wx.StaticText(self.panel, label="", pos=(440,250))

        #areas emersas
        self.textATSMax = wx.StaticText(self.panel, label="Maximum Submerged Transversal Area = ", pos=(540,100))
        self.resultATSMax = wx.StaticText(self.panel, label="", pos=(740,100))
        self.textATSMin = wx.StaticText(self.panel, label="Minimum Submerged Transversal Area = ", pos=(540,150))
        self.resultATSMin = wx.StaticText(self.panel, label="", pos=(740,150))
        self.textALSMax = wx.StaticText(self.panel, label="Maximum Submerged Lateral Area = ", pos=(540,200))
        self.resultALSMax = wx.StaticText(self.panel, label="", pos=(740,200))
        self.textALSMin = wx.StaticText(self.panel, label="Minimum Submerged Lateral Area = ", pos=(540,250))
        self.resultALSMin = wx.StaticText(self.panel, label="", pos=(740,250))      

        
        #definindo botao de calcular
        self.Buttoncalcular = wx.Button(self.panel, label='Calculate', pos=(550,40), size=(100,20))
        self.Buttoncalcular.Bind(wx.EVT_BUTTON, self.OnButtonCalcular,self.Buttoncalcular)
     
    def OnButtonGDWT(self, event):
        dado = self.lista.GetValue()
        navio = self.listaTipos.GetValue()
        if dado == 'DWT' or dado == 'TEU': pass
        else: 
            newx =  float(eval('self.result' + dado + '.GetLabel()[0:-2]'))
            newy =  float(self.resultDWT.GetLabel())
            Basic_Graph(navio,  newx, newy, dado, 'DWT')
                
    def OnButtonGLOA(self, event):
        dado = self.lista.GetValue()
        navio = self.listaTipos.GetValue()
        if dado == 'LOA': pass
        else:
            if dado == 'DWT' or dado == 'TEU': newx =  float(self.resultDWT.GetLabel())
            else: newx =  float(eval('self.result' + dado + '.GetLabel()[0:-2]'))
            newy =  float(self.resultLOA.GetLabel()[0:-2])
            Basic_Graph(navio, newx, newy, dado, 'LOA')

            
    def OnButtonGLpp(self, event):
        dado = self.lista.GetValue()
        navio = self.listaTipos.GetValue()
        if dado == 'Lpp': pass
        else: 
            if dado == 'DWT' or dado == 'TEU': newx =  float(self.resultDWT.GetLabel())
            else: newx =  float(eval('self.result' + dado + '.GetLabel()[0:-2]'))
            newy =  float(self.resultLpp.GetLabel()[0:-2])
            Basic_Graph(navio, newx, newy, dado, 'Lpp')

            
    def OnButtonGBeam(self, event):
        dado = self.lista.GetValue()
        navio = self.listaTipos.GetValue()
        if dado == 'Beam': pass
        else: 
            if dado == 'DWT' or dado == 'TEU': newx =  float(self.resultDWT.GetLabel())
            else: newx =  float(eval('self.result' + dado + '.GetLabel()[0:-2]'))
            newy =  float(self.resultBeam.GetLabel()[0:-2])
            Basic_Graph(navio, newx, newy, dado, 'Beam')

            
    def OnButtonGDepth(self, event):
        dado = self.lista.GetValue()
        navio = self.listaTipos.GetValue()
        if dado == 'Depth': pass
        else: 
            if dado == 'DWT' or dado == 'TEU': newx =  float(self.resultDWT.GetLabel())
            else: newx =  float(eval('self.result' + dado + '.GetLabel()[0:-2]'))
            newy =  float(self.resultDepth.GetLabel()[0:-2])
            Basic_Graph(navio, newx, newy, dado, 'Depth')

            
    def OnButtonGDraft(self, event):
        dado = self.lista.GetValue()
        navio = self.listaTipos.GetValue()
        if dado == 'Draft': pass
        else: 
            if dado == 'DWT' or dado == 'TEU': newx =  float(self.resultDWT.GetLabel())
            else: newx =  float(eval('self.result' + dado + '.GetLabel()[0:-2]'))
            newy =  float(self.resultDraft.GetLabel()[0:-2])
            Basic_Graph(navio, newx, newy, dado, 'Draft')

    def OnButtonGDispl(self, event):
        dado = self.lista.GetValue()
        navio = self.listaTipos.GetValue()
        if dado == 'DWT' or dado == 'TEU': newx =  float(self.resultDWT.GetLabel())
        else: newx =  float(eval('self.result' + dado + '.GetLabel()[0:-2]'))
        newy =  float(self.resultDispl.GetLabel()[0:-2])
        Basic_Graph(navio, newx, newy, dado, 'Displ')


    def onCombo(self, event):

        if self.listaTipos.GetValue() == 'Bulk Carrier' or self.listaTipos.GetValue() == 'General Cargo':
            self.lista.Clear()
            self.lista.Append('DWT')
            self.lista.Append('LOA')
            self.lista.Append('Lpp')
            self.lista.Append('Beam')
            self.lista.Append('Depth')
            self.lista.Append('Draft')
        elif self.listaTipos.GetValue() == 'Containership':
            self.lista.Clear()
            self.lista.Append('TEU')
            self.lista.Append('LOA')
            self.lista.Append('Lpp')
            self.lista.Append('Beam')
            self.lista.Append('Depth')
            self.lista.Append('Draft')
            
    def OnButtonCalcular(self, event):

        try:
            float(self.value1.GetValue())
        except ValueError:
            errstr = "Error: Must be an number!! "
            dlg = wx.MessageDialog(self, errstr, "Ahoy!",
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        else:
            self.ButtonGDWT = wx.Button(self.panel, label='G', pos=(1,100), size=(15,15))
            self.Bind(wx.EVT_BUTTON, self.OnButtonGDWT, self.ButtonGDWT)
            self.ButtonGLOA = wx.Button(self.panel, label='G', pos=(1,150), size=(15,15))
            self.Bind(wx.EVT_BUTTON, self.OnButtonGLOA, self.ButtonGLOA)
            self.ButtonGLpp = wx.Button(self.panel, label='G', pos=(1,200), size=(15,15))
            self.Bind(wx.EVT_BUTTON, self.OnButtonGLpp, self.ButtonGLpp)
            self.ButtonGBeam = wx.Button(self.panel, label='G', pos=(1,250), size=(15,15))
            self.Bind(wx.EVT_BUTTON, self.OnButtonGBeam, self.ButtonGBeam)
            self.ButtonGDepth = wx.Button(self.panel, label='G', pos=(1,300), size=(15,15))
            self.Bind(wx.EVT_BUTTON, self.OnButtonGDepth, self.ButtonGDepth)
            self.ButtonGDraft = wx.Button(self.panel, label='G', pos=(1,350), size=(15,15))
            self.Bind(wx.EVT_BUTTON, self.OnButtonGDraft, self.ButtonGDraft)
            self.ButtonGDispl = wx.Button(self.panel, label='G', pos=(1,400), size=(15,15))
            self.Bind(wx.EVT_BUTTON, self.OnButtonGDispl, self.ButtonGDispl) 
            n = float(self.value1.GetValue())

            if self.method.GetValue() == 'ROM':
                if self.listaTipos.GetValue() == 'Bulk Carrier': self.Calculo_de_tamanho('Bulk Carrier', 'ROM', self.lista.GetValue(), n)                            
                elif self.listaTipos.GetValue() == 'Containership': self.Calculo_de_tamanho('Containership','ROM', self.lista.GetValue(), n)
                elif self.listaTipos.GetValue() == 'General Cargo': self.Calculo_de_tamanho('General Cargo','ROM', self.lista.GetValue(), n)
            elif self.method.GetValue() == 'PIANC 50% Confidence Limit':
                if self.listaTipos.GetValue() == 'Bulk Carrier': self.Calculo_de_tamanho('Bulk Carrier', 'P50', self.lista.GetValue(), n)                            
                elif self.listaTipos.GetValue() == 'Containership': self.Calculo_de_tamanho('Containership','P50', self.lista.GetValue(), n)
                elif self.listaTipos.GetValue() == 'General Cargo': self.Calculo_de_tamanho('General Cargo','P50', self.lista.GetValue(), n)
            elif self.method.GetValue() == 'PIANC 75% Confidence Limit':
                if self.listaTipos.GetValue() == 'Bulk Carrier': self.Calculo_de_tamanho('Bulk Carrier', 'P50', self.lista.GetValue(), n)                            
                elif self.listaTipos.GetValue() == 'Containership': self.Calculo_de_tamanho('Containership','P50', self.lista.GetValue(), n)
                elif self.listaTipos.GetValue() == 'General Cargo': self.Calculo_de_tamanho('General Cargo','P50', self.lista.GetValue(), n)

    def Calculo_de_tamanho(self, vessel, metodo, entrada, valor):
        valor = str(valor)

        if entrada == '' or entrada == None:
            errstr = "Error: A parameter must be chosen!! "
            dlg = wx.MessageDialog(self, errstr, "Ahoy!",
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
        else: 
        
            if MyRegressionCurve(vessel, metodo,entrada,valor) == 'error':
                errstr = "Error: No files to calculate! "
                dlg = wx.MessageDialog(self, errstr, "Ahoy!",
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
            else: 
                if vessel == 'Containership':
                    self.resultDWT.SetLabel(MyRegressionCurve(vessel,metodo,entrada,valor)['DWT'])
                    self.textDWT = wx.StaticText(self.panel, label="TEU = ", pos=(20,100))
                else:
                    self.resultDWT.SetLabel(MyRegressionCurve(vessel,metodo,entrada,valor)['DWT'])

                self.resultDWT.SetForegroundColour((wx.BLUE))
                self.resultLOA.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['LOA'])
                self.resultLOA.SetForegroundColour((wx.BLUE))
                self.resultLpp.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['Lpp'])
                self.resultLpp.SetForegroundColour(wx.BLUE)
                self.resultBeam.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['Beam'])
                self.resultBeam.SetForegroundColour(wx.BLUE)
                self.resultDepth.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['Depth'])
                self.resultDepth.SetForegroundColour(wx.BLUE)
                self.resultDraft.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['Draft'])
                self.resultDraft.SetForegroundColour(wx.BLUE)
                self.resultDispl.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['Displ'])
                self.resultDispl.SetForegroundColour(wx.BLUE)

                if entrada == 'DWT' or  entrada == 'LOA' or entrada == 'Lpp' or entrada == 'TEU':
                    self.resultWTrvBal.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['WTrvBal'])
                    self.resultWTrvBal.SetForegroundColour(wx.BLUE)
                    self.resultWTrvLoad.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['WTrvLoad'])
                    self.resultWTrvLoad.SetForegroundColour(wx.BLUE)
                    self.resultWLatBal.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['WLatBal'])
                    self.resultWLatBal.SetForegroundColour(wx.BLUE)
                    self.resultWLatLoad.SetLabel(MyRegressionCurve(vessel, metodo, entrada, valor)['WLatLoad'])
                    self.resultWLatLoad.SetForegroundColour(wx.BLUE)

                    if self.method.GetValue() == 'PIANC 50% Confidence Limit' or self.method.GetValue() == 'PIANC 75% Confidence Limit':
                        self.resultATSMax.SetLabel('')
                        self.resultATSMin.SetLabel('')
                        self.resultALSMax.SetLabel('')
                        self.resultALSMin.SetLabel('')
                    else:
                        self.resultATSMax.SetLabel('')
                        self.resultATSMax.SetForegroundColour(wx.BLUE)
                        self.resultATSMin.SetLabel('')
                        self.resultATSMin.SetForegroundColour(wx.BLUE)
                        self.resultALSMax.SetLabel('')
                        self.resultALSMax.SetForegroundColour(wx.BLUE)
                        self.resultALSMin.SetLabel('')
                        self.resultALSMin.SetForegroundColour(wx.BLUE)
                else:
                    self.resultWTrvBal.SetLabel('')
                    self.resultWTrvLoad.SetLabel('')
                    self.resultWLatBal.SetLabel('')
                    self.resultWLatLoad.SetLabel('')
                    self.resultATSMax.SetLabel('')
                    self.resultATSMin.SetLabel('')
                    self.resultALSMax.SetLabel('')
                    self.resultALSMin.SetLabel('')
                            


# class SQUAT(wx.Panel):
#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent,style=wx.NO_FULL_REPAINT_ON_RESIZE)
#         self.SetBackgroundColour((237,240,241))

#         tipos = ['Bulk Carrier','Containership','Tanker']
#         self.vessels = wx.ComboBox(self, choices=tipos, size=(100,20), pos=(130,50))
#         self.Txtvessels = wx.StaticText(self, label="Vessel Type", pos=(20,50))
        
#         self.TxtVelocidade = wx.StaticText(self, label="Speed (m/s)", pos=(20,100))
#         self.Velocidade = wx.TextCtrl(self, value= '',size=(50, 20), pos=(130,100))
    
#         self.Txtdep = wx.StaticText(self, label="Depth (m)", pos=(20,150))
#         self.dep = wx.TextCtrl(self, value= '',size=(50, 20), pos=(130,150))
        
#         self.TxtLpp = wx.StaticText(self, label="Lpp (m)", pos=(20,200))
#         self.Lpp = wx.TextCtrl(self, value= '',size=(50, 20), pos=(130,200))
        
#         self.TxtBeam = wx.StaticText(self, label="Beam (m)", pos=(20,250))
#         self.Beam = wx.TextCtrl(self, value= '',size=(50, 20), pos=(130,250))

#         self.TxtDraft = wx.StaticText(self, label="Draft (m)", pos=(20,300))
#         self.Draft = wx.TextCtrl(self, value= '',size=(50, 20), pos=(130,300))        
        
#         self.TxtCoefBl = wx.StaticText(self, label="Block Coeficient", pos=(20,350))
#         self.CoefBl = wx.TextCtrl(self, value= '',size=(50, 20), pos=(130,350))
        
#         self.TxtFolgas = wx.StaticText(self, label="Folga adicional (m)", pos=(20,400))
#         self.Folgas = wx.TextCtrl(self, value= '',size=(50, 20), pos=(130,400))
        
#         self.inner = wx.RadioButton(self, label="Inner Region", style=wx.RB_GROUP, pos=(20,450))
#         self.outer = wx.RadioButton(self, label="Outer Region", pos = (20,470))
        
#         self.TxtFnh = wx.StaticText(self, label="Froude Depth Number (Fnh): ", pos=(400,150))
#         self.TxtDesloc = wx.StaticText(self, label="Volume de deslocamento (m3): ", pos=(400,180))
        
#         self.TxtSquat = wx.StaticText(self, label="Squat calculado: ", pos=(400,210))
#         self.TxtVer1 = wx.StaticText(self, label="Froude Depth Number Test: ", pos=(400,240)) 
#         self.TxtVer2 = wx.StaticText(self, label="Squat  Test (squat+draft< water depth): ", pos=(400,270))
#         self.TxtVer3 = wx.StaticText(self, label="Depth/Draft Relation Test: ", pos=(400,300))
#         self.TxtVer4 = wx.StaticText(self, label="Squat + folgas: ", pos=(400,330))       
        
#         self.calcsquat = wx.Button(self,label='Calculate', pos=(20,550), size=(150,30))
#         self.calcsquat.Bind(wx.EVT_BUTTON, self.OnReturnSquat)
#         self.clearbutton = wx.Button(self,label='Clear Items', pos=(200,550), size=(150,30))
#         self.clearbutton.Bind(wx.EVT_BUTTON, self.OnClearItems)

#     def OnReturnSquat(self,event):

#         velocidade = self.Velocidade.GetValue()
#         dep = self.dep.GetValue()
#         Lpp = self.Lpp.GetValue()
#         Beam = self.Beam.GetValue()
#         Draft = self.Draft.GetValue()
#         CoefBl = self.CoefBl.GetValue()
#         Folgas = self.Folgas.GetValue()
#         if self.inner.GetValue() == True: region = 'inner'
#         elif self.outer.GetValue() == True: region = 'outer'
#         else:
#             errstr = "Error: What is the type of region!? "
#             dlg = wx.MessageDialog(self, errstr, "Ahoy! - Error", wx.OK | wx.ICON_ERROR)
#             dlg.ShowModal()
#             dlg.Destroy()

#         try: 
#             float(velocidade) and float(dep) and float(Lpp) and float(Beam) and float(Draft) and float(CoefBl)
#         except ValueError:
#             errstr = "Error: Not a Number! This is not possible! "
#             dlg = wx.MessageDialog(self, errstr, "Ahoy! - Error", wx.OK | wx.ICON_ERROR)
#             dlg.ShowModal()
#             dlg.Destroy()

#         resultado = waterway_functions.OnCalcSquat(self.vessels.GetValue(),float(velocidade), float(dep), float(Lpp), float(Beam), float(Draft), float(CoefBl),float(Folgas),region)
#         self.Fnh = wx.StaticText(self, label=str(round(resultado['Fnh'],2)), pos=(700,150))
#         self.Fnh.SetForegroundColour(wx.BLUE)
#         self.Desloc = wx.StaticText(self, label=str(int(resultado['Vol'])), pos=(700,180))        
#         self.Desloc.SetForegroundColour(wx.BLUE)
#         self.Squat = wx.StaticText(self, label=str(round(resultado['Squat'],2)), pos=(700,210))       
#         self.Squat.SetForegroundColour(wx.BLUE)
#         self.Ver1 = wx.StaticText(self, label=resultado['ver1'], pos=(700,240)) 
#         if resultado['ver1'] == 'ok': self.Ver1.SetForegroundColour(wx.BLUE)
#         else: self.Ver1.SetForegroundColour(wx.RED) 
#         self.Ver2 = wx.StaticText(self, label=resultado['ver2'], pos=(700,270))
#         if resultado['ver2'] == 'ok': self.Ver2.SetForegroundColour(wx.BLUE)
#         else: self.Ver2.SetForegroundColour(wx.RED) 
#         self.Ver3 = wx.StaticText(self, label=resultado['ver3'], pos=(700,300))
#         if resultado['ver3'] == 'ok': self.Ver3.SetForegroundColour(wx.BLUE)
#         else: self.Ver3.SetForegroundColour(wx.RED)      
#         self.Ver4 = wx.StaticText(self, label=resultado['ver4'], pos=(700,330))
#         if resultado['ver4'] == 'ok': self.Ver4.SetForegroundColour(wx.BLUE)
#         else: self.Ver4.SetForegroundColour(wx.RED) 
 
#     def OnClearItems(self, event):
#         self.Velocidade.Clear()
#         self.dep.Clear()
#         self.Lpp.Clear()
#         self.Beam.Clear()
#         self.Draft.Clear() 
#         self.CoefBl.Clear()
#         self.Folgas.Clear()
#         self.Fnh.SetLabel('')
#         self.Desloc.SetLabel('')
#         self.Squat.SetLabel('')   
#         self.Ver1.SetLabel('')
#         self.Ver2.SetLabel('')
#         self.Ver3.SetLabel('')
#         self.Ver4.SetLabel('')
    
# class WATERWAY(wx.Panel):
#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent,style=wx.NO_FULL_REPAINT_ON_RESIZE)
#         self.SetBackgroundColour((237,240,241))

#         self.inner = wx.RadioButton(self, label="Inner Channel", style=wx.RB_GROUP, pos=(470,20))
#         self.outer = wx.RadioButton(self, label="Outer Channel", pos = (470,40))

#         self.single = wx.RadioButton(self, label="One way Channel", style=wx.RB_GROUP, pos=(620,20))
#         self.double = wx.RadioButton(self, label="Two way Channel", pos = (620,40))
        
#         self.TxtLOA = wx.StaticText(self, label="LOA (m)", pos=(20,20))
#         self.LOA = wx.TextCtrl(self, value= '',size=(120, 20), pos=(250,20))

#         self.TxtBeam = wx.StaticText(self, label="Beam(m)", pos=(20,70))
#         self.Beam = wx.TextCtrl(self, value= '',size=(120, 20), pos=(250,70))
    
#         self.TxtDraft = wx.StaticText(self, label="Draft (m)", pos=(20,120))
#         self.Draft = wx.TextCtrl(self, value= '',size=(120, 20), pos=(250,120))
    
#         manouve = ['Good','Moderate','Poor']
#         self.TxtManouve = wx.StaticText(self, label="Ship Manoeuvrability", pos=(20,170))
#         self.manouve = wx.ComboBox(self, choices=manouve, size=(120,20), pos=(250,170))

#         Speed=['Fast  (> 12)','Moderate (8-12)','Slow (5-8)']
#         self.TxtSpeed = wx.StaticText(self, label="Vessel Speed (knots)", pos=(20,220))
#         self.Speed = wx.ComboBox(self, choices= Speed, size=(120, 20), pos=(250,220))

#         Wind = ['Mild (< 15)','Moderate (15-33)','Severe  (33-48)'] 
#         self.TxtWind = wx.StaticText(self, label="Prevailing cross wind (knots)", pos=(20,270))
#         self.Wind = wx.ComboBox(self, choices = Wind,size=(120, 20), pos=(250,270))

#         CrossCurrent = ['Negligible (< 0.2)','Low (0.2-0.5)','Moderate (0.5-1.5)','Strong (> 3)']
#         self.TxtCrossCurrent = wx.StaticText(self, label="Prevailing cross current (knots)", pos=(20,320))
#         self.CrossCurrent = wx.ComboBox(self, choices = CrossCurrent, size=(120, 20), pos=(250,320),)

#         LongCurrent = ['Low (<1.5)','Moderate (1.5-3)','Strong  (> 3)']
#         self.TxtLongCurrent = wx.StaticText(self, label="Prevailing longitudinal current (knots)", pos=(20,370))
#         self.LongCurrent = wx.ComboBox(self, choices = LongCurrent, size=(120, 20), pos=(250,370))

#         WHeight = ['Hs < 1 and L < LOA', '3 > Hs > 1 and L = LOA', 'Hs > 3 and L > LOA']
#         self.TxtWHeight = wx.StaticText(self, label="Significant wave height (Hs) and length (L)", pos=(20,420))
#         self.WHeight = wx.ComboBox(self, choices= WHeight,size=(120, 20), pos=(250,420))     

#         self.TxtDWaterway = wx.StaticText(self, label="Depth of Waterway", pos=(20,470))
#         self.DWaterway = wx.TextCtrl(self, value= '',size=(120, 20), pos=(250,470))

#         Cargo = ['Low','Medium','High']
#         self.TxtBS = wx.StaticText(self, label="Cargo Hazzard level", pos=(20,520))
#         self.Cargo = wx.ComboBox(self, choices=Cargo, size=(120,20), pos=(250,520))

#         Traffic = ['Light','Moderate','Heavy']
#         self.TxtTraffic = wx.StaticText(self, label="Encounter Traffic Density", pos=(20,570))
#         self.Traffic = wx.ComboBox(self, choices=Traffic, size=(120,20), pos=(250,570))
        
#         Width = ['Sloping channel edges and shoals','Steep and hard embankments, structures']
#         self.TxtWidth = wx.StaticText(self, label="Width for bank clearance", pos=(20,620))
#         self.Width = wx.ComboBox(self, choices=Width, size=(205,20), pos=(250,620))

#         aids = ['Excellent with shore traffic control','Good','Moderate with infrequent poor visibility','Moderate with frequent poor visibility ']
#         self.TxtAids = wx.StaticText(self, label="Aids to Navigation", pos=(20,670))
#         self.Aids = wx.ComboBox(self, choices=aids, size=(200,20), pos=(250,670))

#         BS = ['Smooth and soft','Smooth or sloping and hard','Rough and hard']
#         self.TxtBS = wx.StaticText(self, label="Bottom Surface", pos=(20,720))
#         self.BS = wx.ComboBox(self, choices=aids, size=(200,20), pos=(250,720))

#         self.TextWbm = wx.StaticText(self, label="Basic Manoeuvring Lane (Wbm): ", pos=(500,220))
#         self.Wbm = wx.StaticText(self, label="", pos=(900,220))

#         self.TextWi = wx.StaticText(self, label="Aditional Width for Straight Channel Sections (Sum of Wi): ", pos=(500,250))
#         self.Wi = wx.StaticText(self, label="", pos=(900,250))

#         self.TextWb = wx.StaticText(self, label="Aditional Width for Bank Clearance at red and green side of channel (Wb): ", pos=(500,280))
#         self.Wb = wx.StaticText(self, label="", pos=(900,280))

#         self.TextWp = wx.StaticText(self, label="Aditional Width for Passing Distance in Two-Way Traffic (Wp): ", pos=(500,310))
#         self.Wp = wx.StaticText(self, label="", pos=(900,310))

#         self.TextW = wx.StaticText(self, label="Total Width of the Channel:", pos=(500,340))
#         self.W = wx.StaticText(self, label="", pos=(900,340))
        
#         self.calcwaterway = wx.Button(self,label='Calculate', pos=(800,20), size=(150,30))
#         self.calcwaterway.Bind(wx.EVT_BUTTON, self.OnReturnWaterway)
            
#     def OnReturnWaterway(self,event):

#         beam = float(self.Beam.GetValue())
#         draft = float(self.Draft.GetValue())
#         loa = float(self.LOA.GetValue())
#         manouve = self.manouve.GetValue()
#         aids = self.Aids.GetValue()
#         bottomsurface = self.BS.GetValue()
#         cargo = self.Cargo.GetValue()
#         traffic = self.Traffic.GetValue()
#         width = self.Width.GetValue()
#         speed = self.Speed.GetValue()
#         wind = self.Wind.GetValue()
#         crosscurrent = self.CrossCurrent.GetValue()
#         longcurrent = self.LongCurrent.GetValue()
#         wheight = self.WHeight.GetValue()
#         dwaterway = self.DWaterway.GetValue()
#         if self.inner.GetValue(): channel = 'inner'
#         else: channel = 'outer'
#         if self.single.GetValue(): type = "One way Channel"
#         else: type = 'Two way Channel'
        
#         resultado = waterway_functions.OnWaterway(beam, draft, loa, manouve, aids, bottomsurface, cargo, traffic, width, speed, 
#                     wind, crosscurrent, longcurrent, wheight, dwaterway, channel, type)

#         self.Wbm.SetLabel(str(resultado['Wbm'])+ ' m')
#         self.Wbm.SetForegroundColour(wx.BLUE) 
#         self.Wi.SetLabel(str(resultado['Wi'])+' m')
#         self.Wi.SetForegroundColour(wx.BLUE) 
#         self.Wp.SetLabel(str(resultado['Wp']) + ' m')
#         self.Wp.SetForegroundColour(wx.BLUE) 
#         self.Wb.SetLabel(str(resultado['Wb']) + ' m')
#         self.Wb.SetForegroundColour(wx.BLUE) 
#         self.W.SetLabel(str(resultado['W']) + ' m')
#         self.W.SetForegroundColour(wx.BLUE) 

# class PageThree(wx.Panel):
#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent)
#         self.SetBackgroundColour((237,240,241))
#         t = wx.StaticText(self, -1, "This is a PageThree object", (60,60))
            
# class Waterway_Project(wx.Frame):
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, wx.GetApp().TopWindow, id, 'Outra Janela', size=(1000,850))
#         favicon = wx.Icon('teste.ico', wx.BITMAP_TYPE_ICO, 16, 16)
#         self.SetIcon(favicon)   
#         p = wx.Panel(self)
#         p.SetBackgroundColour((237,240,241))
#         nb = wx.Notebook(p)
        
#         pag_squat = SQUAT(nb)
#         pag2 = WATERWAY(nb)
#         pag3 = PageThree(nb)

#         nb.AddPage(pag_squat, "SQUAT")
#         nb.AddPage(pag2, "WATERWAY")
#         nb.AddPage(pag3, "Item 3")

#         sizer = wx.BoxSizer()
#         sizer.Add(nb, 1, wx.EXPAND)
#         p.SetSizer(sizer)

# class OptResults(wx.Frame):
        
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, wx.GetApp().TopWindow, id, 'Ahoy! - Optimoor Processing Results', size=(600,400))
#         favicon = wx.Icon('teste.ico', wx.BITMAP_TYPE_ICO, 16, 16)
#         self.SetIcon(favicon)   
#         self.panel = wx.Panel(self)
#         self.panel.SetBackgroundColour((237,240,241))
             
#         self.static = wx.RadioButton(self.panel, label="Static Scenario", style=wx.RB_GROUP, pos=(20,20))
#         self.dyn = wx.RadioButton(self.panel, label="Dynamic scenario", pos = (20,50))

#         self.TxtCapacity = wx.StaticText(self.panel, label="Bollards Capacity (t): ", pos=(20,80))
#         self.Capacity = wx.TextCtrl(self.panel, value= '',size=(120, 20), pos=(130,80))

#         self.TxtDirectory = wx.StaticText(self.panel, label="Directory of CSV file: ", pos=(20,110))
#         self.Directory = wx.TextCtrl(self.panel, value= '',size=(410, 20), pos=(130,110))
        
#         self.TxtHeader = wx.StaticText(self.panel, label="Cables numbers (ascending orders):", pos=(20,140))
#         self.Header = wx.TextCtrl(self.panel, value= '',size=(300, 20), pos=(240,140))

#         self.calcOptResults = wx.Button(self.panel,label='Resume results', pos=(390,20), size=(150,30))
#         self.calcOptResults.Bind(wx.EVT_BUTTON, self.OnReturnOptimoorResults)
        
#     def OnReturnOptimoorResults(self, event):

#        path = self.Directory.GetValue()
#        #if path[0][-1] == r'/':
#        #    path = path[0][0:-2]

#        try: capacity = int(self.Capacity.GetValue())
#        except ValueError:
#             errstr = "Error! The bollard's capacity is not a number! "
#             dlg = wx.MessageDialog(self, errstr, "Ahoy! - Error", wx.OK | wx.ICON_ERROR)
#             dlg.ShowModal()
#             dlg.Destroy()

#        capacity = int(self.Capacity.GetValue())
#        cables = self.Header.GetValue()
#        cables2 = cables.split(',')
#        final = map(int, cables2)

#        if self.static.GetValue():
#             result = optimoor_functions.Static_results(path, capacity, final)
#             if result == 'Errorcables':
#                 errstr = "Error! More cables were used then typed here!"
#                 dlg = wx.MessageDialog(self, errstr, "Ahoy! - Error", wx.OK | wx.ICON_ERROR)
#                 dlg.ShowModal()
#                 dlg.Destroy()
#             elif result == 'Errorpath':
#                 errstr = "Error! This is a not valid directory!"
#                 dlg = wx.MessageDialog(self, errstr, "Ahoy! - Error", wx.OK | wx.ICON_ERROR)
#                 dlg.ShowModal()
#                 dlg.Destroy()
#             else:
#                 self.Result = wx.StaticText(self.panel, label="The results were compiled with success. Please, check the directory.", pos=(20,250))
                
if __name__ == '__main__':
    app = App(False)
    app.MainLoop()
