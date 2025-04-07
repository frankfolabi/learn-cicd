from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Success is not in what you have, but who you are.",
    "Your time is limited, don’t waste it living someone else’s life.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t wait for opportunity. Create it.",
    "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
    "The key to success is to focus on goals, not obstacles.",
    "Believe you can and you’re halfway there.",
    "Act as if what you do makes a difference. It does.",
    "Success is not how high you have climbed, but how you make a positive difference to the world.",
    "Work hard in silence, let your success be the noise.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "Start where you are. Use what you have. Do what you can.",
    "Doubt kills more dreams than failure ever will.",
    "If it doesn’t challenge you, it won’t change you.",
    "Opportunities don't happen. You create them.",
    "Don't watch the clock; do what it does. Keep going.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "It always seems impossible until it’s done.",
    "Strive not to be a success, but rather to be of value.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "You miss 100% of the shots you don’t take.",
    "If you are not willing to risk the usual, you will have to settle for the ordinary.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream it. Wish it. Do it.",
    "Don’t limit your challenges. Challenge your limits.",
    "Great minds discuss ideas; average minds discuss events; small minds discuss people.",
    "I never dreamed about success. I worked for it.",
    "Work until your idols become your rivals.",
    "You don’t have to be great to start, but you have to start to be great.",
    "The only place where success comes before work is in the dictionary.",
    "There are no shortcuts to any place worth going.",
    "Motivation is what gets you started. Habit is what keeps you going.",
    "If you can dream it, you can do it.",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "Discipline is doing what needs to be done, even if you don’t want to do it.",
    "Make each day your masterpiece.",
    "Turn your wounds into wisdom.",
    "Do the hard jobs first. The easy jobs will take care of themselves.",
    "Your passion is waiting for your courage to catch up.",
    "Magic is believing in yourself. If you can make that happen, you can make anything happen.",
    "If something is important enough, even if the odds are against you, you should still do it.",
    "Go the extra mile. It’s never crowded there.",
    "Be so good they can’t ignore you.",
    "Sometimes you win, sometimes you learn.",
    "Don’t tell people your plans. Show them your results.",
    "If you get tired, learn to rest, not quit.",
    "Difficult roads often lead to beautiful destinations.",
    "Stay positive. Work hard. Make it happen.",
    "Don’t quit. Suffer now and live the rest of your life as a champion.",
    "Success is the sum of small efforts repeated day in and day out.",
    "You are never too old to set another goal or to dream a new dream.",
    "Nothing worth having comes easy.",
    "Today is your opportunity to build the tomorrow you want.",
    "Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway.",
    "Learn as if you will live forever, live like you will die tomorrow.",
    "When you feel like quitting, think about why you started.",
    "Be the change that you wish to see in the world.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "A person who never made a mistake never tried anything new.",
    "Start each day with a positive thought and a grateful heart.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
    "If you don’t like the road you’re walking, start paving another one.",
    "Perseverance is not a long race; it is many short races one after the other.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Great things never come from comfort zones.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "You only fail when you stop trying.",
    "The secret of getting ahead is getting started.",
    "Don’t be afraid to give up the good to go for the great.",
    "Success is a journey, not a destination.",
    "Sometimes later becomes never. Do it now.",
    "Try not to become a person of success, but rather try to become a person of value.",
    "Don’t let yesterday take up too much of today.",
    "If you change the way you look at things, the things you look at change.",
    "You don’t need to see the whole staircase, just take the first step.",
    "Hustle in silence and let your success make the noise.",
    "The future depends on what you do today.",
    "The expert in anything was once a beginner.",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful.",
    "Action is the foundational key to all success.",
    "You are capable of amazing things.",
    "Work hard, stay positive, and get up early. It’s the best part of the day.",
    "Don’t count the days, make the days count.",
    "A goal without a plan is just a wish.",
    "Doubt is a killer. You just have to know who you are and what you stand for.",
    "Failure is not the opposite of success; it’s part of success.",
    "Do not wait for the perfect time and place to enter, for you are already onstage.",
    "Success begins with self-discipline.",
    "You didn’t come this far only to come this far.",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
