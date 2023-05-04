#The following defines one object, oldprint:
oldprint= print # make this normal print

def print(count = False, reset = False, stats = False): 
    """This version of print adds two features, for counting and statistics.
    
To use the counting feature, call print with a "count=True" argument.
The counter has several operating modes:
 - If no "counter" variable is passed-in, a default counter is used.
 - Otherwise, counter must be a list containing only an integer.
 - Also, to reset the conter back to 0, pass in "reset=True".
   Furthermore, if the only argument is "reset=True", nothing prints.

To use the statistics feature, call print with a "stats=True" argument.
In this case, no other arguments are allowed. It will display:
 - How many times print has been called (since importing this version).
 - How many times a counter was printed.
 - How many times a counter was reset.
 - How many times statistics were printed (including the current one)."""

    #The following line use a mutable function argument with a default value
    #(see lecture 7's discussion of this concept). But there is something
    #special about the name of this argument: it should get an unusual name,
    #because users aren't meant to ever use this argument when doing prints.
    #Now what is the purpose of this mutable argument? It keeps track of the
    #four statistics numbers that print if the user runs print(stats=True).
    #
    _______  #Adds 1 to the number that counts how often print was called:
    
    
    if ____________:
       raise(ValueError,"The counter must be a list containing one integer.")
    if stats:
        if __________________:
            raise(SyntaxError(
             "When printing statistics, you can't include other arguments."))
        __________ # Adds 1 to statistic of how often statistics were printed
        __________ # Prints the 4 statistice numbers
        return

    if reset:
        ______  # Add 1 to the reset statistic.
        ______  # Reset the counter. It is a mutable default-valued argument.
        if ______: return #Checks if nothing was passed-in to actually print.

    if count==False: return oldprint(________)

    ______  # Add 1 to the statistic of how many times a counter was printed.
    ______  # Add 1 to the counter.
    
    #The following makes the separator a ", "--unless the user passes-in sep:
    if ________
    else: ________

    oldprint(_______) #Prints the counter, along with its parentheses.
    oldprint(_______) #Prints the arguments the user passed in for printing.
