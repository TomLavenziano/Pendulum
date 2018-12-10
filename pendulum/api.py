"""Microservice API for taking converting Notes to Smart Notes"""
import os
import hug
import pendulum

def build_smartnote(note):
    return pendulum.note_to_smartnote(note)

@hug.get(note='This is a GET test note')
@hug.post(note='test')
@hug.local()
def SmartNote(note: hug.types.text):
    """Convert Note to Smart Note"""
    smart_note = build_smartnote(note)
    return {
            'note': '{0}'.format(note),
            'smartNote': smart_note
            }


if __name__ == '__main__':
    os.system('hug -f {0}'.format(__file__))
