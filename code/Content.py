import random

class Content:
    def __init__(self):
        self.tips_link = "https://www.notion.so/naftali10/Work-Breaks-d8623d5316a34621b26f4adef23e4137"
        self.tips = [
            "Keep your shoulder healthy and strong\n"
            "with physiotherapy exercises,\n"
            "to reduce the risk of another dislocation.",

            "\n"
            "Go down the stairs a few floors and back up,\n"
            "for some cardio activity.",

            "\n"
            "Stretch your muscles:\n"
            "Front leg, back arm, chest, and more.",

            "\n"
            "Warm up your joints, to lubricate tissues\n"
            "and reduce stiffness of the body.",

            "Apply focused pressure using a tennis ball to points in your\n"
            "neck, chest, shoulder blades, below the arm pits.\n"
            "Breath into it for a minute or two, until the pain is gone.",

            "Practice yoga by doing\n"
            "The Worlds Greatest Stretch, Front Growing Stretch,\n"
            "and Small Bridge.",

            "Perform strength workout to get in shape:\n"
            "lift weights with front arm, swing weights with shoulders,\n"
            "do squats and push ups.",

            "\n"
            "Listen to music that you love,\n"
            "and dance if it feels right.",

            "\n"
            "Play the guitar and sing along.\n"
            "Enjoy your voice in the world.",

            "\n"
            "Socialize with friends, family,\n"
            "team members, and other colleagues"
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
            "Time to re-oil the machine in you, and increase productivity.",
            "Time for self-care, to have more satisfaction from this day."
        ]

    def randomize_motivation(self) -> str:
        return random.choice(self.motivations)

    def randomize_tip(self) -> str:
        return random.choice(self.tips)
