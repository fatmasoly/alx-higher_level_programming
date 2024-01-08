 #!/usr/bin/python3
 
 
 def lookup(obj):
      """
    Returns a list of attributes and methods of the given object.

    Parameters:
    - obj: Any Python object
        The object for which the attributes and methods will be looked up.

    Returns:
    - list
        A list containing the names of attributes and
        methods of the given object.
        """
        return dir(obj)