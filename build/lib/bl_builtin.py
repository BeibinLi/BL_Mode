import builtins, time, os


print( "Beibin Mode Loaded" )


#%% Defint the global constant
HOME_DIR = os.path.expanduser( "~" )
LOG_DIR = os.path.join( HOME_DIR, "bl_log" )
if not os.path.exists( LOG_DIR ): os.mkdir( LOG_DIR )

OUT = open( os.path.join( LOG_DIR, time.ctime() + ".log")  , "w" )



#%% Override the print function
def print( *args, **kwargs ):
    """
    print with Python's default "print" function.
    Then, save the messages into "~/bl_log/xxx.log" files, where "xxx" represent the time when this module is loaded.

    """
    builtins.print( "In BL Print function" )
    builtins.print( *args, **kwargs )
    builtins.print( *args, **kwargs, file = OUT, flush = True )





#if __name__ != "__main__":
#    builtins.print( "In BL NOT Main" )
#
#    if 'bl_overriden' not in __builtins__:
#    # or not __builtins__[ 'bl_overriden' ]:
#        "We haven't overriden the built-in functions yet"
#        __builtins__[ 'print' ] = print
#        __builtins__[ 'bl_overriden' ] = True


