from EscapeRoom import EscapeRoom
import string
import random

class Vorhof(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Dennis", __name__)
        self.add_level(self.create_level1())



###LEVELS###

    def create_level1(self):
        runen = ["hcid enffö mases"]
        task_messages = [
            "<img src = 'static/tower.png' width='400' height='500' />",
            "Vor dir erstreckt sich ein mysteriöser und alt aussehender Turm in die Höhe. Du hast das Gefühl, hineingehen "
            "zu müssen. Eine unsichtbare Kraft zieht dich hinein zum Turm hin... ",
            "Du entscheidest dich der Kraft nachzugeben und du suchst den Eingang",
            "Auf der Rückseite ist sie.. die Tür.",
            "<img src = 'static/tower_door.png' width = '400' height = '500' />",
            "Als du näher kommst, erscheinen auf einmal Buchstaben rund um die "
            "alte Holztür. Du weißt, dass du hinein musst und versuchst sie zu öffnen. "
            "Wie vermutet, lässt sie sich aber kein Stück bewegen... ",
        ]

        hints = [
            f"den Spruch 'sprich Freund und tritt ein' kennst du irgendwoher.. aber was haben denn die Wörter {runen} "
            f"darunter zu bedeuten? Ist das eventuell"
            f" elbisch oder klingonisch? Das wäre echt nerdig.. schalte mal einen Gang RÜCKWÄRTS! "
        ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sprich_freund,
                "data": runen}

### SOLUTIONS ###

    def sprich_freund(self, runen):
        password = ""
        password += runen[::-1]
        return password



