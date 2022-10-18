from pytube import YouTube
link = input('Link do video: ')
yt = YouTube(link)
result = {

    'title': yt.title,
    'views': yt.views,
    'duration': yt.length,
    'avaliating': yt.rating,
    
}

print(f"Nome do video: {result['title']}")
minutos = result['duration'] / 60
minutos2 = round(minutos, 2)
print(f"Duração: {minutos} minutos")

yr = yt.streams.get_highest_resolution()
print('Video baixando...')

yr.download('C:\\Users\\andre\\Downloads')
print('Video baixado com sucesso!')