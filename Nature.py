import sqlite3
import time
import sys
#rabbit starves if rabbit hunger = 0 for 3 days
#for procreate settings if a rabbit has a procreate rate of 70 then we do if rabbit gets >30 they procreate
min = 0
hour = 0

day = 0
N_rabbits = 1000
N_fox = 1000
def start_simulation():
    global set
    min = 0
    hour = 0
    day = 0
    while start == True:
        for i in range(61):
            time_string = time.strftime("%S")
            f = (int(time_string))
            time.sleep(1)
            time_check = time.strftime("%S")
            a = (int(time_check))

            if f + 1 == a:
                print(i)
                min

            if i*setter >= 60:
                eq = i / 60
                min = (min + eq )
                min = (min * set)
                print("min", min)

            if min >= 60:
                hour = (hour +1)
                print("hour:",hour)
                S_check()
                Starve()
                Eat()
                F_check()
                min = min-60
            if hour ==18:
                print("Animals are sleeping")
            if hour == 24:
                day = (day +1)
                print("day",day)
                hour = hour - 24


import random

#we choose if rabbit finds food by using random and rabbits with higher frailty have a larger random set
#example rand.int(1,100) for very frail rabbits and for healthy rabbits rand.int(50,100) whoever gets closest to 100 gets food
#make a loop that chooses the amount of rabbits that will randomly find food so loop selecting a random rabbit and keep doing so till food runs out
connect = sqlite3.connect("Nature.db")
c = connect.cursor()

def create_table():
    c.execute("""CREATE TABLE rabbit (
                      id text,
                      Age integer,
                      Frailty integer,
                      Gender text,
                      Fertility integer,
                      Hunger integer
                      Speed integer
                      )""")
    c.execute("""CREATE TABLE Fox ( 
                         id text,
                         Age integer,
                         Frailty integer,
                         Gender text,
                         Fertility integer,
                         Hunger integer
                         )""")
    c.execute("""CREATE TABLE World ( 
                             Year integer,
                             Month Integer
                             Season text,
                             Time real,
                             Food integer
                             )""")


class World:
    def __init__(self,Years,Month,Time,Weather,Food_A):
        self.Years = Years
        self.Weather = Weather
        self.Food_A = Food_A
        self.Month = Month
        self.Time = Time

class Animals:
    def __init__(self,Age,Frailty,Gender,Fertility,Hunger,id):
        self.Age = Age
        self.Frailty = Frailty
        self.Gender = Gender
        self.Fertility = Fertility
        self.Hunger = Hunger
        self.id = id

World1 = World(0,0,0,0,3)

# 1 = male 2 = female

def Reset_Rabbits():
        global N_rabbits
        DEL = input("WOULD U LIKE TO DELETE PAST DATA")
        if DEL == "yes":
            for i in range(1,1000):
                f = 1+i
                af = str(f)
                c.execute("DELETE FROM rabbit WHERE id =?", (af,))

        for i in range(1000):
            f = 1 + i
            Gender = random.randint(1, 2)

            Rabbit = Animals(0, 100, Gender, 20, 20, f)
            Rg = (str(Rabbit.Gender))
            Ra = (str(Rabbit.Age))
            Rfr = (str(Rabbit.Fertility))
            Rf = (str(Rabbit.Frailty))
            Ri = (str(Rabbit.id))
            Rh = (str(Rabbit.Hunger))
            S_RabID = (str(Rabbit.id))
            f = 1 + i

            c.execute("INSERT INTO rabbit VALUES (?,?,?,?,?,?)", (Ri, Ra, Rf, Rg, Rfr, Rh))
            connect.commit()

def Reset_Foxes():
    for i in range(1000):
        f = 1 + i
        Gender = random.randint(1, 2)

        Fox = Animals(0, 100, Gender, 20, 20, f)
        Fg = (str(Fox.Gender))
        Fa = (str(Fox.Age))
        Ffr = (str(Fox.Fertility))
        Ff = (str(Fox.Frailty))
        Fi = (str(Fox.id))
        Fh = (str(Fox.Hunger))
        S_RabID = (str(Fox.id))
        f = 1 + i

        c.execute("INSERT INTO Fox VALUES (?,?,?,?,?,?)", (Fi, Fa, Ff, Fg, Ffr, Fh))
        connect.commit()



def load_rabbit():
    id = input("which rabbit do you want to look at")
    c.execute("SELECT * FROM rabbit WHERE id=? ",(id))
    print(c.fetchall())
def Eat():
    Food_scarcity = World1.Food_A
    for i in range(Food_scarcity):

        var = random.randint(1, 100)

        id = str(var)
        c.execute("SELECT Hunger FROM rabbit WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1] + oak[2]

        int_string = int(u_string)
        eaten = int_string + 20
        print(eaten)

        c.execute("UPDATE rabbit SET Hunger=? WHERE id=? ", (eaten, id,))
        print("rabbit", id, "has eaten")

def procreateR():

    global N_rabbits
    x = random.randint(4,12)
    for i in range(x):

        Gender = random.randint(1, 2)

        Rabbit = Animals(0, 100, Gender, 0, 20, N_rabbits+1)
        Rg = (str(Rabbit.Gender))
        Ra = (str(Rabbit.Age))
        Rfr = (str(Rabbit.Fertility))
        Rf = (str(Rabbit.Frailty))
        Ri = (str(Rabbit.id))
        Rh = (str(Rabbit.Hunger))
        S_RabID = (str(Rabbit.id))


        c.execute("INSERT INTO rabbit VALUES (?,?,?,?,?,?)", (Ri, Ra, Rf, Rg, Rfr, Rh))
        connect.commit()

#hunger check everyday and it takes all rabbits with hunger 0 and takes there ids and adds a nrxt to it on the first day if that number gets up to 3 it dies
def S_check():
    global N_rabbits
    for i in range(1, N_rabbits):
        var = i


        id = str(var)
        c.execute("SELECT Hunger FROM rabbit WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1] + oak[2]

        int_string = int(u_string)
        if int_string == 0:

            print("rabbit", id, "Has died :(")
            c.execute("DELETE FROM rabbit WHERE id =?", (id))
            N_rabbits =N_rabbits - 1
            connect.commit()






def F_check():

    global N_rabbits
    for i in range(1,N_rabbits+1):
        var = i

        id = str(var)
        c.execute("SELECT Fertility FROM rabbit WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1] + oak[2]

        int_string = int(u_string)

        #change this its a copy from starve so make if statement for if fertile procreate
        x = random.randint(1,100)
        if x > int_string:
            procreateR()
            print("rabbit", id, "a new rabbit is born")
            c.execute("UPDATE rabbit SET Fertility=? WHERE id=? ", (0, id,))
            N_rabbits = N_rabbits +1



        connect.commit()
def Starve():

    import sqlite3
    import random

    for i in range(1,N_rabbits):
        var = i

        id = str(var)
        c.execute("SELECT Hunger FROM rabbit WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1] + oak[2]

        int_string = int(u_string)
        eaten = int_string - 1


        c.execute("UPDATE rabbit SET Hunger=? WHERE id=? ", (eaten, id,))
        print("rabbit", id, "grows hungry")
        connect.commit()
#*****************************************************FOXES*************************************************************
def Eat_Rab():
        global N_rabbits
        F_val = random.randint(1,1000)
        id = str(F_val)
        var = c.execute("SELECT id=? FROM Fox ", (id,))


        c.execute("SELECT Hunger FROM Fox WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1]+oak[2]

        int_string = int(u_string)
        R_id = random.randint(1,N_rabbits)


        c.execute("DELETE FROM rabbit WHERE id =?", (R_id))
        N_rabbits = N_rabbits - 1
        eaten = int_string + 20
        print(eaten)
        c.execute("UPDATE Fox SET Hunger=? WHERE id=? ", (eaten, id,))
        print("Fox", id, "has eaten")
        print("rabbit",R_id,"Has eaten")
        connect.commit()
def load_rabbit():
    id = input("which rabbit do you want to look at")
    c.execute("SELECT * FROM rabbit WHERE id=? ",(id))
    print(c.fetchall())
def Eat():
    Food_scarcity = World1.Food_A
    for i in range(Food_scarcity):

        var = random.randint(1, 100)

        id = str(var)
        c.execute("SELECT Hunger FROM rabbit WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1] + oak[2]

        int_string = int(u_string)
        eaten = int_string + 20
        print(eaten)

        c.execute("UPDATE rabbit SET Hunger=? WHERE id=? ", (eaten, id,))
        print("rabbit", id, "has eaten")



        c.execute("SELECT Hunger FROM rabbit WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1] + oak[2]

        int_string = int(u_string)
        eaten = int_string + 20
        print(eaten)

        c.execute("UPDATE rabbit SET Hunger=? WHERE id=? ", (eaten, id,))
        print("rabbit", id, "has eaten")


def procreateR():

    global N_rabbits
    x = random.randint(4,12)
    for i in range(x):

        Gender = random.randint(1, 2)

        Rabbit = Animals(0, 100, Gender, 0, 20, N_rabbits+1)
        Rg = (str(Rabbit.Gender))
        Ra = (str(Rabbit.Age))
        Rfr = (str(Rabbit.Fertility))
        Rf = (str(Rabbit.Frailty))
        Ri = (str(Rabbit.id))
        Rh = (str(Rabbit.Hunger))
        S_RabID = (str(Rabbit.id))


        c.execute("INSERT INTO rabbit VALUES (?,?,?,?,?,?)", (Ri, Ra, Rf, Rg, Rfr, Rh))
        connect.commit()

#hunger check everyday and it takes all rabbits with hunger 0 and takes there ids and adds a nrxt to it on the first day if that number gets up to 3 it dies
def F_S_check():
    global N_rabbits
    for i in range(1, N_rabbits):
        var = i


        id = str(var)
        c.execute("SELECT Hunger FROM rabbit WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1] + oak[2]

        int_string = int(u_string)
        if int_string == 0:

            print("rabbit", id, "Has died :(")
            c.execute("DELETE FROM rabbit WHERE id =?", (id))
            N_rabbits =N_rabbits - 1
            connect.commit()






def F_F_check():

    global N_rabbits
    for i in range(1,N_rabbits+1):
        var = i

        id = str(var)
        c.execute("SELECT Fertility FROM Fox WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1] + oak[2]

        int_string = int(u_string)

        #change this its a copy from starve so make if statement for if fertile procreate
        x = random.randint(1,100)
        if x > int_string:
            procreateR()
            print("rabbit", id, "a new rabbit is born")
            c.execute("UPDATE rabbit SET Fertility=? WHERE id=? ", (0, id,))
            N_rabbits = N_rabbits +1



        connect.commit()
def F_Starve():


    for i in range(1,N_rabbits):
        var = i

        id = str(var)
        c.execute("SELECT Hunger FROM Fox WHERE id=?", (id,))

        oak = (str(c.fetchone()))

        st = "".join(oak)

        u_string = oak[1] + oak[2]

        int_string = int(u_string)
        eaten = int_string - 1


        c.execute("UPDATE Fox SET Hunger=? WHERE id=? ", (eaten, id,))
        print("Fox", id, "grows hungry")
        connect.commit()


New = input("***IF THIS IS A NEW PC TYPE new***")

if New == "new":
    create_table()
Reset = input("***would u like to reset all of your rabbits if so type Reset***")
if Reset == "Reset":
    Reset_Rabbits()
Reset_F = input("***would u like to reset all of your foxes if so type Reset***")
if Reset_F == "Reset":
    Reset_Foxes()
choice = input("1.would you like to check a rabbits stats \n 2.woulld you like to change \n 3.view the Simulation the  rabbits are in \nor type start to begin the simulation")


if choice == "start":
    start = True
    seter = input("1.if you would like to speed up the simulation type the number u would like to speed it it up buy ")
    setter = int(seter)
    if setter > 0:
        set = 0 + setter
    if setter == 0:
        set = 1
    start_simulation()

connect.commit()
connect.close()