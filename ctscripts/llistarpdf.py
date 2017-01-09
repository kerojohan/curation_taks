from org.dspace.curate import ScriptedTask
from org.dspace.curate import Curator
from org.dspace.content.service import DSpaceObjectService
from org.dspace.content.factory import ContentServiceFactory

#from org.dspace.content.service import BitstreamService
 
class Main(ScriptedTask):
        def init(self, curator, taskName):
                print "initializing with Jython"
 
        def performDso(self, dso):
                if dso.getType()==2:
                        myBundles = dso.itemService.getBundles(dso,"ORIGINAL")
                        print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
                        for i in myBundles:
                                myBitstreams = i.getBitstreams()
                                total = len(myBitstreams)
               
                                if len(myBitstreams)>0:
                                    for k in range(0,len(myBitstreams)):
		                        #if ".pdf" in myBitstreams[k].getName() and ".pdf.txt" not in myBitstreams[k].getName() and "_sum.pdf" not in myBitstreams[k].getName():
                                        if "pdf" in myBitstreams[k].getName():
                                            print myBitstreams[k].getName()
                return 0
 
        def performId(self, context, id):
                print "perform on id %s" % (id)
                return 0
