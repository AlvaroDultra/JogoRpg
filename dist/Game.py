from tkinter import *
import tkinter as tk
from tkinter import messagebox
janela = Tk()
janela.geometry("1800x900")
labelnomeperso1 = Label(janela, text='Insira nome do \n primeiro personagem')
labelnomeperso1.grid(column=2, row=0)
nome1entry = tk.Entry(janela, width=30)

nome1entry.grid(column=3, row=0)
labelnomeperso2 = Label(janela, text= 'insira nome do \nsegundo personagem')
labelnomeperso2.grid(column=6, row=0)
nome2entry = tk.Entry(janela, width=30)

nome2entry.grid(column=7, row=0)
labelsaude1 = Label(janela, text='Insira a saude')
labelsaude1.grid(column=2, row=3)
saude1entry = tk.Entry(janela, width=30)

saude1entry.grid(column=3, row=3)
labelatak1 = Label(janela, text='Insira o ataque')
labelatak1.grid(column=2, row=4)
atak1entry = tk.Entry(janela, width=30)
atak1entry.grid(column=3, row=4)

habespecial1label = Label(janela, text="insira o poder da habilidade especial \nde seu personagem")
habespecial1label.grid(column=2, row=5)
habe1entry = tk.Entry(janela, width=30)
habe1entry.grid(column=3, row=5)

labelsaude2 = Label(janela, text='Insira a saude')
labelsaude2.grid(column=6, row=3)
saude2entry = tk.Entry(janela, width=30)
saude2entry.grid(column=7, row=3)

labelatak2 = Label(janela, text='Insira o ataque')
labelatak2.grid(column=6, row=4)
atak2entry = tk.Entry(janela, width=30)
atak2entry.grid(column=7, row=4)

habespecial2label = Label(janela, text="insira o poder da habilidade especial \nde seu personagem")
habespecial2label.grid(column=6, row=5)
habe2entry = tk.Entry(janela, width=30)
habe2entry.grid(column=7, row=5)


classe1entry =StringVar()
magorb = Radiobutton(janela, text= 'Mago', value='MAGO', variable= classe1entry)
magorb.grid(column=2, row=7)
Guerreirob = Radiobutton(janela, text= 'Guerreiro', value='GUERREIRO', variable= classe1entry)
Guerreirob.grid(column=2, row=8)
boxerb = Radiobutton(janela, text= 'Boxer', value='BOXER', variable= classe1entry)
boxerb.grid(column=2, row=9)
ladinob = Radiobutton(janela, text= 'Ladino', value='LADINO', variable= classe1entry)
ladinob.grid(column=2, row=10)

classe2entry =StringVar()
magorb = Radiobutton(janela, text= 'Mago', value='MAGO', variable= classe2entry)
magorb.grid(column=7, row=7)
Guerreirob = Radiobutton(janela, text= 'Guerreiro', value='GUERREIRO', variable= classe2entry)
Guerreirob.grid(column=7, row=8)
boxerb = Radiobutton(janela, text= 'Boxer', value='BOXER', variable= classe2entry)
boxerb.grid(column=7, row=9)
ladinob = Radiobutton(janela, text= 'Ladino', value='LADINO', variable= classe2entry)
ladinob.grid(column=7, row=10)


text_widget = tk.Text(janela, width=125, height=40)
text_widget.grid(column=5, row=13)




import random
import sys

class RedirectText:
    def __init__(self, text_widget):
        self.output = text_widget

    def write(self, string):
        self.output.insert(tk.END, string)

sys.stdout = RedirectText(text_widget)


class Personagem:
        
        def __init__(self, nome, saude:int, ataque:int):
            self.nome = nome
            self.saude = saude
            self.ataque = ataque
            
        def dano(self, dano):
            
            self.saude -= dano
            if self.saude <= 0:
                return f'{self.nome} foi atacado e tomou {dano} de dano e agora está morto'
            else:
                return f'{self.nome} foi atacado e tomou {dano} de dano e agora está com {self.saude} de vida'
            
        def atacar(self, alvo):
            
            return f'{self.nome} atacou {alvo} com um poder de {self.ataque}'
        
        

class Mago(Personagem):
        def __init__(self, poder_de_cura, nome, saude, ataque):
            super().__init__(nome, saude, ataque)
            self.poder_de_cura = poder_de_cura
        
        def cura(self):
            if self.saude <= 0:
                return f'{self.nome} está morto e não pode fazer isso'
            
            self.saude += self.poder_de_cura
            return f'{self.nome} se curou e agora está com {self.saude} de vida'

class Guerreiro(Personagem):
        def __init__(self, furia, nome, saude, ataque):
            super().__init__(nome, saude, ataque)
            self.furia = furia
            
        def enfurecer(self):
            if self.saude <= 0:
                return f'{self.nome} está morto e não pode fazer isso'
            
            self.ataque += self.furia
            return f'{self.nome} ficou putasso e agora tem {self.ataque} de ataque!'
        
class Ladino(Personagem):
        def __init__(self, nome, saude, ataque):
            
            super().__init__(nome, saude, ataque)
            
            
        
        def roubar(self, alvo,roubo): 
            self.saude+=roubo
            return(f'{self.nome} roubou de {alvo} {roubo} pontos de vida e agora esta com {self.saude}' )
        
        def robatk (self, alvo, roubo):
            self.ataque+=roubo
            return(f'{self.nome} roubou de {alvo} {roubo} pontos de vida e os adicionou em seus pontos de ataque')

class Boxer(Personagem):
        def __init__(self, nome, saude, ataque):
            super().__init__(nome, saude, ataque)




#FIGURAS
fotomago = PhotoImage(file= "mago.png")
figuramago = Label(image=fotomago)
fotoguerreiro = PhotoImage(file='guerreiro.png')
figuraguerreiro=Label(image=fotoguerreiro)
fotoladino = PhotoImage(file='ladino.png')
figuraladino=Label(image=fotoladino)
fotoboxer = PhotoImage(file='outro boxer.png')
figuraboxer=Label(image=fotoboxer)

        
print('Seja Bem vindo! Pressione o botão regras para aprender a jogar se for a sua primeira vez por aqui!')        

def criar_personagem1():
        saude1=saude1entry.get()
        nome = nome1entry.get()
        atak1=atak1entry.get()
        habe1=habe1entry.get()
        classe = classe1entry.get()
        saude = int(saude1)
        if saude<65:
            print('Saude Tente Novamente!!')
            return
        pd = 100 - saude
        at = saude*0.11

        ataque = int(atak1)
        if ataque > at:
            print('Limite maximo violado,Tente Novamente!')
            return
        pd -= ataque
        classe=classe.upper()
        if classe == "MAGO":
            poder_de_cura = int(habe1)
            print('Personagem criado! Passando para criacao de seu oponente!')
            figuramago.grid(column=2, row=13)
            return Mago(poder_de_cura, nome, saude, ataque)
        elif classe == "GUERREIRO":
            furia = int(habe1)
            print('Personagem criado! Passando para criacao de seu oponente!')
            figuraguerreiro.grid(column=2, row=13)

            return Guerreiro(furia, nome, saude, ataque)
        elif classe == "LADINO":
            print('Personagem criado! Passando para criacao de seu oponente!')
            figuraladino.grid(column=2, row=13)
            return Ladino(nome, saude, ataque)
        elif classe == 'BOXER':
            print('Personagem criado! Passando para criacao de seu oponente!')
            figuraboxer.grid(column=2, row=13)
            return Boxer(nome, saude, ataque)

        if pd<0:
            print('Pontos maximos excedidos! Tente Novamente!')
            return
        else:
            print("Classe inválida! Tente Novamente!")
            
            return 
def criar_personagem2():
        nome = nome2entry.get()
        saude2=saude2entry.get()
        atak2=atak2entry.get()
        habe2=habe2entry.get()
        classe = classe2entry.get()
        saude = int(saude2)
        if saude<65:
            print('Saude menor que 65, Tente Novamente!')
            return
        pd = 100 - saude
        at = saude*0.10

        ataque = int(atak2)
        if ataque > at:
            print('Limite maximo violado,Tente Novamente!')
            return

        
        pd -= ataque
        classe=classe.upper()
        if classe == "MAGO":
            poder_de_cura = int(habe2)
            print('Personagens criados! vamos a luta!')
            figuramago.grid(column=7, row=13)

            return Mago(poder_de_cura, nome, saude, ataque)
        elif classe == "GUERREIRO":
            furia = int(habe2)

            print('Personagens criados! vamos a luta!')
            figuraguerreiro.grid(column=7, row=13)

            return Guerreiro(furia, nome, saude, ataque)
        elif classe == "LADINO":
            print('Personagens criados! vamos a luta!')
            figuraladino.grid(column=7, row=13)
            return Ladino(nome, saude, ataque)

        elif classe == 'BOXER':
            print('Personagem criados! Vamos a luta')
            figuraboxer.grid(column=7, row=13)
            return Boxer(nome, saude, ataque)    
        if pd<0:
            print('Pontos maximos excedidos! Tente Novamente!')
            return
        else:
            print("Classe inválida! Tente Novamente!")
            
            return

def regras():
    text_widget.delete('1.0', tk.END) 





    print("Vamos as Regras do Jogo! Primeiramente cada personagem possui 100 pontos de XP para distribuir entre Saude, ataque e Habilidade especial(calma que eu ja explico o que é isso) \nA primeira decisão que deve ser feita é quantos pontos de saúde o seu personagem terá, para que nenhum personagem fique muito fraco, ao menos 65 pontos devem ser exclusivos à Saude!\nApós cadastrar seus pontos de saúde, você deve destinar os restantes de seus pontos entre ataque e habilidades especiais (calmaaa ja falei que jaja explico), no entanto seu ataque so pode representar NO MÁXIMO 10% DE SUA SAÚDE!\nDa forma que se sua saúde for 65, seu personagem só poderá ter 6 pontos de ataque\nVamos agora as classes e as habilidades especiais!\nO stats de Habilidades especiais é utilizado para caracterizar o poder que a habilidade especial de cada personagem terá baseado na classe que for escolhida\nA classe de mago possui a habilidade especial de curar, o poder da cura é representado por quantos pontos foram destinados a essa caracteristica\nA classe de Guerreiro possui a habilidade especial de se enfurecer que acrescenta ao seu ataque a quantidade de pontos destinados a habilidade especial, no entanto, ao utilizar essa habilidade, o jogador deve ficar uma rodada sem jogar.\nAs classes de Ladino e mago possuem habilidades especiais que não nescessitam de pontos exclusivos.\nO ladino, possui duas habilidades, a de Roubar ataque (Ratk) que acrescenta aos seus pontos de ataque a quantidade que seu adversário possui, após utilizar essa habilidade o Ladino deve ficar uma rodada sem jogar.\nE a de Roubar Saúde (ROB) que acrescenta aos seus pontos de saude a quantidade que seu adversário possui de ataque, após utilizar essa habilidade o Ladino deve ficar uma rodada sem jogar.\nAntes de explicar sobre a classe de Boxer, será necessário falar sobre os dados, cada ação de ataque só é bem sucedida se os dados rolarem um número acima de 3 (os dados tem 6 faces), números abaixo disso causam com que o oponente desvie, e se o jogador tirar 6, ele consegue um dano crítico.\nO Boxer, possui a seguinte habilidade: tentar sequencias. A priori, os dados pra essa habilidade tem 9 faces, caso o jogador tire entre 3 e 6, o resultado será um ataque normal.\nNo entanto, se o dado rolar mais do que 6, o boxer acertará um dano critico e jogará novamente! após usar essa habilidade, o Boxer deve ficar uma rodada sem jogar.\nJogo explicado! Vamos à Luta!")

regrasb = Button(janela, text='Regras',command=regras)
regrasb.grid(column=5, row=7)
    
def jogar ():
        text_widget.delete('1.0', tk.END)
        personagem1 = criar_personagem1()
        personagem2 = criar_personagem2()
        while True:
            

            
            acao = None
            
            def atq1():
                nonlocal acao
                acao = "1ATK"
                
            atq11 = Button(janela, text=f'{personagem1.nome} atacar',command=atq1)
            atq11.grid(column=2, row=7)

            def atq2():
                nonlocal acao
                acao = "2ATK"
                
            atq22 = Button(janela, text=f'{personagem2.nome} atacar',command=atq2)
            atq22.grid(column=7, row=7)
    
            def seq1():
                 nonlocal acao
                 acao = '1SEQ'

            seq11 = Button(janela, text=f'{personagem1.nome} sequencia', command=seq1)
            seq11.grid(column=2, row=8)
            
            def seq2():
                 nonlocal acao
                 acao = '2SEQ'
            
            seq22 = Button(janela, text=f'{personagem2.nome} sequencia', command=seq2)
            seq22.grid(column=7, row=8)
            
            def cur1():
                 nonlocal acao
                 acao = '1CUR'
            cur11 = Button(janela, text=f'{personagem1.nome} cura', command=cur1)
            cur11.grid(column=2, row=9)

            def cur2():
                 nonlocal acao
                 acao = '2CUR'
            cur22 = Button(janela, text=f'{personagem2.nome} cura', command=cur2)
            cur22.grid(column=7, row=9)

            def fur1():
                 nonlocal acao
                 acao = '1FUR'
            fur11 = Button(janela, text=f'{personagem1.nome} se enfurecer', command=fur1)
            fur11.grid(column=2, row=10)

            def fur2():
                 nonlocal acao
                 acao = '2FUR'
            fur22 = Button(janela, text=f'{personagem2.nome} se enfurecer', command=fur2)
            fur22.grid(column=7, row=10)
            

            def rob1():
                 nonlocal acao
                 acao = '1ROB'
            rob11 = Button(janela, text=f'{personagem1.nome} roubar saude', command=rob1)
            rob11.grid(column=2, row=11)

            def rob2():
                 nonlocal acao
                 acao = '2ROB'
            rob22 = Button(janela, text=f'{personagem2.nome} roubar saude', command=rob2)
            rob22.grid(column=7, row=11)

            def rtk1():
                 nonlocal acao
                 acao = '1RTK'
            rtk11 = Button(janela, text=f'{personagem1.nome} roubar ataque', command=rtk1)
            rtk11.grid(column=2, row=12)

            def rtk2():
                 nonlocal acao
                 acao = '2RTK'
            rtk22 = Button(janela, text=f'{personagem2.nome} roubar ataque', command=rtk2)
            rtk22.grid(column=7, row=12)
            
            while acao == None:
                 janela.update_idletasks()
                 janela.update()
                 
            if acao=='1ATK':
                x = random.randint(1, 6)
                if x>3 and x<6:
                    print (personagem1.atacar(personagem2.nome))
                    print (personagem2.dano(personagem1.ataque))
                elif x==6:
                    print(f'{personagem1.nome} CONSEGUIU UM DANO CRITICO!!! (rolagem dos dados {x})')
                    print (personagem1.atacar(personagem2.nome))
                    print (f'No entanto, seu pooder critico transformou seu poder de ataque em {personagem1.ataque*1.5}!!!')
                    print (personagem2.dano(int(personagem1.ataque * 1.5)))

                    
                else:
                    print (f'{personagem2.nome} esquivou!(rolagem dos dados {x})')
            
            
            if acao == '2ATK':
                x = random.randint(1,6)
                if x>3 and x<6:
                    print(personagem2.atacar(personagem1.nome))
                    print(personagem1.dano(personagem2.ataque))
                
                elif x==6:
                    print(f'{personagem2.nome} CONSEGUIU UM DANO CRITICO!!!(rolagem dos dados {x})')
                    print (personagem2.atacar(personagem1.nome))
                    print (f'No entanto, seu pooder critico transformou seu poder de ataque em {personagem2.ataque*1.5}!!!')
                    print (personagem1.dano(int(personagem2.ataque * 1.5)))

                else:
                    print(f'{personagem1.nome} esquivou(rolagem dos dados {x})')

            if acao == '2SEQ':
                if personagem2.__class__!= Boxer:
                    print('Seu personagem não é um boxeador')
                elif personagem2.__class__==Boxer:
                    x = random.randint (1,9)
                    if x>3 and x<6:
                        print(personagem2.atacar(personagem1.nome))
                        print(personagem1.dano(personagem2.ataque))
                    elif x>=6:
                        print(f'{personagem2.nome} CONSEGUIU UM DANO CRITICO!!!(rolagem dos dados {x})')
                        print (personagem2.atacar(personagem1.nome))
                        print (f'No entanto, sua velocidade e forca vinda do boxe transformou seu dano {personagem2.ataque*2.5}!!! e além disso, {personagem1.nome} ficou tão atordoado que {personagem2.nome} jogará novamente!')
                        print (personagem1.dano(int(personagem2.ataque * 2.5)))
                    else:
                        print(f'{personagem1.nome} esquivou(rolagem dos dados {x})')
            
            if acao =='1SEQ':
                if personagem1.__class__!= Boxer:
                    print('Seu personagem não é um boxeador')
                elif personagem1.__class__==Boxer:
                    x = random.randint (1,9)
                    if x>3 and x<6:
                        print(personagem1.atacar(personagem2.nome))
                        print(personagem2.dano(personagem1.ataque))
                    elif x>=6:
                        print(f'{personagem1.nome} CONSEGUIU UM DANO CRITICO!!!(rolagem dos dados {x})')
                        print (personagem1.atacar(personagem2.nome))
                        print (f'No entanto, sua velocidade e forca vinda do boxe transformou seu dano em {personagem1.ataque*2.5}!!! e além disso, {personagem2.nome} ficou tão atordoado que {personagem1.nome} jogará novamente!')
                        print (personagem2.dano(int(personagem1.ataque * 2.5)))
                    else:
                        print(f'{personagem2.nome} esquivou(rolagem dos dados {x})')



            if acao =='1CUR':
                if personagem1.__class__ != Mago:
                    print('Seu personagem não é um mago')
                elif personagem1.__class__ == Mago:
                    print(personagem1.cura())
            
            if acao =='2CUR':
                if personagem2.__class__ != Mago:
                    print('Seu personagem não é um mago')
                elif personagem1.__class__ == Mago:
                    print(personagem2.cura())

            if acao == '1FUR':
                if personagem1.__class__ != Guerreiro:
                    print('Seu personagem não é um guerreiro')
                elif personagem1.__class__ == Guerreiro:
                    print(personagem1.enfurecer())

            if acao == '2FUR':
                if personagem2.__class__ != Guerreiro:
                    print('Seu personagem não é um guerreiro')	
                elif personagem2.__class__ == Guerreiro:
                    print(personagem2.enfurecer())

            if acao == '1ROB':
                if personagem1.__class__!= Ladino:
                    print('Seu personagem não é um Ladino')
                elif personagem1.__class__== Ladino:
                    
                        print(personagem1.roubar(personagem2.nome, personagem2.ataque))
                        
                    
            if acao == '2ROB':
                if personagem2.__class__ != Ladino:
                    print('Seu personagem não é um Ladino')
                elif personagem2.__class__ == Ladino:
                    
                        print(personagem2.roubar(personagem1.nome, personagem1.ataque))
                        
            
            if acao == '1RTK':
                if personagem1.__class__!= Ladino:
                    print('Seu personagem não é um Ladino')
                elif personagem1.__class__== Ladino:
                    
                        print(personagem1.robatk(personagem2.nome, personagem2.ataque))
                        
                    
            if acao == '2RTK':
                if personagem2.__class__ != Ladino:
                    print('Seu personagem não é um Ladino')
                elif personagem2.__class__ == Ladino:
                    
                        print(personagem2.robatk(personagem1.nome, personagem1.ataque))
                        
                    
            

            if personagem1.saude <= 0:
                print(f"{personagem1.nome} morreu!")
                break
            elif personagem2.saude <= 0:
                print(f"{personagem2.nome} morreu!")
                break
            
                
jogarb = Button(janela, text='Jogar',command=jogar)
jogarb.grid(column=5, row=8)

janela.mainloop()
