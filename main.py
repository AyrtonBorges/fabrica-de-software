import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
attributes_container = []

with open('venv/teste.csv', 'w', encoding='utf-8') as entrada_file:
    # Using TwitterSearchScraper to scrape data and append tweets to list
    entrada = sntwitter.TwitterSearchScraper('Bitcoin since:2022-05-22 until:2022-11-30').get_items()
    template = 'Username;Displayname;ID;Descrição\n'
    entrada_file.write(template)
    for i, tweet in enumerate(entrada):
        if i > 10:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.url, tweet.content])
        teste = sntwitter.TwitterUserScraper(tweet.user.username)._get_entity()
        temp = teste.username+";"+teste.displayname+';'+str(teste.id)+';'+teste.description.replace('\n',' ')+';'+'\n'
        entrada_file.write(temp)
        print(teste.username,teste.id,teste.displayname) # Faz printar o username, o id da pessoa e o nome de de faixada do perfil dela
    entrada_file.close()
