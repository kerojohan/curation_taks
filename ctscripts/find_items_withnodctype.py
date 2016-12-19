from org.dspace.curate import ScriptedTask
from org.dspace.curate import Curator
from org.dspace.content.service import DSpaceObjectService
from org.dspace.content.factory import ContentServiceFactory
import subprocess

#from org.dspace.content.service import BitstreamService

class Fnotype(ScriptedTask):
        def init(self, curator, taskName):
                print "initializing with Jython"

        def performDso(self, dso):
                #print "perform on dso "
                if dso.getType()==2:
                      #  print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
                        mytypes = dso.itemService.getMetadata(dso, "dc", "type", None, dso.ANY);
                        totaltypes = len(mytypes)
                        if totaltypes == 0:
                            print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
			#for i in myBundles:
                        #    print i.getValue()
                               




#print path
                return 0

        def performId(self, context, id):
                print "perform on id %s" % (id)
                return 0
