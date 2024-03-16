#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# !pip install -U ultralytics
# !pip install opencv-python
# !pip install dxcam
# !pip install pydirectinput-rgx
# !pip install shapely
# !pip install sahi
# !pip install keyboard
# !pip install pywin32
# !pip install --quiet PySide6


# In[2]:


import sys
import os
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import  Qt, QRunnable, Slot, QThreadPool,QProcess
from PySide6.QtGui import QIcon, QCloseEvent
import re

# import run

from configparser import ConfigParser


# In[3]:


settings_file='settings.ini'
config = ConfigParser()
config.read(settings_file)
# list(config['custom'])


# In[4]:


class mywidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=loader.load('UI_design.ui',None)
        self.ui.setWindowIcon(QIcon("icon.png"))
        
        self.threadpool = QThreadPool()
        
        if self.read_config('custom','FPS')=='True':
            self.ui.FPS_checkBox.setCheckState(Qt.Checked)
        if self.read_config('custom','VERBOSE')=='True':
            self.ui.VERBOSE_checkBox.setCheckState(Qt.Checked)
        if self.read_config('custom','AIM_ASSIST')=='True':
            self.ui.AIM_ASSIST_checkBox.setCheckState(Qt.Checked)
        if self.read_config('custom','AUTO_TRIGGER')=='True':
            self.ui.AUTO_TRIGGER_checkBox.setCheckState(Qt.Checked)
        if self.read_config('custom','ALWAYS_ACTIVE')=='True':
            self.ui.ALWAYS_ACTIVE_checkBox.setCheckState(Qt.Checked)
            
        if self.read_config('custom','PREDICT')=='True':    
            self.ui.PREDICT_radioButton.setChecked(True)
        if self.read_config('custom','SAHI')=='True':    
            self.ui.SAHI_radioButton.setChecked(True)
        if self.read_config('custom','HEAD')=='True':
            self.ui.HEAD_radioButton.setChecked(True)
        if self.read_config('custom','BODY')=='True':
            self.ui.BODY_radioButton.setChecked(True)
        if self.read_config('custom','RANDOM')=='True':
            self.ui.RANDOM_radioButton.setChecked(True)
        
        
        self.ui.SAHI_CT_lineEdit.setText(self.read_config('custom','SAHI_CT'))
        self.ui.YOLO_CONFIDENCE_THRESHOLD_lineEdit.setText(self.read_config('custom','YOLO_CONFIDENCE_THRESHOLD'))
        self.ui.IOU_lineEdit.setText(self.read_config('custom','IOU'))
        self.ui.MODEL_PATH_lineEdit.setText(self.read_config('custom','MODEL_PATH'))
        self.ui.LEFT_lineEdit.setText(self.read_config('custom','LEFT'))
        self.ui.TOP_lineEdit.setText(self.read_config('custom','TOP'))
        self.ui.RIGHT_lineEdit.setText(self.read_config('custom','RIGHT'))
        self.ui.BOTTOM_lineEdit.setText(self.read_config('custom','BOTTOM'))
        self.ui.SCALE_lineEdit.setText(self.read_config('custom','SCALE'))
        self.ui.ACTIVATE_KEY_lineEdit.setText(self.read_config('custom','ACTIVATE_KEY'))
        self.ui.D_or_E_KEY_lineEdit.setText(self.read_config('custom','D_or_E_KEY'))
        
        self.ui.Browse_pushButton.clicked.connect(self.getModelPath)
        self.ui.DEFAULT_pushButton.clicked.connect(self.default_settings)
        self.ui.APPLY_pushButton.clicked.connect(self.apply_settings)
        self.ui.RUN_pushButton.clicked.connect(self.RUN)
        
        app.aboutToQuit.connect(self.closeEvent)
        
    def getModelPath(self):
        file_filter='PyTorch Model (*.pt *.pth)'
        model_path=QFileDialog.getOpenFileName(
            self, 
            'Select a model',
            dir=os.getcwd(),
            filter=file_filter 
        )
        self.ui.MODEL_PATH_lineEdit.setText(model_path[0])
   
    def show_FPS(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.ui.FPS_textEdit.setText(stdout)#[5:50])
        
    def show_ERROR(self):
        error=self.p.readAllStandardError()
        if len(error)>1:
            # print(error)
            # print(len(error))
            stderr=bytes(error).decode("latin-1")
            self.ui.FPS_textEdit.append(stderr)#[5:50])
        # else:print(error)
        
    
    def apply_settings(self):
        config.set('custom','FPS',str(self.ui.FPS_checkBox.isChecked() ) )
        config.set('custom','VERBOSE',str(self.ui.VERBOSE_checkBox.isChecked() ) )
        config.set('custom','AIM_ASSIST',str(self.ui.AIM_ASSIST_checkBox.isChecked() ) )
        config.set('custom','AUTO_TRIGGER',str(self.ui.AUTO_TRIGGER_checkBox.isChecked() ) )
        
        config.set('custom','PREDICT',str(self.ui.PREDICT_radioButton.isChecked() ) )
        config.set('custom','SAHI',str(self.ui.SAHI_radioButton.isChecked() ) )
        config.set('custom','HEAD',str(self.ui.HEAD_radioButton.isChecked() ) )
        config.set('custom','BODY',str(self.ui.BODY_radioButton.isChecked() ) )
        config.set('custom','RANDOM',str(self.ui.RANDOM_radioButton.isChecked() ) )
        
        config.set('custom','SAHI_CT', self.ui.SAHI_CT_lineEdit.text())
        config.set('custom','YOLO_CONFIDENCE_THRESHOLD', self.ui.YOLO_CONFIDENCE_THRESHOLD_lineEdit.text())
        config.set('custom','IOU', self.ui.IOU_lineEdit.text())
        config.set('custom','MODEL_PATH', self.ui.MODEL_PATH_lineEdit.text())
        config.set('custom','LEFT', self.ui.LEFT_lineEdit.text())
        config.set('custom','TOP', self.ui.TOP_lineEdit.text())
        config.set('custom','RIGHT', self.ui.RIGHT_lineEdit.text())
        config.set('custom','BOTTOM', self.ui.BOTTOM_lineEdit.text())
        config.set('custom','SCALE', self.ui.SCALE_lineEdit.text())
        config.set('custom','ACTIVATE_KEY', self.ui.ACTIVATE_KEY_lineEdit.text())
        config.set('custom','D_or_E_KEY', self.ui.D_or_E_KEY_lineEdit.text())      
        
        with open(settings_file,'w') as config_file:
            config.write(config_file)
            

    def default_settings(self):
        
        if self.read_config('default','FPS')=='True':
            self.ui.FPS_checkBox.setCheckState(Qt.Checked)
        else:
            self.ui.FPS_checkBox.setCheckState(Qt.Unchecked)
        if self.read_config('default','VERBOSE')=='True':
            self.ui.VERBOSE_checkBox.setCheckState(Qt.Checked)
        else:
            self.ui.VERBOSE_checkBox.setCheckState(Qt.Unchecked)
        if self.read_config('default','AIM_ASSIST')=='True':
            self.ui.AIM_ASSIST_checkBox.setCheckState(Qt.Checked)
        else:
            self.ui.AIM_ASSIST_checkBox.setCheckState(Qt.Unchecked)
        if self.read_config('default','AUTO_TRIGGER')=='True':
            self.ui.AUTO_TRIGGER_checkBox.setCheckState(Qt.Checked)
        else:
            self.ui.AUTO_TRIGGER_checkBox.setCheckState(Qt.Unchecked)
        if self.read_config('default','ALWAYS_ACTIVE')=='True':
            self.ui.ALWAYS_ACTIVE_checkBox.setCheckState(Qt.Checked)
        else:
            self.ui.ALWAYS_ACTIVE_checkBox.setCheckState(Qt.Unchecked)
            
        if self.read_config('default','PREDICT')=='True':    
            self.ui.PREDICT_radioButton.setChecked(True)
        if self.read_config('default','HEAD')=='True':
            self.ui.HEAD_radioButton.setChecked(True)
        if self.read_config('default','BODY')=='True':
            self.ui.BODY_radioButton.setChecked(True)
        if self.read_config('default','RANDOM')=='True':
            self.ui.RANDOM_radioButton.setChecked(True)
        
        
        self.ui.SAHI_CT_lineEdit.setText(self.read_config('default','SAHI_CT'))
        self.ui.YOLO_CONFIDENCE_THRESHOLD_lineEdit.setText(self.read_config('default','YOLO_CONFIDENCE_THRESHOLD'))
        self.ui.IOU_lineEdit.setText(self.read_config('default','IOU'))
        self.ui.MODEL_PATH_lineEdit.setText(self.read_config('default','MODEL_PATH'))
        self.ui.LEFT_lineEdit.setText(self.read_config('default','LEFT'))
        self.ui.TOP_lineEdit.setText(self.read_config('default','TOP'))
        self.ui.RIGHT_lineEdit.setText(self.read_config('default','RIGHT'))
        self.ui.BOTTOM_lineEdit.setText(self.read_config('default','BOTTOM'))
        self.ui.SCALE_lineEdit.setText(self.read_config('default','SCALE'))
        self.ui.ACTIVATE_KEY_lineEdit.setText(self.read_config('default','ACTIVATE_KEY'))
        self.ui.D_or_E_KEY_lineEdit.setText(self.read_config('default','D_or_E_KEY'))

    def RUN(self):
        if self.ui.RUN_pushButton.text()=='RUN':
            self.ui.RUN_pushButton.setText("STOP")
            self.ui.RUN_pushButton.setStyleSheet('QPushButton{color: rgb(255, 255, 255);background-color: rgb(135, 0, 0);text-decoration: underline;font: 700 14pt "Verdana";border-radius: 7px;}QPushButton:hover{	background-color:rgba(135, 0, 0,200);}QPushButton:pressed{	background-color: rgba(135, 0, 0,150);}')
            self.p = QProcess()
            self.p.start("python", ['run.py'])
            
            if self.read_config('custom','FPS')=='True':
                self.p.readyReadStandardError.connect(self.show_ERROR)
                self.p.readyReadStandardOutput.connect(self.show_FPS)
                

            
        else:
            self.ui.RUN_pushButton.setText("RUN")
            self.ui.RUN_pushButton.setStyleSheet('QPushButton{color: rgb(255, 255, 255);background-color: rgb(0, 135, 0);text-decoration: underline;font: 700 14pt "Verdana";border-radius: 7px;}QPushButton:hover{	background-color:rgba(0, 135, 0,200);}QPushButton:pressed{	background-color: rgba(0, 135, 0,150);}') 
            self.p.kill()
            
            

            

    def read_config(self, section, key):
        return config[section][key]
        
    def show(self):
        self.ui.show()
        
    def closeEvent(self):
        self.p.kill()
        QCloseEvent().accept()
       


# In[5]:


loader=QUiLoader()


# In[6]:


app= QApplication(sys.argv)


# In[7]:


widget= mywidget()

widget.show()

app.exec()


# In[ ]:




