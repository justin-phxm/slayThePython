import random

 ##FLOORS###
 ###Floor 1: Battie
 ###Floor 2: Louse
 ###Floor 3: Nemesis **ELITE**
 ###Floor 4: Lagavulin
 ###Floor 5: Gremlin Horde
 ###Floor 6: Hexaghost **Elite**
 ###Floor 7: Byrd x 3
 ###Floor 8: Spiker
 ###Floor 9: Timekeeper **Elite**
 ###Floor 10: Reptomancer
 #######

class Battie:
  '''The first and most basic enemy, the Battie.'''
  def __init__(self, health = random.randrange(10,13,2), attack = 1, defense = 0):
      self.health = health
      self.attack = attack
      self.defense = defense

  def greet(self):
    print('SCREEE! ' * 7)

  def img(self):
    print(r"""
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
""")
  def name(self):
    return('Battie')
  
  # def turn(self):
  #           user.health = user.health - (enemy1.attack - user.defense)
  #           print(f'The {enemy1.name()} has attacked you for {enemy1.attack - user.defense} damage!')
  #           print(f'You have {user.health} health remaining!')
  #           print()
  #           pass    


class Louse:
  def __init__(self, health = 14, attack = random.randint(2,4), defense = 1):
      self.health = health
      self.attack = attack
      self.defense = defense

  def greet(self):
    print('*sniffle* ' * 2)
  
  def img(self):
    print(r"""
             ,.-----__    
          ,:::://///,:::-. 
         /:''/////// ``:::`;/|/
        /'   ||||||     :://'`\
      .' ,   ||||||     `/(  e \
-===~__-'\__X_`````\_____/~`-._ `.
            ~~        ~~       `~-'
""")
  def name(self):
    return('Louse')


class Nemesis:
  def __init__(self, health = 2, attack = 2, defense = 5):
      self.health = health
      self.attack = attack
      self.defense = defense
      
  def name(self):
    return('Koopa Troopa')

  def greet(self):
    print('Why are you still here... ')

  def img(self):
    print(r"""
                             ___-------___
                         _-~~             ~~-_
                      _-~                    /~-_
   /^\__/^\         /~  \                   /    \
 /|  O|| O|        /      \_______________/        \
| |___||__|      /       /                \          \
|          \    /      /                    \          \
|   (_______) /______/                        \_________ \
|         / /         \                      /            \
 \         \^\\         \                  /               \     /
   \         ||           \______________/      _-_       //\__//
     \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
       ~-----||====/~     |==================|       |/~~~~~
        (_(__/  ./     /                    \_\      \.
               (_(___/                         \_____)_)
""")

class Lagavulin:
  def __init__(self, health = 10, attack = 1, defense = 0):
      self.health = health
      self.attack = attack
      self.defense = defense

  def greet(self):
    print('ZZZZ' * 7)

  def name(self):
    return ('Lagavulin')

  def img(self):
    print(r"""
          .--.         .--.
              \       /        
       |\      `\___/'       /|
        \\    .-'@ @`-.     //  
        ||  .'_________`.  ||
         \\.'^    Y    ^`.//
         .'       |       `.
        :         |         :
       :          |          :
       :          |          :
       :     _    |    _     :
       :.   (_)   |   (_)    :
     __::.        |          :__
    /.--::.       |         :--.\
 __//'   `::.     |       .'   `\\___
`--'     //`::.   |     .'\\     `--'
         ||  `-.__|__.-'   || 
         ||                ||
         //                \\
        |/                  \|
""")


class Mad_Gremlin:
  def __init__(self, health = 10, attack = 1, defense = 0):
      self.health = health
      self.attack = attack
      self.defense = defense

  def greet(self):
    print('Get him boys!!')

  def name(self):
    return ('Mad Gremlin')

  def img(self):
    print(r"""
           "=.
          "=. \
             \ \
          _,-=\/=._        _.-,_
         /         \      /=-._ "-.
        |=-./~\___/~\    /     `-._\
        |   \o/   \o/   /         /
         \_   `~~~;/    |         |
           `~,._,-'    /          /
              | |      =-._      /
          _,-=/ \=-._     /|`-._/
        //           \\   )\
       /|             |)_.'/
      //|             |\_."   _.-\
     (|  \           /    _.`=    \
     ||   ":_    _.;"_.-;"   _.-=.:
  _-."/    / `-."\_."        =-_.;\
 `-_./   /             _.-=.    / \\
        |              =-_.;\ ."   \\
        \                   \\/     \\
        /\_                .'\\      \\
       //  `=_         _.-"   \\      \\
      //      `~-.=`"`'       ||      ||
      ||    _.-_/|            ||      |\_.-_
  _.-_/|   /_.-._/            |\_.-_  \_.-._\
 /_.-._/                      \_.-._\
""")

class Gremlin:
  def __init__(self, health = 10, attack = 1, defense = 0):
      self.health = health
      self.attack = attack
      self.defense = defense

  def name(self):
    return ('Gremlin')

  def img(self):
    print(r"""
                                              ^             
                                             / \           ^
                       _,-~~~--~~~--._      (   \         / \
                   _,-'               `.__  (    \_.---._/   )
                 ,'                       `-(_` -'       `-. )   
                /       "--..                \.'           `/  
               ,             `-.              :  _  .-.  _  : 
              /                 ;             : (0).oYo.(0) ;
            /                    `             \.-'V'"'V'-./
           /                     '              \\^     ^//
  /\      /                      '     :    : .-'\\^   ^//
 ;  \    ;   /                  ,'  _.-`.    `. : \\^_^//
 ;   \   ;  ;`.               ,'~~-'     `.    `.`.`-.-'
  \   |_/   ;  `.        /-'/___.---.      `-.   `.`---.
   \       /     |      /____.---.)))         `-. `---.\
    \_____/      (____________))))\\\            `-.\\\\
                               \\\\
                               """)


class Hexaghost:
  def __init__(self, health = 10, attack = 1, defense = 0):
      self.health = health
      self.attack = attack
      self.defense = defense
 
  def greet(self):
    print('BZZ BZZ' * 3)

  def name(self):
    return ('Hexaghost')

  def img(self):
    print(r"""
   _________________         _         _         _________________
  /:::::::::::::::::\__     / ^       ^ \     __/:::::::::::::::::\
 /:::::::________::::::\_   I           I   _/::::::________:::::::\
/:::::::/        \__:::::\_  \_       _/  _/:::::__/        \:::::::\
\_:::::I    ####    \__::::\   \     /   /::::__/    ####    I ::::_/
  \:::::\__     ####   \__::\   \   /   /::__/   ####     __/:::::/
   \___::::\__     #####  \::\   \_/   /::/  #####     __/::::___/
       \::::::\___    ###  \::\  @ @  /::/  ###    ___/ :::::/
        \___::::::\__   ##  \::\ I_I /::/  ##   __/::::::___/
            \::::::::\_   #  I:I / \ I:I  #   _/::::::::/
             \__:::::::\__   I:I H H I:I   __/:::::::__/
                \____:::::\__I:I H H I:I__/:::::____/
                     \_:::::::/  \ /  \:::::::_/
                    /::\_____/:I / \ I:\_____/::\
                   /::::/   I::I H H I::I  \:::::\
                  /::::/  # I::I H H I::I # \:::::\
                 I::::/  ## /::/ \ / \::\ ##  \::::I
                 I:::/   # /::I   V   I::\ #   \:::I
                 I:::\_   /:::/        \::\   _/:::I
                  \::::\_/:::/          \::\_/::::/
                   \::::::::/            \:::::::/
                    \______/              \_____/
""")

class Byrd:
  def __init__(self, health = 10, attack = 2, defense = 1):
    self.health = health
    self.attack = attack
    self.defense = defense

  def greet(self):
    print('CawCaww!!')

  def img(self):
    print(r"""
     _\|      __     |/_
   _-  \_   _/"->   _/  -_
   -_    `-'(   )`-'    _-
    `=.__.=-(   )-=.__.='
            |/-\|
            Y   Y
""")

  def name(self):
    return ('Byrd')

class Spiker:
  def __init__(self, health = 10, attack = 1, defense = 0):
      self.health = health
      self.attack = attack
      self.defense = defense

  def name(self):
    return ('Spiker')

  def greet(self):
    print('Blub, blub, blob')

  def img(self):
    print(r"""
                          .
                          A       ;
                |   ,--,-/ \---,-/|  ,
               _|\,'. /|      /|   `/|-.
           \`.'    /|      ,            `;.
          ,'\   A     A         A   A _ /| `.;
        ,/  _              A       _  / _   /|  ;
       /\  / \   ,  ,           A  /    /     `/|
      /_| | _ \         ,     ,             ,/  \
     // | |/ `.\  ,-      ,       ,   ,/ ,/      \/
     / @| |@  / /'   \  \      ,              >  /|    ,--.
    |\_/   \_/ /      |  |           ,  ,/        \  ./' __:..
    |  __ __  |       |  | .--.  ,         >  >   |-'   /     `
  ,/| /  '  \ |       |  |     \      ,           |    /
 /  |<--.__,->|       |  | .    `.        >  >    /   (
/_,' \\  ^  /  \     /  /   `.    >--            /^\   |
      \\___/    \   /  /      \__'     \   \   \/   \  |
       `.   |/          ,  ,                  /`\    \  )
         \  '  |/    ,       V    \          /        `-\
          `|/  '  V      V           \    \.'            \_
           '`-.       V       V        \./'\
               `|/-.      \ /   \ /,---`\         
                /   `._____V_____V'
                           '     '
""")

class Time_Eater:
  def __init__(self, health = 10, attack = 1, defense = 0):
      self.health = health
      self.attack = attack
      self.defense = defense

  def name(self):
    return ('Time Eater')

  def greet(self):
    print('Wanna know how to keep an idiot busy for hours?')

  def img(self):
    print(r"""
     /^\    /^\
    {  O}  {  O}
     \ /    \ /
     //     //       _------_
    //     //     ./~        ~-_
   / ~----~/     /              \
 /         :   ./       _---_    ~-
|  \________) :       /~     ~\   |
|        /    |      |  :~~\  |   |
|       |     |      |  \___-~    |
|        \ __/`^\______\.        ./
 \                     ~-______-~\.
 .|                                ~-_
/_____________________________________~~____
""")


class Reptomancer:
  def __init__(self, health = 10, attack = 1, defense = 0):
      self.health = health
      self.attack = attack
      self.defense = defense

  def name(self):
    return ('Reptomancer')

  def greet(self):
    print('SCREEE! ' * 7)

  def img(self):
    print(r"""
           /^\/^\
         _|__|  O|
\/     /~     \_/ \
 \____|__________/  \
        \_______      \
                `\     \                 \
                  |     |                  \
                 /      /                    \
                /     /                       \\
              /      /                         \ \
             /     /                            \  \
           /     /             _----_            \   \
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
""")



class Sword:
  def img(self):
    print(r"""
     /\
    // \
    || |
    || |
    || |
    || |
    || |
    || |
 __ || | __
/___||_|___\
     ww
     MM
    _MM_
   (&<>&)
    ~~~~
    """)




# class Chesire:
#   def img(self):
#     print(r"""
#            .'\   /`.
#          .'.-.`-'.-.`.
#     ..._:   .-. .-.   :_...
#   .'    '-.(o ) (o ).-'    `.
#  :  _    _ _`~(_)~`_ _    _  :
# :  /:   ' .-=_   _=-. `   ;\  :
# :   :|-.._  '     `  _..-|:   :
#  :   `:| |`:-:-.-:-:'| |:'   :
#   `.   `.| | | | | | |.'   .'
#     `.   `-:_| | |_:-'   .'
#       `-._   ````    _.-'
#           ``-------''
# """)




# class Maw:
#   def img(self):
#     print(r"""
#   /|  |\            /|  |\
#   /|  |\            /|  |\
#  / |  | \          / |  | \
#  | |  | |          | |  | |
#  \  \/  /  __  __  \  \/  /
#   \    /  / /  \ \  \    /
#    \  /   \ \__/ /   \  /
#    \  /   /      \   \  /
#   _ \ \__/ O    O \__/ / _
#   \\ \___          ___/ //
# _  \\___/  ______  \___//  _
# \\  ----(          )----  //
#  \\_____( ________ )_____//
#   ~-----(          )-----~ _
#    _____( ________ )_____  \\
#   /,----(          )----  _//
#  //     (  ______  )     /  \
#  ~       \        /      \  /
#           \  __  /       / /
#            \    /       / /
#             \   \      / /
#              \   ~----~ /
#               \________/
# """)

# class Bison:
#   def img(self):
#     print(r"""

#                                     ___,,___
#                                 ,d8888888888b,_
#                             _,d889'        8888b,
#                         _,d8888'          8888888b,
#                     _,d8889'           888888888888b,_
#                 _,d8889'             888888889'688888, /b
#             _,d8889'               88888889'     `6888d 6,_
#          ,d88886'              _d888889'           ,8d  b888b,  d\
#        ,d889'888,             d8889'               8d   9888888Y  )
#      ,d889'   `88,          ,d88'                 d8    `,88aa88 9
#     d889'      `88,        ,88'                   `8b     )88a88'
#    d88'         `88       ,88                   88 `8b,_ d888888
#   d89            88,      88                  d888b  `88`_  8888
#   88             88b      88                 d888888 8: (6`) 88')
#   88             8888b,   88                d888aaa8888, `   'Y'
#   88b          ,888888888888                 `d88aa `88888b ,d8
#   `88b       ,88886 `88888888                 d88a  d8a88` `8/
#    `q8b    ,88'`888  `888'"`88          d8b  d8888,` 88/ 9)_6
#      88  ,88"   `88  88p    `88        d88888888888bd8( Z~/
#      88b 8p      88 68'      `88      88888888' `688889`
#      `88 8        `8 8,       `88    888 `8888,   `qp'
#        8 8,        `q 8b       `88  88"    `888b
#        q8 8b        "888        `8888'
#         "888                     `q88b
#                                   "888'
# """