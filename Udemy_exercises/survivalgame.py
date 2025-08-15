print(r'''
            (                 ,&&&.
             )                .,.&&
            (  (              \=__/
                )             ,'-'.
          (    (  ,,      _.__|/ /|
           ) /\ -((------((_|___/ |
         (  // | (`'      ((  `'--|
       _ -.;_/ \\--._      \\ \-._/.
      (_;-// | \ \-'.\    <_,\_\`--'|
      ( `.__ _  ___,')      <_,-'__,'
       `'(_ )_)(_)_)'
''')
print("Welcome at your Basecamp.\n")
print("Everything is fine until u hear a scream in the woods. ")
print("Your mission is to escape this Scenario.\n")

choice1 = input('The scream is coming from the deep wood around you. It seem\'s to come from the left one. So you decided '
                'to pack your stuff and run the opposite direction. After a few meters the path split in left and right. '
                'Type "left" or "right":').lower()

if choice1 == "left":
    choice2 = input('You run and run.. the path is going to be better and better. Not an dirty way anymore, now its a stoned '
                    'way. After a long run you stand breathless in front of an old cabin in the woods. No one seems to be home. '
                    'Maybe you cant hide in there till the morning? Type "hide" or "running":').lower()
    if choice2 == "running":
        choice3 = input('You are very exhausted but you run and run and run. In the shining moonlight you see an old wooden '
                        'bridge that build over a floating river. Type "cross" or "swim" or "detour:').lower()
        if choice3 == "cross":
            print("The wooden planks creaks under your shows after every step. One breaks but u can jump over the hole. "
                  "After the Bridge you can see the village outside the forest. You have done it!\n You win!")
        elif choice3 == "swim":
            print("You jump in the river. The water feels like an Iceberg that crushed into your body. It's so cold and "
                  "strong, that you were pulled you immediately. You drowned there.\n Game over")
        elif choice3 == "detour":
            print("You try to found another way across the river. After 1 hour of run you cant take any more steps. "
                  "You have to rest. Some wolves smells you and decided to eating you.\n Game over")
    if choice2 == "hide":
        print("The door opened surprising easily. You entered the cabin and blocked the door with a heavy wooden "
              "desk which you found in this room. After a few minutes, after you recovered your breath a little, you discovered the room. "
              "What you found are many tools like saws, hammers and a lot of blood and skulls in the corner. "
              "At this moment the door bangs and splattered. A man with a dead body in his hand entered the "
              "cabin and you passed out.\n Game over.")
elif choice1 == "right":
    print("you turned right. You can't see anything in the dark. At once u don't have any ground on your foot and you fall. "
          "You feeling the pain at the ground and you realize, that is not an hole. That is a Grave. \n Game over.")
