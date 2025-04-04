# Escrever um programa que calcule a duração total (no formato hh:mm:ss) de um album musical com 5 músicas
# O utilizador devrá informar a duração de cada musica em minutos e segundos

iterate_list_with_duration = []

def calculate_music_in_hours(duration):
    convert_seconds_to_hours = duration/3600
    return convert_seconds_to_hours

count = 0

while count <5 :    
    musicduration = float(input("Digite a duração da música em segundos : "))    
    duration = calculate_music_in_hours(musicduration)
    iterate_list_with_duration.append(duration)
    count = count + 1

total_album_duration = 0

def iterate_list_with_duration(iterate_list_with_duration):
    for i in range(len(iterate_list_with_duration)):
        total_album_duration = iterate_list_with_duration[i]
    return total_album_duration

album_duration = iterate_list_with_duration