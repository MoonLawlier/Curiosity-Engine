
import random

ideas = ["Explore the night sky with a telescope,",
         "Build a model rocket and launch it,",
         "Create a star chart to identify constellations,",
         "Visit a planetarium or observatory,",
         "Make a DIY sundial to track the sun's movement,",
         "Design a space-themed board game,",
         "Write a story about an intergalactic adventure,",
         "Create a scrapbook of space missions and discoveries,"]

inspiration = ["Like spotify","inspired by Netflix","as seen on YouTube","featured in National Geographic",
               "recommended by TED Talks","highlighted in Scientific American","endorsed by NASA",
               "celebrated by SpaceX","promoted by ESA","supported by JAXA"]

constraints = ["but without screen!","using only text!","No pics alllowed!","with a time limit of 30 minutes!",
               "using recycled materials!","with a budget of $10!","in a group of 3!","while listening to classical music!",
               "with your non-dominant hand!","while blindfolded!","that works offline!","using only items found in nature!"]

print(f"{random.choice(ideas)} {random.choice(inspiration)}, {random.choice(constraints)}")
