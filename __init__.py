from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking

class Meetingroom(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('meetingroom.intent')
    def handle_meetingroom(self, message):
        meeting_type = message.data.get('roomName')
        if meeting_type is not None:
            self.speak_dialog("i_don't_know_about_the",
                              {'type': meeting_type})
            response = self.ask_yesno('Do_you_want_me_to_repeat')
            if response == 'yes':
                self.speak_dialog("i_don't_know_about_the",
                              {'type': meeting_type})
                self.speak_dialog('Have_a_nice_day')

        else:
            self.speak_dialog('meetingroom')
            response = self.get_response('meetingroom', num_retries=0)

    def stop(self):
    pass

        


def create_skill():
    return Meetingroom()