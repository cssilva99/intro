def calculate_music_in_seconds(durationminutes, durationseconds):
    convert_minutes_to_seconds = durationminutes/60
    totaltime = convert_minutes_to_seconds + durationseconds
    totalHora = int(totaltime // 3600)
    totalMin = int((totalHora % 3600) // 60)
    totalSeg = int(totalMin % 60)
    return totalHora, totalMin, totalSeg