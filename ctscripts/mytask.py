from org.dspace.curate import ScriptedTask
from org.dspace.curate import Curator
from org.dspace.content.service import DSpaceObjectService
from org.dspace.content.factory import ContentServiceFactory

#from org.dspace.content.service import BitstreamService
 
class MyTask(ScriptedTask):
        def init(self, curator, taskName):
                print "initializing with Jython"
 
        def performDso(self, dso):
                print "perform on dso "
                if dso.getType()==2:
                        print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
                        myBundles = dso.itemService.getBundles(dso,"VISOR")
                        for i in myBundles:
                                myBitstreams = i.getBitstreams()
                                total = len(myBitstreams)
                                print "Total of  "+str(total)+" files"
                                if len(myBitstreams)==0:
                                    print "ESBORRO BUNDLE"
                                    dso.itemService.removeBundle(Curator.curationContext(),dso,myBundles[0])
                                if len(myBitstreams)>0:
                                    for k in range(0,len(myBitstreams)):
                                            print "DELETE "+myBitstreams[k].getName()
                                            bitstreamService = ContentServiceFactory.getInstance().getBitstreamService()
                                            
                                            bitstreamService.delete(Curator.curationContext(),myBitstreams[k])
                                            
                                            print len(myBitstreams)
                                            #        myBitstreams[k].getBundles().remove(i)
                                    print "ESBORRO BUNDLE"
                                    dso.itemService.removeBundle(Curator.curationContext(),dso,myBundles[0])
                return 0
 
        def performId(self, context, id):
                print "perform on id %s" % (id)
                return 0
