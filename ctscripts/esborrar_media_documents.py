from org.dspace.curate import ScriptedTask
from org.dspace.curate import Curator
from org.dspace.content.service import DSpaceObjectService
from org.dspace.content.factory import ContentServiceFactory

#from org.dspace.content.service import BitstreamService
 
class DMD(ScriptedTask):
        def init(self, curator, taskName):
                print "initializing with Jython"
 
        def performDso(self, dso):
                if dso.getType()==2:
                        print dso.getHandle()
                        #print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
                        myBundles = dso.itemService.getBundles(dso,"MEDIA_DOCUMENT")
			#if (len(myBundles))>1:
                        for i in myBundles:
                           
                            myBitstreams = i.getBitstreams()
                            total = len(myBitstreams)
                            print "Total of  "+str(total)+" files"
                            if len(myBitstreams)==0:
                                print "ESBORRO BUNDLE"
                                dso.itemService.removeBundle(Curator.curationContext(),dso,i)
                            if len(myBitstreams)>0:
                                for k in range(0,len(myBitstreams)):
                                    #if ".pdf.xml" in myBitstreams[0].getName():
                                    print "ESBORRO fitxer"+myBitstreams[0].getName()
                                    bitstreamService = ContentServiceFactory.getInstance().getBitstreamService()
                                    bitstreamService.delete(Curator.curationContext(),myBitstreams[0])
                                             
                                #            try:
				#	        print "DELETE "+myBitstreams[0].getName()
                                 #               bitstreamService = ContentServiceFactory.getInstance().getBitstreamService()
                                            
                                  #              bitstreamService.delete(Curator.curationContext(),myBitstreams[0])
                                   #         except ValueError:
                                    #            print "ERROR en item "+dso.getHandle()
                                 #  print "ESBORRO BUNDLE"
                                 #  dso.itemService.removeBundle(Curator.curationContext(),dso,myBundles[0])
                return 0
 
        def performId(self, context, id):
                print "perform on id %s" % (id)
                return 0
