from urllib import request

for poke in range(1, 808):
    
    pkmn = str(poke)
    if len(pkmn) == 1:
        pkmn = '00'+pkmn
    elif len(pkmn) == 2:
        pkmn = '0'+pkmn
    print('Pokemon '+pkmn)    
    img_reg = request.urlopen('https://www.serebii.net/sunmoon/pokemon/'+pkmn+'.png')
    img_shiny = request.urlopen('https://www.serebii.net/Shiny/SM/'+pkmn+'.png')
    reg = open('./shinydex/pkmn-images/'+pkmn+'.png', 'wb')
    shiny = open('./pkmn-images/'+pkmn+'-shiny.png','wb')
    reg.write(img_reg.read())
    shiny.write(img_shiny.read())
    reg.close()
    shiny.close()
