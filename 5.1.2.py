import winsound


def song():
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }
    notes = "500-sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol"
    notes = notes.split(',')
    for note_duration in notes:
        duration, note = note_duration.split('-')
        frequency = freqs[note]
        duration = int(duration)
        winsound.Beep(frequency, duration)


song()
