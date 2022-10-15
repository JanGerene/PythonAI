# PythonAI

An opensource AI Assistant for the Raspberry Pi
**By Kevin McAleer**

---



## Skills framework

The new skills framework is very simple to implement:

1. Create a new python file in the `skills` folder
2. add a new class such as:

``` python
@dataclass
class Insults_skill:
    name = 'insults'
    
    def commands(self, command:str):
        return ['insult me', 'tell me an insult', 'give me an insult', 'roast me']
        
    def handle_command(self, command:str, ai:AI):
       ai.say('you are a worm')

def initialize():
    factory.register('insult_skill', Insult_skill)

```

3. Update the `skills.json` file to include the new skill:

``` json
{
    "plugins": ["skills.goodday", "skills.weather", "skills.facts", "skills.jokes", "skills.calendar", "skills.insult"],
    "skills": [
        {
            "name": "weather_skill"
        },
        {
            "name": "facts_skill"
        },
        {
            "name": "jokes_skill"
        },
        {
            "name": "goodday_skill"
        },
        {
            "name": "calendar_skill"
        },
        {
            "name": "insult_skill"
        }
    ]
}
```

4. Run the `alf.py` Python program
5. The skills factory will load the `skills.json` file and create a new list of skills, including this new Insults skill.
The `commands` function within the skill returns all the words or phrases that the AI will listen for and then handle those requests by running the `handle_command` function.

---

Create an API key (its free) at <home.openweathermap.org>

## On Raspberry Pi

Make sure you have pyaudio and espeak installed:

```bash
sudo apt-get install espeak
sudo apt-get install python-audio 
```
