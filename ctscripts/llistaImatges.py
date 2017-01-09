from org.dspace.curate import ScriptedTask
from org.dspace.curate import Curator
from org.dspace.content.service import DSpaceObjectService
from org.dspace.content.factory import ContentServiceFactory
import subprocess
import math

#from org.dspace.content.service import BitstreamService

class Main(ScriptedTask):
        def init(self, curator, taskName):
                print "initializing with Jython"

        def performDso(self, dso):
                #print "perform on dso "
                if dso.getType()==2:
                        #print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
                        myBundles = dso.itemService.getBundles(dso,"ORIGINAL")
                        totalbundles = len(myBundles)
                        for i in myBundles:
				print "\"https://calaix-new-pro.csuc.cat/handle/"+dso.getHandle()+"\",\""+dso.getName()+"\"" 
                                myBitstreams = i.getBitstreams()
                                total = len(myBitstreams)
                                if len(myBitstreams)>0:
                                    for k in range(0,len(myBitstreams)):
					if (".pdf" not in myBitstreams[k].getName()):
                                            #print str(int(wout2)) 
                                            print myBitstreams[k].getName() 
#print path
                return 0

        def performId(self, context, id):
                print "perform on id %s" % (id)
                return 0
