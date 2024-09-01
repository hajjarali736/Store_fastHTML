# Author: Ali Zaghlan El Hajjar
# Description: This script uses the JokeAPI to asynchronously fetch a joke from specified categories.
# The joke is fetched in a "twopart" format, which includes a setup and a delivery.
# Blacklisted categories are excluded from the joke selection.

from jokeapi import Jokes  # Import the Jokes class from the jokeapi module
import asyncio  # Import the asyncio module for handling asynchronous operations

# Initialize empty lists for categories and jokes
categories = []
joke = []

# Example lines for joke setup and delivery
first_line = "heheh"
second_line = "hohoho"

# Define an asynchronous function to list a joke


async def list_joke(categories):
    j = await Jokes()  # Initialize the Jokes class asynchronously
    # Fetch a joke based on the specified categories and filters
    joke = await j.get_joke(
        category=categories,  # List of joke categories to include
        # Specify the joke type as 'twopart' (setup and delivery)
        joke_type="twopart",
        blacklist=['nsfw', 'religious', 'political', 'racist',
                   'sexist']  # Blacklist categories to exclude
    )
    # Return the joke setup and delivery as a list
    return [joke["setup"], joke["delivery"]]

# Run the asynchronous function and get the joke
# 'joke' will be a list containing setup and delivery
joke = asyncio.run(list_joke(categories))
