from jokeapi import Jokes # Import the Jokes class
import asyncio

categories = []
joke = []
first_line = "heheh"
second_line = "hohoho"

async def list_joke(categories):
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(category=categories,
                            joke_type="twopart",
                            blacklist=['nsfw', 'religious', 'political', 'racist', 'sexist'],
                            
                            ) 
    return [joke["setup"] ,joke["delivery"]]
    
    
#joke is a list that contain setup and delivery
joke = asyncio.run(list_joke(categories)) 