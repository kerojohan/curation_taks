from org.dspace.curate import ScriptedTask
from org.dspace.curate import Curator
from org.dspace.content.service import DSpaceObjectService
from org.dspace.content.factory import ContentServiceFactory
from PIL import Image
#from org.dspace.content.service import BitstreamService
 
class Main(ScriptedTask):
        def init(self, curator, taskName):
                print "initializing with Jython"
 
        def performDso(self, dso):
                #print "perform on dso "
                if dso.getType()==2:
                        print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
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
                                        try:
                                            with open(path) as file:
                                                print path
                                                
                                                im = Image.open(path)
                                                print 'width: %d - height: %d' % im.size
                                            except IOError as e:
                                                pass


#print path
                return 0
 
        def performId(self, context, id):
                print "perform on id %s" % (id)
                return 0
