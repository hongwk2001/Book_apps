import json
import os

path = r'c:\git_repo\Book_apps\frankenstein\src\main\assets\books\ch_14.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_en = [
    "Chapter 10",
    "I spent the next day wandering through the valley. I stood beside the source of the Arveiron, which begins in a glacier. That glacier was slowly advancing down from the hilltop to block the valley.",
    "The steep slopes of massive mountains were laid out before me, and the ice wall of the glacier towered above me. A few shattered pine trees were scattered around, and the solemn silence of this magnificent, majestic hall of nature was broken only by the roaring rapids, the sound of huge ice fragments falling, and the thunderous roar of avalanches. Or it was only the echo of the glacier, cracking and tearing as if it were a toy in giant hands, resounding throughout the mountains as unchanging laws silently worked.",
    "These sublime and majestic scenes gave me the greatest comfort. They elevated me from petty feelings, and although they did not completely eliminate my sadness, they calmed it down. They also provided some relief from the painful thoughts that had weighed heavily on my mind for a month.",
    "When I went to bed at night, the giant shapes of nature that I had gazed at during the day filled my surroundings, allowing me to sleep comfortably as if they were protecting and comforting me. The mountain peaks covered in clean snow, the dazzling summits, the dense pine forests, the rough and desolate canyons, and even the eagles soaring through the clouds—all these things seemed to gather around me and offer deep peace to my heart.",
    "When I woke up the next morning, where had they flown off to? Everything that breathed vitality into my soul had fled with sleep, and a dark depression cast storm clouds over every thought. It rained pouring down, and thick fog obscured the mountain peaks so that I could not even see the faces of those giant friends.",
    "Nevertheless, I wanted to pierce that veil of fog and seek them out in their cloud-covered hideouts. What did a rainstorm matter to me? My mule was brought to the door, and I decided to climb to the top of Montanvert.",
    "I remembered the effect that the first sight of that massive, constantly moving glacier had brought to my mind. It had filled me with a sublime ecstasy that gave my soul wings to soar from the dark world into light and joy.",
    "Seeing an awe-inspiring and majestic sight in nature truly always had the effect of making my mind solemn and helping me forget the worries of a fleeting life. I decided to go without a guide. Because I knew the way well, and having someone else along would destroy the solitary grandeur of the scenery.",
    "The climb is steep, but the path constantly winds in short turns, making it possible to overcome the mountain's verticality. It is a terrifyingly desolate landscape.",
    "In thousands of places, traces of winter avalanches can be found, with trees lying broken on the ground, some completely destroyed, and others bent, leaning against jutting rocks or laid across other trees.",
    "As you climb higher, the path is intersected by snow-covered ravines, and stones constantly roll down from above. One of them is particularly dangerous, because even a very small sound like speaking loudly is enough to cause an air vibration and bring destruction down on the speaker's head. The pine trees are neither tall nor lush, and their dullness adds a harsh atmosphere to the landscape.",
    "I looked down at the valley below my feet. A massive fog rising from the river flowed through the valley, wrapping around the opposite mountains like a thick wreath, and their peaks were obscured by uniform clouds. Meanwhile, rain poured from the dark sky, adding to the gloomy impression I received from the objects around me.",
    "Ah! Why do humans boast of a sensitivity superior to that seen in beasts? It merely makes humans a more inevitable being. If our impulses were limited only to hunger, thirst, and desire, we would be almost free. But now we are swayed by every blowing wind and the chance words or scenes those words might convey to us.",
    "We rest, but a dream has the power to ruin our sleep. We wake up, but a single wandering thought pollutes the day. We feel, imagine, think rationally, and laugh or cry. We embrace deep sorrow or shake off our worries. Whether it is joy or sadness, it makes no difference. The path for it to leave is always open.",
    "Human's yesterday can never be the same as tomorrow. Only the fact that things change will last!",
    "It was nearly noon when I reached the top of the climb. I sat for a while on a rock looking down at the sea of ice. Fog covered both that place and the surrounding mountains.",
    "Presently, a breeze scattered the clouds, and I went down onto the glacier. The surface was very uneven, rising like the waves of a turbulent sea, dipping low, and scattered with deep crevices.",
    "The ice field was almost one league, about 4.8 kilometers, in width, but it took me nearly two hours to cross it. The opposite mountain is a bare vertical rock.",
    "From the side where I was standing now, Montanvert was exactly one league away on the opposite side, and above it, Mont Blanc rose, boasting awe-inspiring majesty. I stayed in a hollow of the rock and gazed at this wondrous and massive landscape.",
    "The sea, or rather the huge river of ice, wound its way through vegetation and through the dependent mountains, whose airy peaks hung over its hollows. Above the clouds, their icy and sparkling peaks shone in the sunlight.",
    "My heart, which had been filled with sorrow before, now swelled with something resembling joy. I shouted, \"Wandering souls, if you are truly wandering without resting in your narrow beds, allow me this faint happiness, or take me as your companion away from the joys of life.\"",
    "When I said this, I suddenly saw the figure of a man in the distance coming toward me at superhuman speed. He was easily jumping over the crevices in the ice that I had walked carefully around. As he got closer, his height also seemed to exceed that of a human.",
    "I became anxious. A fog covered my eyes and a feeling of fainting seized me, but thanks to the cold gale of the mountain, I quickly recovered. As the figure came closer—a truly terrifying and disgusting sight!—I realized it was the monster I had created.",
    "Trembling with anger and fear, I decided to wait for his approach and engage in a life-or-death fight. He came closer. His face showed bitter anguish combined with contempt and malice, and his unearthly ugliness was almost too terrible for human eyes to look at.",
    "But I hardly noticed it. At first, anger and hatred left me speechless, but I soon regained my composure and poured out words full of fierce hatred and contempt upon him.",
    "\"Demon,\" I shouted. \"How dare you approach me? Aren't you afraid of my arm's fierce revenge crashing down on your miserable head? Get lost, you terrible bug!",
    "No, rather stay, so I can trample you into dust! Ah! If only I could bring back the victims you so demonically murdered by ending your miserable life!\"",
    "\"I expected this welcome,\" the demon said. \"All humans hate the miserable. Then how much more must I, the most miserable of all living things, be hated! Yet even you, my creator, despise and try to cast out me, your creation. We are bound by a bond that can only be broken when one of us ceases to exist.",
    "You are trying to kill me. How dare you play with life like this? Do your duty to me. Then I too will do my duty to you and the rest of humanity.",
    "If you agree to my conditions, I will leave them and you in peace. But if you refuse, I will fill the jaws of death until it is satisfied with the blood of your remaining friends.\"",
    "\"Disgusting monster! You demon! Even the torture of hell is too light a revenge for your sins.",
    "Despicable fiend! Do you blame me for your birth? Then come at me. I will extinguish with my own hands the spark that I so negligently granted.\"",
    "My anger was endless. I lunged at him, engulfed in all the emotions one being can harbor to take the life of another.",
    "He easily dodged me and said.",
    "\"Calm down! I beg you to please listen to me before you pour your hatred on this devoted head. Isn't the pain I've suffered enough that you try to add to my misery?",
    "Even if life is merely an accumulation of pain, it is precious to me, and I will protect it. Remember, you made me more powerful than yourself. My height is greater than yours, and my joints are more flexible.",
    "However, I will not fall into the temptation to fight against you. I am your creation, and if you also fulfill your rightful role owed to me, I will be a gentle and obedient being to you, my natural lord and king.",
    "Oh, Frankenstein, why are you fair to everyone else but try to trample only on me? I am the very one who most desperately needs to receive your justice, or rather your generosity and affection. Remember that I am your creation. I should rightfully be your Adam, but instead I am like a fallen angel chased out of joy by you without any fault.",
    "Everywhere you look blessings overflow, but only I am irrevocably excluded from it. I was good and kind, but misery made me a demon. Make me happy. Then I will be a being with virtue once again.\"",
    "\"Get lost! I won't listen to your words. There can be nothing in common between you and me. We are enemies.",
    "Get lost right now, or let's test our strength in a fight where one of us must fall.\"",
    "\"What do I have to do to move your heart? What plea must I make for you to cast a favorable look upon your creation begging for your goodwill and sympathy? Believe me, Frankenstein. I was good. My soul shone with love and humanity. But am I not lonely now? Am I not miserably alone?",
    "Even you, my creator, disgust me, so what hope can I get from your fellow kind who owe me nothing? They despise and hate me. Only the unpopulated mountains and desolate glaciers are my refuge.",
    "I have wandered around here for days. The ice caves, the only things I don't fear, are my only dwelling and the only place humans don't resent. I welcome this bleak sky. It is because it is kinder to me than your fellow kind.",
    "If the majority of humans knew of my existence, they would also arm themselves for my ruin like you do. Then should I not hate those who disgust me? I will make no compromise with my enemies.",
    "I am miserable, and they too will share my misery. But you have the power to compensate me, and the power to save them from that giant disaster lying solely in your hands. If you refuse, the disaster will grow so large that not only you and your family but thousands of other people will be swept up and swallowed by the whirlwind of revenge.",
    "Awaken your sympathy, and do not despise me. Listen to my story. After hearing it all, decide whether to abandon me or pity me according to your judgment. But please listen to me.",
    "No matter how bloody human laws may be, do they not give even those convicted a chance to defend themselves before passing a sentence? Listen to my words, Frankenstein. You accuse me of being a murderer, yet you try to destroy your own creation with a self-satisfied conscience.",
    "Oh, praise that eternal justice of humans! But I am not asking you to spare my life. Listen to my story. Then, if you can, and if you want to, destroy this piece you made with your hands.\"",
    "\"Why do you bring back to my memory the fact that I was the miserable origin and author, the situation that makes me shudder just thinking about it?\" I retorted. \"Cursed day, you disgusting demon, I curse the day you first saw the light!",
    "I curse these hands that created you—even though it means cursing myself! You have made me miserable beyond words. You have left me no room to consider whether I am fair to you or not.",
    "Get lost! Remove your disgusting appearance from my sight.\"",
    "\"I will set you free like this, my creator.\" He said, bringing his loathsome hands before my eyes. I roughly brushed them away. \"I will remove this sight you disgust from you like this. But you can still hear my words, and you can show me sympathy.",
    "In the name of the virtues I once possessed, I demand this of you. Listen to my story. It is a long and strange story, and the temperature here does not suit your delicate senses. Let's go to the hut on the mountain.",
    "The sun is still high in the sky. Before the sun hides behind your snow-covered cliff and goes down to light another world, you will be able to hear all my story and make a decision. Whether I forever leave the dwellings of humans and live a harmless life, or become a disaster to your fellow kind and the culprit bringing your own swift ruin, is up to you.\"",
    "Leaving these words, he took the lead across the ice, and I followed him. My mind was complicated and I did not answer him, but as I walked I weighed the various arguments he put forward and decided to at least listen to his story.",
    "I was driven by curiosity, and sympathy also solidified my decision. I had assumed him to be my younger brother's murderer up until now, so I really wanted to verify whether this opinion was true or not.",
    "Also, for the first time, I felt what the duty to a creation as a creator was, and the thought occurred to me that I should first make him happy before complaining of his evil deeds. These motives urged me to follow his demand.",
    "So we crossed the ice and climbed up the rock on the opposite side. The air was cold, and it started to rain again. We entered the hut. The demon with a triumphant attitude, and I with a heavy heart and a gloomy mood.",
    "But I had agreed to listen, and as I settled down next to the fire lit by this terrible companion, he began his story."
]

for i, item in enumerate(data):
    if i < len(new_en):
        item['en'] = new_en[i]

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Rewrite complete!')
