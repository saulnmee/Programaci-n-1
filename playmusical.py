print ("Playlist Musical")
playlist_musical = ["Bohemian Rhapsody","Hotel California","Stanway to Heaven"]

playlist_musical.append("Inmortal-Alejo")

index= playlist_musical.index("Hotel California")
playlist_musical[index]="Shape of you"

playlist_musical.insert(0,"Watermelon Sugar")

playlist_musical.pop()

print("Lista final de canciones:",playlist_musical)
print("Cantidad de canciones:",len(playlist_musical))
