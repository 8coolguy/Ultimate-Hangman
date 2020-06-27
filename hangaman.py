import pygame 
import ctypes
from PyDictionary import PyDictionary
from random import randint

user = ctypes.windll.user32
dictionary =PyDictionary()


#make the panel
X =user.GetSystemMetrics(0)
Y=user.GetSystemMetrics(1)
Black =(0,0,0)
r =int(X/20)
White =(255,255,255)
under_distance =int((X-r)-(X/4+2*r))
class main:
    @staticmethod
    def draw_MenuScreen(panel,pygame):
        pygame.draw.line(panel,White,(int(X*.5/5),int(Y*2.5/3)),(int(X/5)-r,int(Y*2.5/3)),2)#standBase
        pygame.draw.line(panel,White,(int((X*.5/5+int(X/5)-r)/2),int(Y*2.5/3)),(int((X*.5/5+int(X/5)-r)/2),int(Y/7)),2)#stand 
        pygame.draw.line(panel,White,(int((X*.5/5+int(X/5)-r)/2),int(Y/7)),(int(X/4),int(Y/7)),2)#standArm
        pygame.draw.line(panel,White,(int(X/4),int(Y/7)),(int(X/4),int(Y/4)-r),2)#standArm2

        pygame.draw.circle(panel,White,(int(X/4),int(Y/4)),r)#outer circle face
        pygame.draw.circle(panel,Black,(int(X/4),int(Y/4)),r-2)#inner cicle
        pygame.draw.line(panel,White,(int(X/4),int(Y/4)+r),(int(X/4),int(Y*1.7/3)),2) #body
        pygame.draw.line(panel,White,(int(X/4),int(Y*1.7/3)),(int(X/4)+r,int(Y*2.5/3)),2) #Right Leg
        pygame.draw.line(panel,White,(int(X/4),int(Y*1.7/3)),(int(X/4)-r,int(Y*2.5/3)),2) #lefty leg 
        pygame.draw.line(panel,White,(int(X/4)+r,int(Y*.9/2)),(int(X/4)-r,int(Y*.9/2)),2) #arms
        
        
        pygame.draw.line(panel,White,(int(X/4)-r/2,int(Y/4)-r/2),(int(X/4)-r/2,int(Y/4)+r/2),2)#left eye
        pygame.draw.line(panel,White,(int(X/4)+r/2,int(Y/4)-r/2),(int(X/4)+r/2,int(Y/4)+r/2),2)#right eyes
        
        pygame.draw.line(panel,White,(int(X/4)-r/4,int(Y/4)+r/2),(int(X/4)+r/4,int(Y/4)+r/2),2)#face               
    @staticmethod
    def draw_EasyHangMan(panel,pygame,errors):
        #stand
        pygame.draw.line(panel,White,(int(X*.5/5),int(Y*2.5/3)),(int(X/5)-r,int(Y*2.5/3)),2)#standBase
        pygame.draw.line(panel,White,(int((X*.5/5+int(X/5)-r)/2),int(Y*2.5/3)),(int((X*.5/5+int(X/5)-r)/2),int(Y/7)),2)#stand 
        pygame.draw.line(panel,White,(int((X*.5/5+int(X/5)-r)/2),int(Y/7)),(int(X/4),int(Y/7)),2)#standArm
        pygame.draw.line(panel,White,(int(X/4),int(Y/7)),(int(X/4),int(Y/4)-r),2)#standArm2
        if(errors>0):
            pygame.draw.circle(panel,White,(int(X/4),int(Y/4)),r)#outer circle face
            pygame.draw.circle(panel,Black,(int(X/4),int(Y/4)),r-2)#inner cicle
        if(errors>1):
            pygame.draw.line(panel,White,(int(X/4),int(Y/4)+r),(int(X/4),int(Y*1.7/3)),2) #body
        if(errors>2):
            pygame.draw.line(panel,White,(int(X/4)+r,int(Y*.9/2)),(int(X/4)-r,int(Y*.9/2)),2) #arms
        if(errors>3):
            pygame.draw.line(panel,White,(int(X/4),int(Y*1.7/3)),(int(X/4)-r,int(Y*2.5/3)),2) #lefty leg
        if(errors>4):
            pygame.draw.line(panel,White,(int(X/4),int(Y*1.7/3)),(int(X/4)+r,int(Y*2.5/3)),2) #Right Leg
        if(errors>5):
            pygame.draw.line(panel,White,(int(X/4)-r/2,int(Y/4)-r/2),(int(X/4)-r/2,int(Y/4)+r/2),2)#left eye
        if(errors>6):
            pygame.draw.line(panel,White,(int(X/4)+r/2,int(Y/4)-r/2),(int(X/4)+r/2,int(Y/4)+r/2),2)#right eyes
        if(errors>7):
            pygame.draw.line(panel,White,(int(X/4)-r/4,int(Y/4)+r/2),(int(X/4)+r/4,int(Y/4)+r/2),2)#face          
    @staticmethod   
    def draw_MediumHangMan(panel,pygame,errors):
        #stand
        pygame.draw.line(panel,White,(int(X*.5/5),int(Y*2.5/3)),(int(X/5)-r,int(Y*2.5/3)),2)#standBase
        pygame.draw.line(panel,White,(int((X*.5/5+int(X/5)-r)/2),int(Y*2.5/3)),(int((X*.5/5+int(X/5)-r)/2),int(Y/7)),2)#stand 
        pygame.draw.line(panel,White,(int((X*.5/5+int(X/5)-r)/2),int(Y/7)),(int(X/4),int(Y/7)),2)#standArm
        pygame.draw.line(panel,White,(int(X/4),int(Y/7)),(int(X/4),int(Y/4)-r),2)#standArm2
        if(errors >0):
            pygame.draw.circle(panel,White,(int(X/4),int(Y/4)),r)#outer circle face
            pygame.draw.circle(panel,Black,(int(X/4),int(Y/4)),r-2)#inner cicle
        if(errors >1):
            pygame.draw.line(panel,White,(int(X/4),int(Y/4)+r),(int(X/4),int(Y*1.7/3)),2) #body
        if(errors>2):
            pygame.draw.line(panel,White,(int(X/4)+r,int(Y*.9/2)),(int(X/4)-r,int(Y*.9/2)),2) #arms
        if(errors>3):
            pygame.draw.line(panel,White,(int(X/4),int(Y*1.7/3)),(int(X/4)-r,int(Y*2.5/3)),2) #lefty leg
        if(errors>4):
            pygame.draw.line(panel,White,(int(X/4),int(Y*1.7/3)),(int(X/4)+r,int(Y*2.5/3)),2) #Right Leg
        if(errors>5):
            pygame.draw.line(panel,White,(int(X/4)-r/2,int(Y/4)-r/2),(int(X/4)-r/2,int(Y/4)+r/2),2)#left eye
            pygame.draw.line(panel,White,(int(X/4)+r/2,int(Y/4)-r/2),(int(X/4)+r/2,int(Y/4)+r/2),2)#right eyes
        if(errors>6):
            pygame.draw.line(panel,White,(int(X/4)-r/4,int(Y/4)+r/2),(int(X/4)+r/4,int(Y/4)+r/2),2)#face
        if(errors>7):
            print('You Lose')
    @staticmethod 
    def draw_HardHangMan(panel,pygame,errors):
        #stand
        pygame.draw.line(panel,White,(int(X*.5/5),int(Y*2.5/3)),(int(X/5)-r,int(Y*2.5/3)),2)#standBase
        pygame.draw.line(panel,White,(int((X*.5/5+int(X/5)-r)/2),int(Y*2.5/3)),(int((X*.5/5+int(X/5)-r)/2),int(Y/7)),2)#stand 
        pygame.draw.line(panel,White,(int((X*.5/5+int(X/5)-r)/2),int(Y/7)),(int(X/4),int(Y/7)),2)#standArm
        pygame.draw.line(panel,White,(int(X/4),int(Y/7)),(int(X/4),int(Y/4)-r),2)#standArm2
        if(errors > 0):
            pygame.draw.circle(panel,White,(int(X/4),int(Y/4)),r)#outer circle face
            pygame.draw.circle(panel,Black,(int(X/4),int(Y/4)),r-2)#inner cicle
        if(errors >1):
            pygame.draw.line(panel,White,(int(X/4),int(Y/4)+r),(int(X/4),int(Y*1.7/3)),2) #body
        if(errors>2):
            pygame.draw.line(panel,White,(int(X/4)+r,int(Y*.9/2)),(int(X/4)-r,int(Y*.9/2)),2) #arms
        if(errors>3):
            pygame.draw.line(panel,White,(int(X/4),int(Y*1.7/3)),(int(X/4)-r,int(Y*2.5/3)),2) #lefty leg
            pygame.draw.line(panel,White,(int(X/4),int(Y*1.7/3)),(int(X/4)+r,int(Y*2.5/3)),2) #Right Leg
        if(errors>4):
            pygame.draw.line(panel,White,(int(X/4)-r/2,int(Y/4)-r/2),(int(X/4)-r/2,int(Y/4)+r/2),2)#left eye
            pygame.draw.line(panel,White,(int(X/4)+r/2,int(Y/4)-r/2),(int(X/4)+r/2,int(Y/4)+r/2),2)#right eyes
        if(errors>5):
            pygame.draw.line(panel,White,(int(X/4)-r/4,int(Y/4)+r/2),(int(X/4)+r/4,int(Y/4)+r/2),2)#face
        if(errors>6):
            print('You Lose')        
    def draw_text(text,font,color,screen,x,y):
        textobj =font.render(text, 1, color)
        textrect =textobj.get_rect()
        textrect.center =(x,y)
        screen.blit(textobj,textrect)
    def draw_bottom_text(text,font,color,screen,x,y):
        textobj =font.render(text, 1, color)
        textrect =textobj.get_rect()
        textrect.midbottom=(x,y)
        screen.blit(textobj,textrect)
    def draw_right_text(text,font,color,screen,x,y):
        textobj =font.render(text, 1, color)
        textrect =textobj.get_rect()
        textrect.midleft=(x,y)
        screen.blit(textobj,textrect)    
    def find_word(difficulty):
        if(difficulty=='easy'):
            dif_range =3500
        elif(difficulty =='hard'):
            dif_range =7500
        elif(difficulty =='medium'):
            dif_range =19500
        finding =True 
        reader =open('20kwords.txt','r') 
        words =reader.read().splitlines()
        while(finding):
            word =words[randint(0,dif_range)]	
            if str(PyDictionary().meaning(word)) == None:
                continue
            if len(word)>3:
                finding =False
                reader.close()
                return(word)
    def easy_hangman():
        pygame.init()
        pygame.event.pump()
        panel = pygame.display.set_mode([X,Y])
        pygame.display.set_caption("Easy Mode")
        gameRun =True
        errors=0
        score =0
        while gameRun:
            #choose a word and display the definitio with underlines for the amount of letters there are
            word =main.find_word('easy')
            print(word)
            skipSpace =int(under_distance/(1.25*len(word)))
            unders = int((4/5)*skipSpace)
            defSpace =int((X/2)/len(str(PyDictionary().meaning(word))))*4
            main.draw_right_text(str(PyDictionary().meaning(word)),pygame.font.SysFont(None,defSpace),White,panel,0,int(Y/10))
            for letter in range(len(word)):
                pygame.draw.line(panel, White,(int(letter*skipSpace+X/4+2*r),int(Y/3)),(int(letter*skipSpace+X/4+2*r+unders),int(Y/3)),2)
            correctGuess =[False for letter in range(len(word))]
            guessing=True 
            while guessing:
                main.draw_EasyHangMan(panel,pygame,errors)
                #event for loop
                for event in pygame.event.get():
                    if event.type ==pygame.QUIT:
                        gameRun=False
                        guessing=False
                    if  pygame.key.get_pressed()[pygame.K_a]:
                        if 'a' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'a' ==word[letter]:
                                    x.append(letter)                                    
                            for letter in x:
                                main.draw_bottom_text('a',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_b]:
                        if 'b' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'b' ==word[letter]:
                                    x.append(letter)
                            for letter in x:
                                main.draw_bottom_text('b',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_c]:
                        if 'c' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'c' ==word[letter]:
                                    x.append(letter)                                    
                            for letter in x:
                                main.draw_bottom_text('c',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_d]:
                        if 'd' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'd' ==word[letter]:
                                    x.append(letter)                                    
                            for letter in x:
                                main.draw_bottom_text('d',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_e]:
                        if 'e' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'e' ==word[letter]:
                                    x.append(letter)
                            for letter in x:
                                main.draw_bottom_text('e',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_f]:
                        if 'f' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'f' ==word[letter]:
                                    x.append(letter)

                            for letter in x:
                                main.draw_bottom_text('f',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_g]:
                        if 'g' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'g' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('g',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_h]:
                        if 'h' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'h' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('h',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_i]:
                        if 'i' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'i' ==word[letter]:
                                    x.append(letter)
                                   
                            for letter in x:
                                main.draw_bottom_text('i',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_j]:
                        if 'j' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'j' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('j',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                    
                    if  pygame.key.get_pressed()[pygame.K_k]:
                        if 'k' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'k' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('k',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                        
                    if  pygame.key.get_pressed()[pygame.K_l]:
                        if 'l' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'l' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('l',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_m]:
                        if 'm' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'm' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('m',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                    
                    if  pygame.key.get_pressed()[pygame.K_n]:
                        if 'n' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'n' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('n',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_o]:
                        if 'o' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'o' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('o',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_p]:
                        if 'p' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'p' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('p',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_q]:
                        if 'q' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'q' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('q',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                
                    if  pygame.key.get_pressed()[pygame.K_r]:
                        if 'r' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'r' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('r',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                            
                    if  pygame.key.get_pressed()[pygame.K_s]:
                        if 's' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if's' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('s',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter]=True
                                
                        else:
                            errors = errors+1
                            
                    if  pygame.key.get_pressed()[pygame.K_t]:
                        if 't' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if't' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('t',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1        
               
                    if  pygame.key.get_pressed()[pygame.K_u]:
                        if 'u' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'u' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('u',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1       
                            
                    if  pygame.key.get_pressed()[pygame.K_v]:
                        if 'v' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'v' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('v',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1  
                            
                    if  pygame.key.get_pressed()[pygame.K_w]:
                        if 'w' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'w' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('w',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_x]:
                        if 'x' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'x' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('x',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                
                    if  pygame.key.get_pressed()[pygame.K_y]:
                        if 'y' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'y' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('y',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1        
                    
                    if  pygame.key.get_pressed()[pygame.K_z]:
                        if 'z' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'z' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('z',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                pygame.display.update()
                pygame.time.delay(10)
                if not(False in correctGuess):
                    score =score+1
                    main.draw_text(word,pygame.font.SysFont(None,70),White,panel,int(X/2),int(Y/2)) 
                    pygame.display.update()
                    pygame.time.delay(10)
                    guessing =False
                if errors ==9:
                    nextScreen =True
                    while nextScreen:
                        main.draw_text(word,pygame.font.SysFont(None,70),White,panel,int(X/2),int(Y/2))
                        next_button=pygame.Rect(0,0,180,70)
                        next_button.center =int(3*X/4),int(Y*4/5)
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if mouse[1]<int(Y*4/5)+35 and mouse[1]> int(Y*4/5)-35 and mouse[0]>int(3*X/4)-90 and mouse[0]<int(3*X/4)+90:
                            pygame.draw.rect(panel,(128,128,128),next_button)
                            if click[0] ==1:
                                guessing =False
                                main.score_board(score)
                                nextScreen =False
                                gameRun =False
                        else:pygame.draw.rect(panel,Black,next_button)
                        main.draw_text("Next",pygame.font.SysFont(None,70),White,panel,int(3*X/4),int(Y*4/5))
                        pygame.display.update()
                        pygame.time.delay(10)
                        #event for loop
                        for event in pygame.event.get():
                            if event.type ==pygame.QUIT:
                                nextScreen =False            
            pygame.time.delay(1000)                    
            panel.fill((0,0,0))
        pygame.quit()
    def score_board(score):
        pygame.init()
        panel = pygame.display.set_mode([X,Y])
        pygame.display.set_caption("Score")
        scored =True
        while scored:
            main.draw_text(str(score*100),pygame.font.SysFont(None,70),White,panel,int(X/2),int(Y/2))
            try_button=pygame.Rect(0,0,180,70)
            try_button.center =int(3*X/4),int(Y*4/5)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if mouse[1]<int(Y*4/5)+35 and mouse[1]> int(Y*4/5)-35 and mouse[0]>int(3*X/4)-90 and mouse[0]<int(3*X/4)+90:
                pygame.draw.rect(panel,(128,128,128),try_button)
                if click[0] ==1:
                    main.menu()                                                    
            else:pygame.draw.rect(panel,Black,try_button)
            main.draw_text("Try Again",pygame.font.SysFont(None,70),White,panel,int(3*X/4),int(Y*4/5))
            pygame.display.update()
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    scored =False
        pygame.quit()
    def medium_hangman():
        pygame.init()
        pygame.event.pump()
        panel = pygame.display.set_mode([X,Y])
        pygame.display.set_caption("Medium Mode")
        gameRun =True
        errors=0
        score =0
        while gameRun:
            #choose a word and display the definitio with underlines for the amount of letters there are
            word =main.find_word('medium')
            print(word)
            skipSpace =int(under_distance/(1.25*len(word)))
            unders = int((4/5)*skipSpace)
            defSpace =int((X/2)/len(str(PyDictionary().meaning(word))))*4
            main.draw_right_text(str(PyDictionary().meaning(word)),pygame.font.SysFont(None,defSpace),White,panel,0,int(Y/10))
            for letter in range(len(word)):
                pygame.draw.line(panel, White,(int(letter*skipSpace+X/4+2*r),int(Y/3)),(int(letter*skipSpace+X/4+2*r+unders),int(Y/3)),2)
            correctGuess =[False for letter in range(len(word))]
            guessing=True 
            while guessing:
                main.draw_MediumHangMan(panel,pygame,errors)
                #event for loop
                for event in pygame.event.get():
                    if event.type ==pygame.QUIT:
                        gameRun=False
                        guessing=False
                    if  pygame.key.get_pressed()[pygame.K_a]:
                        if 'a' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'a' ==word[letter]:
                                    x.append(letter)                                    
                            for letter in x:
                                main.draw_bottom_text('a',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_b]:
                        if 'b' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'b' ==word[letter]:
                                    x.append(letter)
                            for letter in x:
                                main.draw_bottom_text('b',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_c]:
                        if 'c' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'c' ==word[letter]:
                                    x.append(letter)                                    
                            for letter in x:
                                main.draw_bottom_text('c',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_d]:
                        if 'd' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'd' ==word[letter]:
                                    x.append(letter)                                    
                            for letter in x:
                                main.draw_bottom_text('d',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_e]:
                        if 'e' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'e' ==word[letter]:
                                    x.append(letter)
                            for letter in x:
                                main.draw_bottom_text('e',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_f]:
                        if 'f' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'f' ==word[letter]:
                                    x.append(letter)

                            for letter in x:
                                main.draw_bottom_text('f',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_g]:
                        if 'g' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'g' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('g',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_h]:
                        if 'h' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'h' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('h',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_i]:
                        if 'i' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'i' ==word[letter]:
                                    x.append(letter)
                                   
                            for letter in x:
                                main.draw_bottom_text('i',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_j]:
                        if 'j' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'j' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('j',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                    
                    if  pygame.key.get_pressed()[pygame.K_k]:
                        if 'k' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'k' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('k',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                        
                    if  pygame.key.get_pressed()[pygame.K_l]:
                        if 'l' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'l' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('l',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_m]:
                        if 'm' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'm' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('m',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                    
                    if  pygame.key.get_pressed()[pygame.K_n]:
                        if 'n' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'n' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('n',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_o]:
                        if 'o' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'o' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('o',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_p]:
                        if 'p' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'p' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('p',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_q]:
                        if 'q' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'q' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('q',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                
                    if  pygame.key.get_pressed()[pygame.K_r]:
                        if 'r' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'r' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('r',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                            
                    if  pygame.key.get_pressed()[pygame.K_s]:
                        if 's' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if's' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('s',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter]=True
                                
                        else:
                            errors = errors+1
                            
                    if  pygame.key.get_pressed()[pygame.K_t]:
                        if 't' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if't' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('t',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1        
               
                    if  pygame.key.get_pressed()[pygame.K_u]:
                        if 'u' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'u' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('u',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1       
                            
                    if  pygame.key.get_pressed()[pygame.K_v]:
                        if 'v' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'v' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('v',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1  
                            
                    if  pygame.key.get_pressed()[pygame.K_w]:
                        if 'w' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'w' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('w',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_x]:
                        if 'x' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'x' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('x',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                
                    if  pygame.key.get_pressed()[pygame.K_y]:
                        if 'y' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'y' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('y',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1        
                    
                    if  pygame.key.get_pressed()[pygame.K_z]:
                        if 'z' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'z' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('z',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                pygame.display.update()
                pygame.time.delay(10)
                if  not (False in correctGuess) :
                    score =score+1
                    main.draw_text(word,pygame.font.SysFont(None,70),White,panel,int(X/2),int(Y/2)) 
                    pygame.display.update()
                    pygame.time.delay(10)
                    guessing =False
                if errors ==8:
                    nextScreen =True
                    while nextScreen:
                        main.draw_text(word,pygame.font.SysFont(None,70),White,panel,int(X/2),int(Y/2))
                        next_button=pygame.Rect(0,0,180,70)
                        next_button.center =int(3*X/4),int(Y*4/5)
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if mouse[1]<int(Y*4/5)+35 and mouse[1]> int(Y*4/5)-35 and mouse[0]>int(3*X/4)-90 and mouse[0]<int(3*X/4)+90:
                            pygame.draw.rect(panel,(128,128,128),next_button)
                            if click[0] ==1:
                                guessing =False
                                main.score_board(score*3)
                                nextScreen =False
                                gameRun =False
                        else:pygame.draw.rect(panel,Black,next_button)
                        main.draw_text("Next",pygame.font.SysFont(None,70),White,panel,int(3*X/4),int(Y*4/5))
                        pygame.display.update()
                        pygame.time.delay(10)
                        #event for loop
                        for event in pygame.event.get():
                            if event.type ==pygame.QUIT:
                                nextScreen =False
            
            pygame.time.delay(1000)                    
            panel.fill((0,0,0))
        pygame.quit()
    def hard_hangman():
        pygame.init()
        pygame.event.pump()
        panel = pygame.display.set_mode([X,Y])
        pygame.display.set_caption("Hard Mode")
        gameRun =True
        errors=0
        score =0
        while gameRun:
            #choose a word and display the definitio with underlines for the amount of letters there are
            word =main.find_word('hard')
            print(word)
            skipSpace =int(under_distance/(1.25*len(word)))
            unders = int((4/5)*skipSpace)
            defSpace =int((X/2)/len(str(PyDictionary().meaning(word))))*4
            main.draw_right_text(str(PyDictionary().meaning(word)),pygame.font.SysFont(None,defSpace),White,panel,0,int(Y/10))
            for letter in range(len(word)):
                pygame.draw.line(panel, White,(int(letter*skipSpace+X/4+2*r),int(Y/3)),(int(letter*skipSpace+X/4+2*r+unders),int(Y/3)),2)
            correctGuess =[False for letter in range(len(word))]
            guessing=True 
            while guessing:
                main.draw_MediumHangMan(panel,pygame,errors)
                #event for loop
                for event in pygame.event.get():
                    if event.type ==pygame.QUIT:
                        gameRun=False
                        guessing=False
                    if  pygame.key.get_pressed()[pygame.K_a]:
                        if 'a' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'a' ==word[letter]:
                                    x.append(letter)                                    
                            for letter in x:
                                main.draw_bottom_text('a',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_b]:
                        if 'b' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'b' ==word[letter]:
                                    x.append(letter)
                            for letter in x:
                                main.draw_bottom_text('b',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_c]:
                        if 'c' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'c' ==word[letter]:
                                    x.append(letter)                                    
                            for letter in x:
                                main.draw_bottom_text('c',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_d]:
                        if 'd' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'd' ==word[letter]:
                                    x.append(letter)                                    
                            for letter in x:
                                main.draw_bottom_text('d',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_e]:
                        if 'e' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'e' ==word[letter]:
                                    x.append(letter)
                            for letter in x:
                                main.draw_bottom_text('e',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_f]:
                        if 'f' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'f' ==word[letter]:
                                    x.append(letter)

                            for letter in x:
                                main.draw_bottom_text('f',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_g]:
                        if 'g' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'g' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('g',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_h]:
                        if 'h' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'h' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('h',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_i]:
                        if 'i' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'i' ==word[letter]:
                                    x.append(letter)
                                   
                            for letter in x:
                                main.draw_bottom_text('i',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_j]:
                        if 'j' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'j' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('j',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                    
                    if  pygame.key.get_pressed()[pygame.K_k]:
                        if 'k' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'k' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('k',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                        
                    if  pygame.key.get_pressed()[pygame.K_l]:
                        if 'l' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'l' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('l',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_m]:
                        if 'm' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'm' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('m',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                    
                    if  pygame.key.get_pressed()[pygame.K_n]:
                        if 'n' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'n' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('n',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_o]:
                        if 'o' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'o' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('o',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_p]:
                        if 'p' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'p' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('p',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_q]:
                        if 'q' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'q' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('q',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                
                    if  pygame.key.get_pressed()[pygame.K_r]:
                        if 'r' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'r' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('r',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                            
                    if  pygame.key.get_pressed()[pygame.K_s]:
                        if 's' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if's' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('s',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter]=True
                                
                        else:
                            errors = errors+1
                            
                    if  pygame.key.get_pressed()[pygame.K_t]:
                        if 't' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if't' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('t',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1        
               
                    if  pygame.key.get_pressed()[pygame.K_u]:
                        if 'u' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'u' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('u',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1       
                            
                    if  pygame.key.get_pressed()[pygame.K_v]:
                        if 'v' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'v' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('v',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1  
                            
                    if  pygame.key.get_pressed()[pygame.K_w]:
                        if 'w' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'w' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('w',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1

                    if  pygame.key.get_pressed()[pygame.K_x]:
                        if 'x' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'x' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('x',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                
                    if  pygame.key.get_pressed()[pygame.K_y]:
                        if 'y' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'y' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('y',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1        
                    
                    if  pygame.key.get_pressed()[pygame.K_z]:
                        if 'z' in word:
                            x =[]
                            for letter in range(len(word)):
                                 if'z' ==word[letter]:
                                    x.append(letter)
                                    
                            for letter in x:
                                main.draw_bottom_text('z',pygame.font.SysFont(None,unders),White,panel,int((int(letter*skipSpace+X/4+2*r)+int(letter*skipSpace+X/4+2*r+unders))/2),int(Y/3))
                                correctGuess[letter] =True
                        else:
                            errors = errors+1
                pygame.display.update()
                pygame.time.delay(10)
                if not False in correctGuess:
                    score =score+1
                    main.draw_text(word,pygame.font.SysFont(None,70),White,panel,int(X/2),int(Y/2)) 
                    pygame.display.update()
                    pygame.time.delay(10)
                    guessing =False
                if errors ==7:
                    nextScreen =True
                    while nextScreen:
                        main.draw_text(word,pygame.font.SysFont(None,70),White,panel,int(X/2),int(Y/2))
                        next_button=pygame.Rect(0,0,180,70)
                        next_button.center =int(3*X/4),int(Y*4/5)
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if mouse[1]<int(Y*4/5)+35 and mouse[1]> int(Y*4/5)-35 and mouse[0]>int(3*X/4)-90 and mouse[0]<int(3*X/4)+90:
                            pygame.draw.rect(panel,(128,128,128),next_button)
                            if click[0] ==1:
                                guessing =False
                                main.score_board(score*5)
                                nextScreen =False
                                gameRun =False
                        else:pygame.draw.rect(panel,Black,next_button)
                        main.draw_text("Next",pygame.font.SysFont(None,70),White,panel,int(3*X/4),int(Y*4/5))
                        pygame.display.update()
                        pygame.time.delay(10)
                        #event for loop
                        for event in pygame.event.get():
                            if event.type ==pygame.QUIT:
                                nextScreen =False
            
            pygame.time.delay(1000)                    
            panel.fill((0,0,0))
        pygame.quit()
    def menu():
        pygame.init()
        panel = pygame.display.set_mode([X,Y])
        pygame.display.set_caption("Ultimate Hangman")
        panel.fill(Black)
        menu =True
        while menu:    
            main.draw_MenuScreen(panel,pygame)
            main.draw_text("Ultimate Hangman",pygame.font.SysFont(None,120),White,panel,int(1*X/2),int(Y/7))
            main.draw_text("Play:",pygame.font.SysFont(None,100),White,panel,int(3*X/4),int(Y/5))
             #button
            easy_button =pygame.Rect(0,0,180,70)
            easy_button.center =int(3*X/4),int(Y*2/5)

            medium_button=pygame.Rect(0,0,180,70)
            medium_button.center=int(3*X/4),int(Y*3/5)

            hard_button=pygame.Rect(0,0,180,70)
            hard_button.center =int(3*X/4),int(Y*4/5)
    
    
   
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            #press for easy
            if mouse[1]<int(Y*2/5)+35 and mouse[1]> int(Y*2/5)-35 and mouse[0]>int(3*X/4)-90 and mouse[0]<int(3*X/4)+90:
                pygame.draw.rect(panel,(128,128,128),easy_button)
                if click[0] ==1:
                    pygame.quit()
                    main.easy_hangman()
                    menu =False
            else:pygame.draw.rect(panel,Black,easy_button)
            #press for medium
            if mouse[1]<int(Y*3/5)+35 and mouse[1]> int(Y*3/5)-35 and mouse[0]>int(3*X/4)-90 and mouse[0]<int(3*X/4)+90:
                pygame.draw.rect(panel,(128,128,128),medium_button)
                if click[0] ==1:
                    pygame.quit()
                    main.medium_hangman()
                    menu =False
            else:pygame.draw.rect(panel,Black,medium_button)
            #press for hard
            if mouse[1]<int(Y*4/5)+35 and mouse[1]> int(Y*4/5)-35 and mouse[0]>int(3*X/4)-90 and mouse[0]<int(3*X/4)+90:
                pygame.draw.rect(panel,(128,128,128),hard_button)
                if click[0] ==1:
                    pygame.quit()
                    main.hard_hangman()
                    menu =False
            else:pygame.draw.rect(panel,Black,hard_button)
            #text on alll the buttons
            main.draw_text("Easy",pygame.font.SysFont(None,70),White,panel,int(3*X/4),int(Y*2/5))
            main.draw_text("Medium",pygame.font.SysFont(None,70),White,panel,int(3*X/4),int(Y*3/5))
            main.draw_text("Hard",pygame.font.SysFont(None,70),White,panel,int(3*X/4),int(Y*4/5))

            pygame.display.update()
            pygame.time.delay(10)
            #event for loop
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    menu =False

if __name__ =="__main__":
    main.menu()
    pygame.quit()






         