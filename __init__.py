# from mycroft import MycroftSkill, intent_file_handler

# class Meetingroom(MycroftSkill):
#     def __init__(self):
#         super().__init__()

#     @intent_file_handler('meetingroom.intent')
#     def handle_meetingroom(self, message):
#         self.speak_dialog('Have_a_nice_day')
#         meeting_type = message.data.get('roomName')
#         if meeting_type is not None:
#             self.speak_dialog("i_don't_know_about_the",
#                               {'type': meeting_type})
#         #     response = self.ask_yesno('Do_you_want_me_to_repeat')
#         #     if response == 'yes':
#         #         self.speak_dialog("i_don't_know_about_the",
#         #                       {'type': meeting_type})
#         #         self.speak_dialog('Have_a_nice_day')

#         # else:
#         #     self.speak_dialog('meetingroom')
#         #     response = self.get_response('meetingroom', num_retries=0)

#     def stop(self):
#     pass

        


# def create_skill():
#     return Meetingroom()

from mycroft import MycroftSkill, intent_file_handler

class TomatoSkill(MycroftSkill):
    def __init__(self):
        super().__init__()

    @intent_handler('what.is.a.tomato.intent')
    def handle_what_is(self, message):
        self.speak_dialog('tomato.description')

    # @intent_handler('do.you.like.intent')
    # def handle_do_you_like(self, message):
    #     tomato_type = message.data.get('type')
    #     if tomato_type is not None:
    #         self.speak_dialog('like.tomato.type',
    #                           {'type': tomato_type})
    #     else:
    #         self.speak_dialog('like.tomato.generic')

    def stop(self):
        pass

def create_skill():
    return TomatoSkill()