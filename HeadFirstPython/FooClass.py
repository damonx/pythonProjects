class FooClass(object):
    """my very first class: FooClass"""
    version = 0.1
    def __init__(self, nm='Damon Xu'):
        """constructor"""
        self.name = nm
        print 'Created a class instance for', nm

    def showname(self):
        """display instance attribute and class name"""
        print 'Your name is', self.name
        print 'My class name is',self.__class__.__name__

    def showver(self):
        """display class(static) attribute"""
        print self.version

    def addMe2Me(self, x):
        return x+x