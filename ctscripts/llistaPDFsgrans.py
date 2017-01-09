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
                                myBitstreams = i.getBitstreams()
                                total = len(myBitstreams)
                                if len(myBitstreams)>0:
                                    for k in range(0,len(myBitstreams)):
                                        asset=0
                                        asset=myBitstreams[0].getInternalId()
                                        path="/projectes/calaix/dspace/assetstore/"+str(asset[:2])+'/'+str(asset[2:4])+'/'+str(asset[4:6])+'/'+asset
#                                        identify -format "%w"
                                        pes=["ls","-l",path]
					cut=["cut", "-d"," ","-f5"]
					p = subprocess.Popen(pes, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                                        p2 = subprocess.Popen(cut,stdin=p.stdout, stdout=subprocess.PIPE)
                                        wout, err = p2.communicate()
					#p2 = subprocess.Popen(cut, stdin=p.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                                        #wout2, err = p2.communicate()
                                        mida= str((int(wout)/1024)/1024)+"MB"
					if (".pdf" in myBitstreams[k].getName() and int(wout) > 60000000 ):
                                            #print str(int(wout2)) 
                                            print "\"https://calaix-new-pro.csuc.cat/handle/"+dso.getHandle()+"\",\"" + dso.getName() + "\",\"" + myBitstreams[0].getName() + "\",\""+mida+"\"" 
#print path
                return 0

        def performId(self, context, id):
                print "perform on id %s" % (id)
                return 0
