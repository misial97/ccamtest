#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines
#Creado por Dagger - https://github.com/gavazquez

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 5

#Filename must start with Server, classname and argument must be the same!
class Satunivers(ReloadCam_Main.Server):

    def GetUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt('maanpH1wfNvT0t7UxaVgppW3trvb29Hh1JKlqGKXqq982cra1NPFpZedmKyle-LN3A==')
        return realUrl

    def GetClines(self):
        print ("Now getting Satunivers clines!")
        satUniverseClines = []
        satUniverseClines.append(self.__GetSatuniversCline())
        satUniverseClines = filter(None, satUniverseClines)
        if len(satUniverseClines) == 0: print ("No Satunivers lines retrieved")
        return satUniverseClines

    def __GetSatuniversCline(self):

        values= {
            'user': ReloadCam_Helper.GetRandomString(5),
            'pass': ReloadCam_Helper.GetRandomString(5)
        }

        htmlCode = ReloadCam_Helper.GetPostHtmlCode(values, None, self.GetUrl())
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
        return None
