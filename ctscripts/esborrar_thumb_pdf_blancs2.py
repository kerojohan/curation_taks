from org.dspace.curate import ScriptedTask
from org.dspace.curate import Curator
from org.dspace.content.service import DSpaceObjectService
from org.dspace.content.factory import ContentServiceFactory
import subprocess

#from org.dspace.content.service import BitstreamService

class MyTask(ScriptedTask):
        def init(self, curator, taskName):
                print "initializing with Jython"

        def performDso(self, dso):
                #print "perform on dso "
                if dso.getType()==2:
                      #  print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
                        myBundles = dso.itemService.getBundles(dso,"THUMBNAIL")
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
                                        size=["identify", "-format","%b",path]
                                        p = subprocess.Popen(size, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                                        wout, err = p.communicate()
                                        print wout

                                        if ( "4563B" in wout ):
                                            print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
                                            print str(wout) 
                                            print "DELETING THUMBNAIL"+myBitstreams[0].getName()
                                            bitstreamService = ContentServiceFactory.getInstance().getBitstreamService()
                                            bitstreamService.delete(Curator.curationContext(),myBitstreams[0])




#print path
                return 0

        def performId(self, context, id):
                print "perform on id %s" % (id)
                return 0
