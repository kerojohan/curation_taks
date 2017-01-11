from org.dspace.curate import ScriptedTask
from org.dspace.curate import Curator
from org.dspace.content.service import DSpaceObjectService
from org.dspace.content.factory import ContentServiceFactory

#from org.dspace.content.service import BitstreamService
 
class Main(ScriptedTask):
    def init(self, curator, taskName):
        print "initializing with Jython"
 
    def performDso(self, dso):
        #print "perform on dso "
        if dso.getType()==2:
            print "Item '" + dso.getName() + "' ("+dso.getHandle()+")"
            col= dso.getOwningCollection().getName()
            dso.itemService.addMetadata(Curator.curationContext(),dso , "dc", "relation", "ispartofseries", dso.ANY, col);
        return 0
        
    def performId(self, context, id):
        print "perform on id %s" % (id)
        return 0
