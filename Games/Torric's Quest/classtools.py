# AttrDisplay code taken from "learning Python" book by Mark Lutz
class AttrDisplay:
    """
    Provides aninheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itsself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """

    def __repr__(self):

        def gatherAttrs(self):
            attrs = []
            for key in sorted(self.__dict__):
                attrs.append('%s=%s' % (key,getattr(self,key)))
            return ', '.join(attrs)


        return '[%s: %s]' % (self.__class__.__name__, gatherAttrs(self))