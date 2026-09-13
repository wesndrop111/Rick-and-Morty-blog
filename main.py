from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def blog():
    return "Привет,мой блог будет о Рике и Морти и моих впечатлениях после просмотра всех существующих на данный момент сезонов. <br> Особая благодарность Kodland и преподователю которые научили меня создавать сайты,на этих сайтах могли бы быть гифки но пока к сожалению не умею их делать на сайтах. <br> Я просмотрел все серии Рика и Морти и мне очень понравилось потому что есть классные персоонажи,классные приключения,и есть перерывы между сюжетом и просто приключениями. <br> Хоть мультфильм если его так можно назвать начал выходить уже давно,но он до сих пор выходит,в этом году вышел новый сезон!В первых сезонах сюжета обычно мало но в последующих его становилось больше!Ещё прелесть например Рика как персоонажа что в одной серии он уничтожает планеты и вселенный, а в другой получает люлей от обычной гориллы и так далее. <br> Мои Впечатления о Мультсериале очень положительные,хоть он и для взрослых. <br> <br> Hello, my blog will be about Rick and Morty and my impressions after watching all the seasons that exist at the moment. <br> Special thanks to Kodland and the teacher who taught me how to create websites, these websites could have GIFs, but unfortunately, I don't know how to add them to websites yet. <br> I watched all the episodes of Rick and Morty and I really liked it because there are cool characters, cool adventures, and there are breaks between the main plot and just random adventures. <br> Even though the cartoon, if you can call it that, started coming out a long time ago, it's still running, and a new season came out this year! In the first seasons, there is usually little plot, but in the subsequent ones, there was more and more of it! Another charm of Rick as a character, for example, is that in one episode he destroys planets and universes, and in another, he gets his butt kicked by a regular gorilla and so on. <br> My impressions of the animated series are very positive, even though it is for adults."



app.run(debug=True)
