class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + '__' + name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass
