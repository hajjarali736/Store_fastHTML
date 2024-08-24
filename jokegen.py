from jokeapi import Jokes # Import the Jokes class
import asyncio


def listing(t):
    k = ""
    for i in t:
        k+=i 
        k+= "\n"
    return t

async def tuple_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(category=['Dark'])  # Retrieve a random joke
    if joke["type"] == "single": # Print the joke
        return (joke["joke"])
    else:
        return(joke["setup"] ,joke["delivery"])
    
    
    
joke = asyncio.run(tuple_joke())


print(listing(joke))