from org.dspace.curate import ScriptedTask
from org.dspace.curate import Curator
from org.dspace.content.service import DSpaceObjectService
from org.dspace.content.factory import ContentServiceFactory
import subprocess
import os.path
import shutil
#from org.dspace.content.service import BitstreamService

class Enoenmediaserver(ScriptedTask):
        def init(self, curator, taskName):
                print "initializing with Jython"

        def performDso(self, dso):
                #print "perform on dso "
                if dso.getType()==2:
                        #print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
                        myBundles = dso.itemService.getBundles(dso,"MEDIA_DOCUMENT")
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
                                        #print path
                                        more=["cat",path]
                                        p2 = subprocess.Popen(more, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                                        out, err2 = p2.communicate()
                                        directori="/projectes/calaix/mediaserver/"+out[43:]
					directori=directori.rsplit('<', 1)[0]
					fitxermediaserver=directori+"document_1.jpg"
					print directori
					if os.path.exists(fitxermediaserver)== False:
					    #os.rmdir(directori)
					    print "ESBORRO fitxer"+myBitstreams[0].getName()
                                            bitstreamService = ContentServiceFactory.getInstance().getBitstreamService()
                                            bitstreamService.delete(Curator.curationContext(),myBitstreams[0])
                                        if len(myBitstreams)==0:
                                            print "ESBORRO BUNDLE"
                                            dso.itemService.removeBundle(Curator.curationContext(),dso,i)
					    print "ESBORRO PATH mediaserver"
                                            #os.rmdir(directori)
                                            try:
                                                if os.path.exists(directori):
                                                    shutil.rmtree(directori)   
                                            except IOError, e:
                                                print "Error no es pot esborrar pq no hi es"
					    
                                        #size=["sed", "-i","s/(http:\/\/media-server.csuc.cat/http:\/\/media-server.csuc.cat/g",path]
                                        #p = subprocess.Popen(size, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                                        #wout, err = p.communicate()
                                        #print wout
                                        #more2=["cat",path]
                                        #p3 = subprocess.Popen(more2, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                                        #out2, err3 = p3.communicate()
                                        #print out2
#print path
                return 0

        def performId(self, context, id):
                print "perform on id %s" % (id)
                return 0
