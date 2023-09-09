import random

class Content:
    def __init__(self):
        self.tips_link = "https://www.notion.so/naftali10/Work-Breaks-d8623d5316a34621b26f4adef23e4137"
        self.tips = [
            "Keep your shoulder healthy and strong with physiotherapy exercises, "
            "to reduce the risk of another dislocation.",

            "Go down the stairs a few floors and back up, "
            "for some cardio activity.",

            "Stretch your muscles: front leg, back arm, chest, and more.",

            "Warm up your joints, to lubricate tissues and reduce stiffness of the body.",

            "Apply focused pressure using a tennis ball to points in your "
            "neck, chest, shoulder blades, below the arm pits. "
            "Breath into it for a minute or two, until the pain is gone.",

            "Practice yoga by doing "
            "The Worlds Greatest Stretch, Front Growing Stretch, and Small Bridge.",

            "Perform strength workout to get in shape: "
            "lift weights with front arm, swing weights with shoulders, do squats and push ups.",

            "Listen to music that you love, and dance if it feels right.",

            "Play the guitar",

            "Socialize with friends, family, team members and other colleagues"
        ]
        self.motivations = [
            "Time for a context switch to zoom out and get new perspective.",
            "Time to be in motion and improve life expectancy and quality.",
            "Time for a fresh approach and perspective on issues.",
            "Time to recharge body and mind with positive energy.",
            "Time to prevent burnout and reduce stress.",
            "Time to step away and come back fresh.",
            "Time to reset and make mindful choices for the rest of the day.",
            "Time for a mini-vacation, because work is not the goal of life.",
            "Time to re-oil the machine in you, and increase productivity",
            "Time for self-care, to have more satisfaction from this day"
        ]

    def randomize_motivation(self) -> str:
        return random.choice(self.motivations)

    def randomize_tip(self) -> str:
        return random.choice(self.tips)
