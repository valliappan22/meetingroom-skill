from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking

class Meetingroom(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('meetingroom.intent')
    def handle_meetingroom(self, message):
        meeting_type = message.data.get('roomName')
        if meeting_type is not None:
            self.speak_dialog("i don't know about the",
                              {'type': meeting_type})
            self.doyouwantToRepeat()
        else:
            self.speak_dialog('meetingroom')
            response = self.get_response('meetingroom', num_retries=0)
    @intent_file_handler('repeat.intent')
    def doyouwantToRepeat():
         self.speak_dialog('Do you want me to repeat')
         response = self.get_response('repeat', num_retries=0)
         if response is None:
            self.speak_dialog('Have a nice day')
        if response is not None:
            self.speak_dialog('Have a nice day')

    def stop(self):
    pass

        


def create_skill():
    return Meetingroom()