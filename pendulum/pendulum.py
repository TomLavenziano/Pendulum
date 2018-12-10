import nlp
import sentiment
import assemble


def main(note):
    return note_to_smartnote(note)


def note_to_smartnote(note):
    smart_note = nlp.process(note)

    print(smart_note)
    return smart_note


def testPendulumLoaded():
    return 'Pendulum Loaded'
