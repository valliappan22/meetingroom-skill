from mycroft import MycroftSkill, intent_file_handler


class Meetingroom(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('meetingroom.intent')
    def handle_meetingroom(self, message):
        self.speak_dialog('meetingroom')


def create_skill():
    return Meetingroom()

