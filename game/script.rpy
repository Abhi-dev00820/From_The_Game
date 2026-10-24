
define h = Character("Hyunsang", color="#c8ffc8")
define m = Character("Mikasa", color="#c8c8ff")
define r = Character("Rangiku", color="#c8c8ff")
define k = Character("Mom", color="#c8c8ff")


label start:

    scene inside house hyun
    with fade

    show hyunsang

    "The story is set in Tokyo, Japan, in 2026."

    "Hyunsang is an 18-year-old high school student who loves playing games. His childhood friend, Mikasa, means a lot to him."

    "Hyunsang lives with his divorced mother, who runs a business in Kyoto and often travels there for work. During those trips, Mikasa keeps him company."

    "The story revolves around the supernatural experiences of Hyunsang and Mikasa. Can they stay safe, or will they get drawn into something darker?"

    h "Mom, I'm going to school!"

    k "Okay, Hyun. Get there safely!"

    scene bus stop
    with dissolve

    h "It's taking forever for the bus to arrive."

    scene bus
    show hyunsang at left

    h "Finally! Here we go."

    scene school
    with dissolve

    "(After reaching school...)"

    scene classroom
    show hyunsang at left

    h "Where the hell is Mikasa? She's late again!"

    show mikasa at right

    m "I'm here, Hyunsang! Sorry for being late."

    menu:
        "Be angry":
            h "I don't even want to talk to you right now."

        "Be polite":
            h "Mikasa, please be punctual. At least try to arrive on time, okay?"

    h "Anyway, come on. Sit here. Sensei is about to arrive."

    scene mikasaandhyun
    with fade

    "(After class...)"

    menu:
        "Ask Mikasa to come to your home":
            scene mid area hs
            show hyunsang at left
            show mikasa at right

            h "Mikasa! Are you free tonight? Let's spend some time together. Mom is going to Kyoto for work."

            m "Umm... yeah, sure! I'll be there. Just don't get too busy gaming, alright?"

            h "As you wish! See you this evening at my place."

        "Don't ask Mikasa":
            scene mid area hs
            show hyunsang at left
            show mikasa at right

            h "Well, I'll see you later, Mikasa."

            m "Okay, I'm heading home. See you!"

    scene bye
    with dissolve

    h "Bye, Mikasa! See you later!"

    m "B-byeee!"

    return
