
from tkinter import *
from PIL import ImageTk,Image

game_interfaace = Tk()
game_interfaace.title("The dragon return")
game_interfaace.minsize(960,640)
game_interfaace.maxsize(960,640)
char_status =[0,0,0,0,0,0,0,0,0]
skill_level = [0,0,0]
skill_damage = [0,0,0]
exp_to_level_up = 10
save_level = [1,1,1]
width_heigh_bt_heigh_lb = [33,3,3]
day = 1
skill_name = ["Fire ball","Buster ball","Meteo shower "]
potion_name = ["Level 1 potion","Level 2 potion","Level 3 potion"]
potion_effect = [15,50,200]
potion_have = [0,0,0]
potion_price = [150,500,1500]
level_job = [0,0]
turn_skill = [1,2,3]
exp_to_job_up = 15
time = 0

monster = 1
ch_fist_turn = 0
player_turn_in_combat = 0
hp_max_in_combat = 0
hp_now = 0
player_turn_need = 0
skill_in_use = 5
stage = 0
monster_turn_in_combat = 0
monster_in_combat = [0,0,0]

pic_menu = ImageTk.PhotoImage(Image.open("pic/menu/c01.jpg"))
pic_menu_play = ImageTk.PhotoImage(Image.open("pic/menu/menu.jpg"))
pic_story_1 = ImageTk.PhotoImage(Image.open("pic/story/001.jpg"))
pic_story_2 = ImageTk.PhotoImage(Image.open("pic/story/002.jpg"))
pic_story_3 = ImageTk.PhotoImage(Image.open("pic/story/003.jpg"))
pic_menu_combat = ImageTk.PhotoImage(Image.open("pic/menu/menu_at_combat.jpg"))
pic_menu_shop = ImageTk.PhotoImage(Image.open("pic/menu/menu_at_shop.jpg"))
pic_menu_status = ImageTk.PhotoImage(Image.open("pic/menu/menu_at_status.jpg"))


pic_combat_blank = ImageTk.PhotoImage(Image.open("pic/combat/cave/blank_enemy.jpg"))
pic_combat_action_with_slime =ImageTk.PhotoImage(Image.open("pic/combat/cave/action_with_slime.jpg"))
pic_combat_action_with_zombie = ImageTk.PhotoImage(Image.open("pic/combat/cave/action_with_zombie.jpg"))
pic_combat_action_with_skeleton =ImageTk.PhotoImage(Image.open("pic/combat/cave/action_with_skeleton.jpg"))

pic_combat_stanby_with_slime =ImageTk.PhotoImage(Image.open("pic/combat/cave/stanby_with_slime.jpg"))
pic_combat_stanby_with_zombie = ImageTk.PhotoImage(Image.open("pic/combat/cave/stanby_with_zombie.jpg"))
pic_combat_stanby_with_skeleton =ImageTk.PhotoImage(Image.open("pic/combat/cave/stanby_with_skeleton.jpg"))

pic_combat_action_slime =ImageTk.PhotoImage(Image.open("pic/combat/cave/action_slime.jpg"))
pic_combat_action_zombie = ImageTk.PhotoImage(Image.open("pic/combat/cave/action_zombie.jpg"))
pic_combat_action_skeleton =ImageTk.PhotoImage(Image.open("pic/combat/cave/action_skeleton.jpg"))

pic_combat_stanby_with_mercenary = ImageTk.PhotoImage(Image.open("pic/combat/tower/stanby_with_mercenary.jpg"))
pic_combat_stanby_with_knight = ImageTk.PhotoImage(Image.open("pic/combat/tower/stanby_with_knight.jpg"))
pic_combat_stanby_with_mage = ImageTk.PhotoImage(Image.open("pic/combat/tower/stanby_with_mage.jpg"))
pic_combat_stanby_with_boss = ImageTk.PhotoImage(Image.open("pic/combat/tower/stanby_with_boss.jpg"))

pic_combat_action_with_mercenary = ImageTk.PhotoImage(Image.open("pic/combat/tower/action_with_mercenary.jpg"))
pic_combat_action_with_knight = ImageTk.PhotoImage(Image.open("pic/combat/tower/action_with_knight.jpg"))
pic_combat_action_with_mage = ImageTk.PhotoImage(Image.open("pic/combat/tower/action_with_mage.jpg"))
pic_combat_action_with_boss = ImageTk.PhotoImage(Image.open("pic/combat/tower/action_with_boss.jpg"))

pic_combat_action_mercenary = ImageTk.PhotoImage(Image.open("pic/combat/tower/action_mercenary.jpg"))
pic_combat_action_knight = ImageTk.PhotoImage(Image.open("pic/combat/tower/action_knight.jpg"))
pic_combat_action_mage = ImageTk.PhotoImage(Image.open("pic/combat/tower/action_mage.jpg"))
pic_combat_action_boss = ImageTk.PhotoImage(Image.open("pic/combat/tower/action_boss.jpg"))
pic_combat_tower = ImageTk.PhotoImage(Image.open("pic/combat/tower/Tower.jpg"))
pic_combat_tower_noenemy = ImageTk.PhotoImage(Image.open("pic/combat/tower/tower_noenemy.jpg"))



story_run = 1
slot_check = 0
save_name = ["Emty","Emty","Emty"]
save_file_location = ["savefile/save1.txt","savefile/save2.txt","savefile/save3.txt",]
in_save_name = StringVar()
enter_save_name = Tk
warning_new_save = Tk
block_Enter_name = 0
sv_name = "Emty"


for a in range(0,3):
    try :
        filepath = save_file_location[a]
        f1 = open(filepath,"r",encoding="utf-8")
        #save_name.append(f1.readline())
        save_name[a] = f1.readline()
        save_level[a]= int(f1.readline())
        f1.close()
    except :
        print(" ")

def story1_1st():
    global pic_story_1
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global story_run
    global width_heigh_bt_heigh_lb

    try :
        pic_label.grid_forget()
        pic_label = Label(image=pic_story_1)
        pic_label.grid(row=0,column=0,columnspan=4)

        text_label.grid_forget()
        text_label = Label(game_interfaace,text="After the great dragon lose  the pricess.",height=width_heigh_bt_heigh_lb[2])
        text_label.grid(row=1,column=0,columnspan=4)


        button_1.grid_forget()
        button_2.grid_forget()
        button_3.grid_forget()
        button_4.grid_forget()

        button_1 = Button(game_interfaace,text="Next",command=story1_2st,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
        button_2 = Button(game_interfaace,text="    ",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
        button_3 = Button(game_interfaace,text="    ",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
        button_4 = Button(game_interfaace,text="Exit",command=fist_menu_1,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

        button_1.grid(row=2,column=0)
        button_2.grid(row=2,column=1)
        button_3.grid(row=2,column=2)
        button_4.grid(row=2,column=3)
    except:
        print(" ")
   
def play_menu():
    global pic_menu_play
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global time

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_play)
    pic_label.grid(row=0,column=0,columnspan=4)

    if time == 0:
        tt = "day"
    else :
        tt = "evening"
    
   

    text_at_label = "What do you want to do?     \nTime : {}".format(tt)
    text_label.grid_forget()
    text_label = Label(game_interfaace,text=text_at_label,height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)



    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="COMBAT",command=go_combat,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="SHOP",command=shop,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="STATUS",command=ch_status,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK TO MANU",command=save_game,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def save_game():
    global slot_check
    global save_file_location
    global save_name
    global sv_name
    global char_status
    global skill_level
    global potion_have
    global level_job
    global time
    global day
    global save_level
    save_level[slot_check] = char_status[0]
    filepath = save_file_location[slot_check]
    f1 = open(filepath,"w+",encoding="utf-8")
    f1.writelines(save_name[slot_check])
    f1.writelines("{}\n".format(char_status[0]))
    f1.writelines("{}\n".format(char_status[1]))
    f1.writelines("{}\n".format(char_status[2]))
    f1.writelines("{}\n".format(char_status[3]))
    f1.writelines("{}\n".format(char_status[4]))
    f1.writelines("{}\n".format(char_status[5]))
    f1.writelines("{}\n".format(char_status[6]))
    f1.writelines("{}\n".format(char_status[7]))
    f1.writelines("{}\n".format(day))
    f1.writelines("{}\n".format(skill_level[0]))
    f1.writelines("{}\n".format(skill_level[1]))
    f1.writelines("{}\n".format(skill_level[2]))
    f1.writelines("{}\n".format(potion_have[0]))
    f1.writelines("{}\n".format(potion_have[1]))
    f1.writelines("{}\n".format(potion_have[2]))
    f1.writelines("{}\n".format(level_job[0]))
    f1.writelines("{}\n".format(level_job[1]))
    f1.writelines("{}\n".format(time))
    f1.close()
    fist_menu_1()
    

def go_combat():
    global pic_menu_combat
    global pic_label
    global text_label
    global level_job
    global exp_to_job_up
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_combat)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="Where are you want to go?",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)

    text_work = "Work\nLv. {:3}  Exp {:4}/{:4}".format(level_job[0],level_job[1],exp_to_job_up)

    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    need_level = char_status[7]*10
    if need_level == 40:
        need_level = 50

    text_bt1 = "Tower Lv. {}\nNeed Lv. {}".format(char_status[7],need_level)

    button_1 = Button(game_interfaace,text=text_bt1,command=tower,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="CAVE",command=cave,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text=text_work,width=width_heigh_bt_heigh_lb[0],command=work,height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=play_menu,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def cave():
    global stage
    stage = 1
    cal_monster_in_cave()
    set_status_combat()
    player_turn()

def tower():
    global stage
    global char_status
    need_level = char_status[7]*10
    if need_level == 40:
        need_level = 50
    if char_status[0] >= need_level:
        stage = 2
        cal_tower()
        set_status_combat()
        player_turn()
    

def cal_tower():
    global char_status
    global monster_in_combat
    global monster
    if char_status[7] == 1:
        monster_in_combat[0] = 150
        monster_in_combat[1] = 10
        monster_in_combat[2] = 2
        monster = 4
    elif char_status[7] == 2:
        monster_in_combat[0] = 600
        monster_in_combat[1] = 50
        monster_in_combat[2] = 1
        monster =5
    elif char_status[7] == 3:
        monster_in_combat[0] = 500
        monster_in_combat[1] = 200
        monster_in_combat[2] = 3
        monster = 6
    elif char_status[7] == 4:
        monster_in_combat[0] = 1500
        monster_in_combat[1] = 150
        monster_in_combat[2] = 2
        monster = 7


def player_turn():
    global pic_combat_stanby_with_skeleton
    global pic_combat_stanby_with_slime
    global pic_combat_stanby_with_zombie

    global pic_combat_stanby_with_mercenary
    global pic_combat_stanby_with_knight
    global pic_combat_stanby_with_mage
    global pic_combat_stanby_with_boss

    global monster_in_combat
    global player_turn_in_combat
    global monster
    global ch_fist_turn
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4


    pic_label.grid_forget()
    if monster ==1:
        pic_label = Label(image=pic_combat_stanby_with_slime)
    elif monster == 2:
        pic_label = Label(image=pic_combat_stanby_with_zombie)
    elif monster == 3:
        pic_label = Label(image=pic_combat_stanby_with_skeleton)
    elif monster == 4:
        pic_label = Label(image=pic_combat_stanby_with_mercenary)
    elif monster == 5:
        pic_label = Label(image=pic_combat_stanby_with_knight)
    elif monster == 6:
        pic_label = Label(image=pic_combat_stanby_with_mage)
    elif monster == 7:
        pic_label = Label(image=pic_combat_stanby_with_boss)
    pic_label.grid(row=0,column=0,columnspan=4)

    textatlabel = "What do you want to do?\nYou HP {} / {}             Moster HP {}".format(hp_now,hp_max_in_combat,monster_in_combat[0])

    text_label.grid_forget()
    text_label = Label(game_interfaace,text=textatlabel,height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Normal Attack\n"+str(char_status[4]),command=normal_attack,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="Use skill",command=use_skill,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="Use potion",command=use_potion,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="RUN!",command=run,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def use_potion():
    global potion_have
    global potion_effect
    global potion_name
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global pic_combat_stanby_with_skeleton
    global pic_combat_stanby_with_slime
    global pic_combat_stanby_with_zombie
    global pic_combat_stanby_with_mercenary
    global pic_combat_stanby_with_knight
    global pic_combat_stanby_with_mage
    global pic_combat_stanby_with_boss
    global monster

    pic_label.grid_forget()
    if monster ==1:
        pic_label = Label(image=pic_combat_stanby_with_slime)
    elif monster == 2:
        pic_label = Label(image=pic_combat_stanby_with_zombie)
    elif monster == 3:
        pic_label = Label(image=pic_combat_stanby_with_skeleton)
    elif monster == 4:
        pic_label = Label(image=pic_combat_stanby_with_mercenary)
    elif monster == 5:
        pic_label = Label(image=pic_combat_stanby_with_knight)
    elif monster == 6:
        pic_label = Label(image=pic_combat_stanby_with_mage)
    elif monster == 7:
        pic_label = Label(image=pic_combat_stanby_with_boss)
    pic_label.grid(row=0,column=0,columnspan=4)

    
    text_label.grid_forget()
    text_label = Label(game_interfaace,text="What potion do you want to use?",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)

    ts1 = "{}   \n Heal : {:3}      You have : {:3}".format(potion_name[0],potion_effect[0],potion_have[0])
    ts2 = "{}   \n Heal : {:3}      You have : {:3}".format(potion_name[1],potion_effect[1],potion_have[1])
    ts3 = "{}   \n Heal : {:3}      You have : {:3}".format(potion_name[2],potion_effect[2],potion_have[2])

    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text=ts1,command=bt1_to_use_potion,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text=ts2,command=bt2_to_use_potion,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text=ts3,command=bt3_to_use_potion,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=player_turn,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def bt1_to_use_potion():
    global char_status
    global potion_effect
    global potion_have
    global hp_max_in_combat
    global hp_now
    if potion_have[0] > 0:
        hp_now += potion_effect[0]
        if hp_now > hp_max_in_combat:
            hp_now = hp_max_in_combat
        potion_have[0] -= 1
        ch_dead_monster()

def bt2_to_use_potion():
    global char_status
    global potion_effect
    global potion_have
    global hp_max_in_combat
    global hp_now
    if potion_have[1] > 0:
        hp_now += potion_effect[1]
        if hp_now > hp_max_in_combat:
            hp_now = hp_max_in_combat
        potion_have[1] -= 1
        ch_dead_monster()

def bt3_to_use_potion():
    global char_status
    global potion_effect
    global potion_have
    global hp_max_in_combat
    global hp_now
    if potion_have[2] > 0:
        hp_now += potion_effect[2]
        if hp_now > hp_max_in_combat:
            hp_now = hp_max_in_combat
        potion_have[2] -= 1
        ch_dead_monster()
    


def use_skill():
    global pic_menu_status
    global skill_name
    global save_level
    global turn_skill
    global skill_damage
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global pic_combat_stanby_with_skeleton
    global pic_combat_stanby_with_slime
    global pic_combat_stanby_with_zombie
    global pic_combat_stanby_with_mercenary
    global pic_combat_stanby_with_knight
    global pic_combat_stanby_with_mage
    global pic_combat_stanby_with_boss

    pic_label.grid_forget()
    pic_label.grid_forget()
    if monster ==1:
        pic_label = Label(image=pic_combat_stanby_with_slime)
    elif monster == 2:
        pic_label = Label(image=pic_combat_stanby_with_zombie)
    elif monster == 3:
        pic_label = Label(image=pic_combat_stanby_with_skeleton)
    elif monster == 4:
        pic_label = Label(image=pic_combat_stanby_with_mercenary)
    elif monster == 5:
        pic_label = Label(image=pic_combat_stanby_with_knight)
    elif monster == 6:
        pic_label = Label(image=pic_combat_stanby_with_mage)
    elif monster == 7:
        pic_label = Label(image=pic_combat_stanby_with_boss)
    pic_label.grid(row=0,column=0,columnspan=4)
    pic_label.grid(row=0,column=0,columnspan=4)

    
    text_label.grid_forget()
    text_label = Label(game_interfaace,text="What skill you want to use?",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)

    ts1 = "{}   turn :{}\n Lv. : {:3}      Damage : {:3}".format(skill_name[0],turn_skill[0],skill_level[0],skill_damage[0])
    ts2 = "{}   turn :{}\n Lv. : {:3}      Damage : {:3}".format(skill_name[1],turn_skill[1],skill_level[1],skill_damage[1])
    ts3 = "{}   turn :{}\n Lv. : {:3}      Damage : {:3}".format(skill_name[2],turn_skill[2],skill_level[2],skill_damage[2])

    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text=ts1,command=bt1_to_use_skill,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text=ts2,command=bt2_to_use_skill,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text=ts3,command=bt3_to_use_skill,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=player_turn,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def bt1_to_use_skill():
    global player_turn_need
    global skill_in_use
    global turn_skill
    player_turn_need = turn_skill[0]
    skill_in_use = 0
    ch_dead_monster()

def bt2_to_use_skill():
    global player_turn_need
    global skill_in_use
    global turn_skill
    player_turn_need = turn_skill[1]
    skill_in_use = 1
    ch_dead_monster()
    
def bt3_to_use_skill():
    global player_turn_need
    global skill_in_use
    global turn_skill
    player_turn_need = turn_skill[2]
    skill_in_use = 2
    ch_dead_monster()
    


def normal_attack():
    global char_status
    global monster_in_combat
    global player_turn_in_combat
    global monster_turn_in_combat
    global skill_in_use
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    tt = "s"

    pic_label.grid_forget()
    if monster ==1:
        pic_label = Label(image=pic_combat_action_with_slime)
        tt = "You normal Atack to slime"

    elif monster == 2:
        pic_label = Label(image=pic_combat_action_with_zombie)
        tt = "You normal Atack to zombie"
    elif monster == 3:
        pic_label = Label(image=pic_combat_action_with_skeleton)
        tt ="You normal Atack to skeleton"
    elif monster == 4:
        pic_label = Label(image=pic_combat_action_with_mercenary)
        tt ="You normal Atack to mercenary"
    elif monster == 5:
        pic_label = Label(image=pic_combat_action_with_knight)
        tt ="You normal Atack to knight"
    elif monster == 6:
        pic_label = Label(image=pic_combat_action_with_mage)
        tt ="You normal Atack to mage"
    elif monster == 7:
        pic_label = Label(image=pic_combat_action_with_boss)
        tt ="You normal Atack to princess"
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text=tt,height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Next",command=ch_dead_monster,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],command=work,height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)
    monster_in_combat[0] -= char_status[4]
    player_turn_in_combat = 0
    skill_in_use = 5

def run():
    global monster_in_combat
    global stage
    global monster
    global ch_fist_turn
    global player_turn_in_combat
    global hp_max_in_combat
    global hp_now
    global player_turn_need
    global skill_in_use
    monster = 1
    ch_fist_turn = 0
    player_turn_in_combat = 0
    hp_max_in_combat = 0
    hp_now = 0
    player_turn_need = 0
    skill_in_use = 5
    stage = 1
    play_menu()

    

def ch_dead_monster():
    global monster_in_combat
    global stage
    global monster
    global ch_fist_turn
    global player_turn_in_combat
    global hp_max_in_combat
    global hp_now
    global player_turn_need
    global skill_in_use
    if monster_in_combat[0] <= 0:
        monster = 1
        ch_fist_turn = 0
        player_turn_in_combat = 0
        hp_max_in_combat = 0
        hp_now = 0
        player_turn_need = 0
        skill_in_use = 5
        if stage == 1:
            victory_cave()
        elif stage == 2:
            victory_tower()
        
    else :
        monster_turn()

def victory_tower():
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global pic_combat_blank
    global char_status

    pic_label.grid_forget()
    pic_label = Label(image=pic_combat_tower_noenemy)
    pic_label.grid(row=0,column=0,columnspan=4)

    
    cal_time()

    textatlabel = "You won this tower"

    text_label.grid_forget()
    text_label = Label(game_interfaace,text=textatlabel,height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    if char_status[7] >= 4:
        button_1 = Button(game_interfaace,text="Next",command=story3_1st,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    else :
        char_status[7] += 1
        button_1 = Button(game_interfaace,text="Next",command=play_menu,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_2 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def story3_1st():
    global pic_story_3
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global story_run


    pic_label.grid_forget()
    pic_label = Label(image=pic_story_3)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="And now the dragon successful revenge ,But she make over her limit.\nShe fall to the ground and fell asleep.",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Next",command=story3_2st,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="    ",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def story3_2st():
    global pic_story_3
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global story_run


    pic_label.grid_forget()
    pic_label = Label(image=pic_story_3)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="To be continue . . .",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Next",command=fist_menu_1,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="Back",command=story3_1st,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="    ",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)


def victory_cave():
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global pic_combat_blank

    pic_label.grid_forget()
    pic_label = Label(image=pic_combat_blank)
    pic_label.grid(row=0,column=0,columnspan=4)

    x = got_exp_at_cave()
    cal_time()

    textatlabel = "You won\n You got exp {}".format(x)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text=textatlabel,height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Next",command=cal_up_lv,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],command=work,height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def got_exp_at_cave():
    global char_status
    global exp_to_level_up
    y = int(10+(5*(char_status[0]-1)))
    return y

def cal_up_lv():
    global char_status
    global exp_to_level_up
    gt = got_exp_at_cave()
    char_status[1]+=gt
    if char_status[1] >= exp_to_level_up:
        char_status[0] += 1
        exp_to_level_up=cal_exp_up(char_status[0])
        char_status[1] = 0
        char_status[2] += 10
        char_status[3] += 5
        char_status[4] += 5
    play_menu()

    

def monster_turn():
    global monster_turn_in_combat
    global monster_in_combat
    global monster
    global hp_now
    global ch_fist_turn
    global pic_combat_action_slime
    global pic_combat_action_skeleton
    global pic_combat_action_zombie
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    if ch_fist_turn == 0:
        monster_turn_in_combat = 0
        ch_fist_turn += 1
    else :
        monster_turn_in_combat += 1

    pic_label.grid_forget()

    if monster_in_combat[2] <= monster_turn_in_combat:
        if monster ==1:
            tt = "Slime Normal attack at you\nHP -{}".format(monster_in_combat[1])
            pic_label = Label(image=pic_combat_action_slime)
        elif monster == 2:
            tt = "Zombie use bite at you\nHP -{}".format(monster_in_combat[1])
            pic_label = Label(image=pic_combat_action_zombie)
        elif monster == 3:
            tt = "Skeleton trow spear at you\nHP -{}".format(monster_in_combat[1])
            pic_label = Label(image=pic_combat_action_skeleton)
        elif monster == 4:
            tt = "Mercenary punch at you\nHP -{}".format(monster_in_combat[1])
            pic_label = Label(image=pic_combat_action_mercenary)
        elif monster == 5:
            tt = "Knight pico blade at you\nHP -{}".format(monster_in_combat[1])
            pic_label = Label(image=pic_combat_action_knight)
        elif monster == 6:
            tt = "Mage use laser beam at you\nHP -{}".format(monster_in_combat[1])
            pic_label = Label(image=pic_combat_action_mage)
        elif monster == 7:
            tt = "princess use judgment at you\nHP -{}".format(monster_in_combat[1])
            pic_label = Label(image=pic_combat_action_boss)
        
        Defentcal=char_status[3]*0.3
        Defentcal = int(Defentcal)
        Afterdefent = monster_in_combat[1] - Defentcal
        if Afterdefent<0 :
            Afterdefent=0
        hp_now -= Afterdefent
        monster_turn_in_combat = 0
    else : 
        if monster ==1:
            pic_label = Label(image=pic_combat_stanby_with_slime)
            tt = "Slime change"
        elif monster == 2:
            pic_label = Label(image=pic_combat_stanby_with_zombie)
            tt = "Zombie change"
        elif monster == 3:
            pic_label = Label(image=pic_combat_stanby_with_skeleton)
            tt = "Skeleton change"
        elif monster == 4:
            pic_label = Label(image=pic_combat_stanby_with_mercenary)
            tt = "Mercenary change"
        elif monster == 5:
            pic_label = Label(image=pic_combat_stanby_with_knight)
            tt = "Knight change"
        elif monster == 6:
            pic_label = Label(image=pic_combat_stanby_with_mage)
            tt = "Mage change"
        elif monster == 7:
            pic_label = Label(image=pic_combat_stanby_with_boss)
            tt = "Princess change"
    pic_label.grid(row=0,column=0,columnspan=4)
    text_label.grid_forget()
    text_label = Label(game_interfaace,text=tt,height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)
    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Next",command=ch_dead_player,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],command=work,height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def ch_dead_player():
    global monster_in_combat
    global hp_now
    global skill_in_use
    global monster
    global ch_fist_turn
    global player_turn_need
    global player_turn_in_combat
    global hp_max_in_combat
    global stage
    global monster_turn_in_combat

    if hp_now <= 0:
        monster = 1
        ch_fist_turn = 0
        player_turn_in_combat = 0
        hp_max_in_combat = 0
        hp_now = 0
        player_turn_need = 0
        skill_in_use = 5
        
        monster_turn_in_combat = 0
        lose_cave()
        
    else :
        if skill_in_use == 5:
            player_turn()
        else :
            check_player_turn_need()

def check_player_turn_need():
    global player_turn_need
    global player_turn_in_combat
    global skill_in_use
    global skill_damage
    global skill_name
    global monster_in_combat
    global pic_combat_action_with_skeleton
    global pic_combat_action_with_slime
    global pic_combat_action_with_zombie
    
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    if ch_fist_turn == 0:
        player_turn_in_combat = 0
    else :
        player_turn_in_combat += 1
    if player_turn_in_combat >= player_turn_need:
        tt = "You use skill {} to monster with {} damage".format(skill_name[skill_in_use],skill_damage[skill_in_use])
        monster_in_combat[0] -= skill_damage[skill_in_use]
        skill_in_use = 5
        player_turn_need = 0
        player_turn_in_combat = 0
    else:
        tt = "You change"

    
    pic_label.grid_forget()    
    if monster ==1:
        pic_label = Label(image=pic_combat_action_with_slime)
    elif monster == 2:
        pic_label = Label(image=pic_combat_action_with_zombie)
    elif monster == 3:
        pic_label = Label(image=pic_combat_action_with_skeleton)
    elif monster == 4:
        pic_label = Label(image=pic_combat_action_with_mercenary)
    elif monster == 5:
        pic_label = Label(image=pic_combat_action_with_knight)
    elif monster == 6:
        pic_label = Label(image=pic_combat_action_with_mage)
    elif monster == 7:
        pic_label = Label(image=pic_combat_action_with_boss)
    
    pic_label.grid(row=0,column=0,columnspan=4)


    

    text_label.grid_forget()
    text_label = Label(game_interfaace,text=tt,height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Next",command=ch_dead_monster,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],command=work,height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)



def lose_cave():
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global pic_combat_blank
    global stage

    pic_label.grid_forget()
    if stage == 1:
        pic_label = Label(image=pic_combat_blank)
    else :
        pic_label = Label(image=pic_combat_tower)
        stage = 1
    pic_label.grid(row=0,column=0,columnspan=4)


    cal_time()

    textatlabel = "You lose"

    text_label.grid_forget()
    text_label = Label(game_interfaace,text=textatlabel,height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Back to town",command=play_menu,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],command=work,height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)


def set_status_combat():
    global char_status
    global hp_now
    global hp_max_in_combat
    global ch_fist_turn 
    global player_turn_in_combat
    global player_turn_need

    player_turn_in_combat = 0
    hp_max_in_combat = 0
    hp_now = 0
    player_turn_need = 0

    ch_fist_turn = 0
    hp_now = char_status[2]
    hp_max_in_combat = char_status[2]


def cal_monster_in_cave():
    global char_status
    global monster
    global monster_in_combat
    lv = char_status[0]
    while lv > 10:
        lv -= 10
        monster += 1
        if monster == 4:
            monster = 1
    lv = char_status[0]
    if monster == 1:
        monster_in_combat[0] = 10+(5*lv)
        monster_in_combat[1] = 5+(3*lv)
        monster_in_combat[2] = 0
    elif monster == 2:
        monster_in_combat[0] = 15+(10*lv)
        monster_in_combat[1] = 5+(3*lv)
        monster_in_combat[2] = 1
    elif monster == 3:
        monster_in_combat[0] = 10+(8*lv)
        monster_in_combat[1] = 15+(15*lv)
        monster_in_combat[2] = 2


def work():
    global char_status
    global level_job
    global exp_to_job_up

    get_money = int(200+((level_job[0]-1)* 150))
    char_status[6] += get_money
    level_job[1] += 10
    if level_job[1] == exp_to_job_up:
        level_job[0] += 1
        level_job[1] = 0
        exp_to_job_up = cal_exp_job_up(level_job[0])
    cal_time()
    go_combat()

def cal_time():
    global time
    global day
    if time == 0:
        time = 1
    else :
        time = 0
        day += 1

def shop():
    global pic_menu_shop
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_shop)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="What are you want to do?",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)



    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="BUY POTION",command=buy_potion,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="UPGRADE STATUS",command=upgrade_atk,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="UPGRADE SKILL",command=upgrade_skill,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=play_menu,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def upgrade_atk():
    global char_status
    global pic_menu_shop
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_shop)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="What status do you want to Upgrade?\nYou have money : "+str(char_status[6]),height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)



    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    if char_status[6] >= 500:
        tt_atk = "ATK  Need money : 500\nNow  ----> Next\n{:4} ----> {:4}".format(char_status[4],char_status[4]+10)
    else :
        tt_atk = "ATK  Need money : 500\nyou don't have enough money to buy it."

    if char_status[6] >= 750:
        tt_magic = "Magic  Need money : 750\nNow  ----> Next\n{:4} ----> {:4}".format(char_status[5],char_status[5]+5)
    else :
        tt_magic = "Magic  Need money : 750\nyou don't have enough money to buy it."

    if char_status[6] >= 500:
        tt_Def = "DEF  Need money : 500\nNow  ----> Next\n{:4} ----> {:4}".format(char_status[3],char_status[3]+5)
    else :
        tt_Def = "DEF  Need money : 500\nyou don't have enough money to buy it."

    button_1 = Button(game_interfaace,text=tt_atk,command=cal_atk_up,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text=tt_magic,command=cal_magic_up,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text=tt_Def,command=cal_Def_up,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=shop,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def upgrade_skill():
    global skill_name
    global skill_level
    global skill_damage
    global pic_menu_shop
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_shop)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="What skill do you want to Upgrade?\nYou have money : "+str(char_status[6]),height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)



    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    next_dg_skill1 = cal_skill_1(skill_level[0]+1)
    next_dg_skill2 = cal_skill_2(skill_level[1]+1)
    next_dg_skill3 = cal_skill_3(skill_level[2]+1)
    

    if char_status[6] >= 800:
        tt_skill1 = "{}  Need money : 800\nLv : {:3}  ----> Lv : {:3}\n{:4} ----> {:4}".format(skill_name[0],skill_level[0],skill_level[0]+1,skill_damage[0],next_dg_skill1)
    else :
        tt_skill1 = "ATK  Need money : 800\nyou don't have enough money to buy it."
    if char_status[6] >= 800:
        tt_skill2 = "{}  Need money : 800\nLv : {:3}  ----> Lv : {:3}\n{:4} ----> {:4}".format(skill_name[1],skill_level[1],skill_level[1]+1,skill_damage[1],next_dg_skill2)
    else :
        tt_skill2 = "ATK  Need money : 800\nyou don't have enough money to buy it."
    if char_status[6] >= 800:
        tt_skill3 = "{}  Need money : 800\nLv : {:3}  ----> Lv : {:3}\n{:4} ----> {:4}".format(skill_name[2],skill_level[2],skill_level[2]+1,skill_damage[2],next_dg_skill3)
    else :
        tt_skill3 = "ATK  Need money : 800\nyou don't have enough money to buy it."

    

    button_1 = Button(game_interfaace,text=tt_skill1,command=bt1_up_skill,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text=tt_skill2,command=bt2_up_skill,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text=tt_skill3,command=bt3_up_skill,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=shop,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)


def bt1_up_skill():
    cal_up_skill(0)

def bt2_up_skill():
    cal_up_skill(1)

def bt3_up_skill():
    cal_up_skill(2)

def cal_up_skill(type_skill):
    global skill_level
    global char_status
    global skill_damage
    if char_status[6] >= 800:
        char_status[6] -= 800
        skill_level[type_skill] += 1
        if type_skill == 0:
            skill_damage[0] = cal_skill_1(skill_level[0])
        if type_skill == 1:
            skill_damage[1] = cal_skill_2(skill_level[1])
        if type_skill == 2:
            skill_damage[2] = cal_skill_3(skill_level[2])
    upgrade_skill()

def cal_atk_up():
    global char_status
    global skill_damage
    global skill_level

    if char_status[6] >= 500:
        char_status[6] -= 500
        char_status[4] += 10
    upgrade_atk()

def cal_Def_up():
    global char_status
    global skill_damage
    global skill_level

    if char_status[6] >= 500:
        char_status[6] -= 500
        char_status[3] += 5
    upgrade_atk()

def cal_magic_up():
    global char_status

    if char_status[6] >= 750:
        char_status[6] -= 750
        char_status[5] += 5
        skill_damage[0] = cal_skill_1(skill_level[0])
        skill_damage[1] = cal_skill_1(skill_level[1])
        skill_damage[2] = cal_skill_1(skill_level[2])

    upgrade_atk()


def buy_potion():
    global char_status
    global potion_have
    global pic_menu_shop
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global potion_name

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_shop)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="What potion do you want to buy?\nYou have money : "+str(char_status[6]),height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)



    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    if char_status[6] >= potion_price[0]:
        tt_potion_1 = "{}\nPrice : {:3}    You have : {:3}".format(potion_name[0],potion_price[0],potion_have[0])
    else :
        tt_potion_1 = "you don't have enough money to buy it."
    
    if char_status[6] >= potion_price[1]:
        tt_potion_2 = "{}\nPrice : {:3}    You have : {:3}".format(potion_name[1],potion_price[1],potion_have[1])
    else :
        tt_potion_2 = "you don't have enough money to buy it."

    if char_status[6] >= potion_price[2]:
        tt_potion_3 = "{}\nPrice : {:3}    You have : {:3}".format(potion_name[2],potion_price[2],potion_have[2])
    else :
        tt_potion_3 = "you don't have enough money to buy it."

    button_1 = Button(game_interfaace,text=tt_potion_1,command=bt1_to_buy_potion,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text=tt_potion_2,command=bt2_to_buy_potion,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text=tt_potion_3,command=bt3_to_buy_potion,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=shop,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def cal_buy_potion(potion_type):
    global char_status
    global potion_price
    global potion_have
    if char_status[6] >= potion_price[potion_type]:
        char_status[6] -= potion_price[potion_type]
        potion_have[potion_type] += 1
    buy_potion()

def bt1_to_buy_potion():
    cal_buy_potion(0)

def bt2_to_buy_potion():
    cal_buy_potion(1)

def bt3_to_buy_potion():
    cal_buy_potion(2)

def ch_status():
    global pic_menu_status
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_status)
    pic_label.grid(row=0,column=0,columnspan=4)

    
    text_label.grid_forget()
    text_label = Label(game_interfaace,text="What status do you want to check?",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)



    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="CHECK BASE STATUS",command=ch_status_base,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="CHECK DAMAGE",command=ch_status_skill,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="CHECK INVENTORY",command=ch_status_inventory,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=play_menu,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def ch_status_inventory():
    global pic_menu_status
    global potion_have
    global potion_effect
    global potion_name
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_status)
    pic_label.grid(row=0,column=0,columnspan=4)

    
    text_label.grid_forget()
    text_label = Label(game_interfaace,text="This is potion at inventory.",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)

    ts1 = "{}   \n Heal : {:3}      You have : {:3}".format(potion_name[0],potion_effect[0],potion_have[0])
    ts2 = "{}   \n Heal : {:3}      You have : {:3}".format(potion_name[1],potion_effect[1],potion_have[1])
    ts3 = "{}   \n Heal : {:3}      You have : {:3}".format(potion_name[2],potion_effect[2],potion_have[2])

    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text=ts1,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text=ts2,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text=ts3,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=ch_status,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def ch_status_skill():
    global pic_menu_status
    global skill_name
    global save_level
    global turn_skill
    global skill_damage
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_status)
    pic_label.grid(row=0,column=0,columnspan=4)

    
    text_label.grid_forget()
    text_label = Label(game_interfaace,text="What skill you want to check?",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)

    ts1 = "{}   turn :{}\n Lv. : {:3}      Damage : {:3}".format(skill_name[0],turn_skill[0],skill_level[0],skill_damage[0])
    ts2 = "{}   turn :{}\n Lv. : {:3}      Damage : {:3}".format(skill_name[1],turn_skill[1],skill_level[1],skill_damage[1])
    ts3 = "{}   turn :{}\n Lv. : {:3}      Damage : {:3}".format(skill_name[2],turn_skill[2],skill_level[2],skill_damage[2])

    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text=ts1,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text=ts2,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text=ts3,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=ch_status,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def ch_status_base():
    global pic_menu_status
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu_status)
    pic_label.grid(row=0,column=0,columnspan=4)


    st_show1 = "Name : {} Level : {:3}        EXP : {:3} / {:3}   Money : {:5}       Tower : {:3}        ".format(save_name[slot_check],char_status[0],char_status[1],exp_to_level_up,char_status[6],char_status[7])
    st_show2 ="\nAtk : {:3}          Magic : {:3}        Defend : {:3}       Day : {:3}".format(char_status[4],char_status[5],char_status[3],day)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text=st_show1+st_show2,height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)



    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=ch_status,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def cal_exp_up(level):
    x = (1.5**level)*10
    x = int(x)
    return x

def cal_exp_job_up(level):
    x = (2**level)*15
    return x

def story1_2st():
    global pic_story_1
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global story_run


    pic_label.grid_forget()
    pic_label = Label(image=pic_story_1)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="But princess spare dragon and let it go.",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Next",command=story2_1st,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="Back",command=story1_1st,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="    ",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="Exit",command=fist_menu_1,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def story2_1st():
    global pic_story_2
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global story_run


    pic_label.grid_forget()
    pic_label = Label(image=pic_story_2)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="The dragon fly to the forest but it lose power too much in battle.",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Next",command=story2_2st,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="Back",command=story1_2st,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="    ",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="Exit",command=fist_menu_1,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def story2_2st():
    global pic_story_2
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global story_run


    pic_label.grid_forget()
    pic_label = Label(image=pic_story_2)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="The dragon in weak form and want to training for revenge time.",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)


    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="Next",command=play_menu,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="Back",command=story2_1st,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="    ",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="Exit",command=fist_menu_1,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def fist_menu_1():
    global pic_menu
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="     ",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)

    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text="START",command=start_new,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text="CONTINUE",command=con,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text="Config",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="EXIT",command=game_interfaace.destroy,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def con():
    global pic_menu
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="     ",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)

    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text=save_name[0]+"\nLv. "+str(save_level[0]),command=bt1_to_con,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text=save_name[1]+"\nLv. "+str(save_level[1]),width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0,command=bt2_to_con)
    button_3 = Button(game_interfaace,text=save_name[2]+"\nLv. "+str(save_level[2]),width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0,command=bt3_to_con)
    button_4 = Button(game_interfaace,text="BACK",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0,command=fist_menu_1)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)

def check_savefile(num):
    global save_name
    global save_file_location
    global warning_new_save
    if save_name[num] != "Emty":
        warning_new_save = Tk()
        warning_new_save.title("Warning")
        warning_new_save.minsize(280,85)
        warning_new_save.maxsize(280,85)
        label_warning1 = Label(warning_new_save,text="You want to start new game?")
        label_warning1.grid(row=0,column=0,columnspan=2)
        label_warning2 = Label(warning_new_save,text="(Your process will gone,Do you want to continue?)")
        label_warning2.grid(row=1,column=0,columnspan=2)
        if num == 0:
            bt1_warning =Button(warning_new_save,text="OK",command=bt1_to_make)
        elif num == 1:
            bt1_warning =Button(warning_new_save,text="OK",command=bt2_to_make)
        elif num == 2:
            bt1_warning = Button(warning_new_save,text="OK",command=bt3_to_make)
        bt2_warning = Button(warning_new_save,text="CANCEL",command=warning_new_save.destroy)
        bt1_warning.grid(row=2,column=0)
        bt2_warning.grid(row=2,column=1)
        warning_new_save.mainloop()
    else :
        make_enter_save_file_name(num)
        story1_1st()

def cal_skill_1(lv):
    global skill_level
    global skill_damage
    global char_status
    x = (20+((lv-1)*15)+((char_status[5]*0.7)))
    y = int(x)
    return y

def cal_skill_2(lv):
    global skill_level
    global skill_damage
    global char_status
    x= (30+((lv-1)*8)+ (char_status[5]*0.85))
    y = int(x)
    return y


def cal_skill_3(lv):
    global save_level
    global skill_damage
    global char_status
    x = (35+((lv-1)*10) + (char_status[5]*1.2))
    y = int(x)
    return y



def make_enter_save_file_name(a):
    global in_save_name
    global slot_check
    global enter_save_name
    global block_Enter_name
    slot_check = a
    in_save_name = StringVar()
    enter_save_name = Tk()
    enter_save_name.title("Enter save name")
    enter_save_name.minsize(140,90)
    enter_save_name.maxsize(140,90)
    lable_save = Label(enter_save_name,text="Enter your save game file")
    lable_save.grid(row=0,column=0,columnspan=2)
    block_Enter_name = Entry(enter_save_name)
    block_Enter_name.focus()
    block_Enter_name.grid(row=1,column=0,columnspan=2)
    bt_ok_save_name = Button(enter_save_name,text="OK",command=ok_enter_save)
    bt_ok_save_name.grid(row=2,column=0,columnspan=2)
    enter_save_name.mainloop()

def ok_enter_save():
    global sv_name
    global block_Enter_name
    global save_name
    sv_name = block_Enter_name.get()
    save_name[slot_check] = sv_name
    sv_name = sv_name +"\n"
    enter_save_name.destroy()
    confirm_save_name()


def confirm_save_name():
    global slot_check
    global save_file_location
    global save_name
    global sv_name
    filepath = save_file_location[slot_check]
    f1 = open(filepath,"w",encoding="utf-8")
    save_name[slot_check] = sv_name
    f1.writelines(sv_name)
    f1.writelines("1\n")
    f1.writelines("0\n")
    f1.writelines("20\n")
    f1.writelines("5\n")
    f1.writelines("10\n")
    f1.writelines("5\n")
    f1.writelines("500\n")
    f1.writelines("1\n")
    f1.writelines("1\n")
    f1.writelines("1\n")
    f1.writelines("1\n")
    f1.writelines("1\n")
    f1.writelines("0\n")
    f1.writelines("0\n")
    f1.writelines("0\n")
    f1.writelines("1\n")
    f1.writelines("0\n")
    f1.writelines("0\n")
    f1.close()
    edit_status(1,0,20,5,10,5,500,1,1,1,1,1,0,0,0,1,0,0)
    story1_1st()


def edit_status(level,exp,hp,defend,atk,magic,money,tower,day,skill_1,skill_2,skill_3,potion1,potion2,potion3,lvjob,expjob,tm):
    global char_status
    global skill_level
    global exp_to_level_up
    global potion_have
    global level_job
    global exp_to_job_up
    global time
    global skill_damage
    global save_level
    exp_to_job_up = cal_exp_job_up(lvjob)
    exp_to_level_up = cal_exp_up(level)
    char_status[0] = level
    save_level[slot_check] = level
    char_status[1] = exp
    char_status[2] = hp
    char_status[3] = defend
    char_status[4] = atk
    char_status[5] = magic
    char_status[6] = money
    char_status[7] = tower
    char_status[8] = day
    skill_level[0] = skill_1
    skill_level[1] = skill_2
    skill_level[2] = skill_3
    potion_have[0] = potion1
    potion_have[1] = potion2
    potion_have[2] = potion3
    level_job[0] = lvjob
    level_job[1] = expjob
    time = tm
    skill_damage[0] = cal_skill_1(skill_1)
    skill_damage[1] = cal_skill_2(skill_2)
    skill_damage[2] = cal_skill_3(skill_3)


def check_save_con(num):
    global slot_check


    slot_check = num
    if save_name[num] != "Emty":
        filepath = save_file_location[num]
        f1 = open(filepath,"r",encoding="utf-8")
        not_save = f1.readline()
        Level = int(f1.readline())
        exp = int(f1.readline())
        hp = int(f1.readline())
        df = int(f1.readline())
        atk = int(f1.readline())
        mg = int(f1.readline())
        mn = int(f1.readline())
        tw = int(f1.readline())
        dy = int(f1.readline())
        s1 = int(f1.readline())
        s2 = int(f1.readline())
        s3 = int(f1.readline())
        p1 = int(f1.readline())
        p2 =int(f1.readline())
        p3 = int(f1.readline())
        lvjb = int(f1.readline())
        expjob = int(f1.readline())
        tm =int(f1.readline())
        f1.close()
        edit_status(Level,exp,hp,df,atk,mg,mn,tw,dy,s1,s2,s3,p1,p2,p3,lvjb,expjob,tm)
        play_menu()
    else:
        make_enter_save_file_name(num)
    
def bt1_to_con():
    check_save_con(0)

def bt2_to_con():
    check_save_con(1)

def bt3_to_con():
    check_save_con(2)


def bt1_to_make():
    warning_new_save.destroy()
    make_enter_save_file_name(0)

def bt2_to_make():
    warning_new_save.destroy()
    make_enter_save_file_name(1)

def bt3_to_make():
    warning_new_save.destroy()
    make_enter_save_file_name(2)

def bt1_to_check_save():
    check_savefile(0)

def bt2_to_check_save():
    check_savefile(1)

def bt3_to_check_save():
    check_savefile(2)


def start_new():
    global pic_menu
    global pic_label
    global text_label
    global button_1
    global button_2
    global button_3
    global button_4
    global save_name

    pic_label.grid_forget()
    pic_label = Label(image=pic_menu)
    pic_label.grid(row=0,column=0,columnspan=4)

    text_label.grid_forget()
    text_label = Label(game_interfaace,text="What save do you want to start?",height=width_heigh_bt_heigh_lb[2])
    text_label.grid(row=1,column=0,columnspan=4)

    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()

    button_1 = Button(game_interfaace,text=save_name[0]+"\nLv. "+str(save_level[0]),command=bt1_to_check_save,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_2 = Button(game_interfaace,text=save_name[1]+"\nLv. "+str(save_level[1]),command=bt2_to_check_save,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_3 = Button(game_interfaace,text=save_name[2]+"\nLv. "+str(save_level[2]),command=bt3_to_check_save,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
    button_4 = Button(game_interfaace,text="BACK",command=fist_menu_1,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=2,column=3)


pic_label = Label(game_interfaace,image=pic_menu)
pic_label.grid(row=0,column=0,columnspan=4)


text_label = Label(game_interfaace,text="   ",height=width_heigh_bt_heigh_lb[2])
text_label.grid(row=1,column=0,columnspan=4)

button_1 = Button(game_interfaace,text="START",command=start_new,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
button_2 = Button(game_interfaace,text="CONTINUE",command=con,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
button_3 = Button(game_interfaace,text=" ",width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)
button_4 = Button(game_interfaace,text="EXIT",command=game_interfaace.destroy,width=width_heigh_bt_heigh_lb[0],height=width_heigh_bt_heigh_lb[1],padx=0,pady=0)

button_1.grid(row=2,column=0)
button_2.grid(row=2,column=1)
button_3.grid(row=2,column=2)
button_4.grid(row=2,column=3)

game_interfaace.mainloop()