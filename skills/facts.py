from dataclasses import dataclass

from ai import AI
from randfacts import randfacts

from skills import factory


@dataclass
class FactsSkill():
    name = 'facts_skill'

    def commands(self, command:str):
        return ['tell me a fact','tell me something',"i'm bored"]
  
    def handle_command(self, command:str, ai:AI):
        fact = randfacts.get_fact()
        ai.say(fact)
        return fact


def initialize():
    factory.register('facts_skill', FactsSkill)
 