import pandas as pd
import numpy as np
import json

class QuestionSection:
    def __init__(self, n:int, desc: str, answer: str, sec_num_li, sec_name_li):
        self.q_num = n
        self.desc=desc.split("\n")[0]
        self.answer_val = answer.replace(" ", "")
        self.answer_val = self.answer_val.replace(",", "_")
        self.answer_val = self.answer_val.replace("/", "_")
        self.answer_val = self.answer_val.strip()
        self.sec_num_li=sec_num_li
        self.sec_name_li=sec_name_li
        self.sec_li_connected=[]
    def __str__(self):
        a = f"q-num= {self.q_num}\ndesc= {self.desc}\nans= {self.answer_val}\nsec_num_li= {self.sec_num_li}\nsec_name_li= {self.sec_name_li}\n"
        return a
    def get_dict(self):
        r={}
        r["q_num"] =  self.q_num
        r["desc"] =  self.desc
        r["ans"] = self.answer_val
        r["sec_num_li"] = self.sec_num_li
        r["sec_name_li"] = self.sec_name_li
        return r
    def get_csv(self):
        s=""
        for e,f in zip(self.sec_num_li, self.sec_name_li):
            s += f"{self.q_num},{self.answer_val},{e},{f}\n"
        return s

def init():
    filename = INPUT_FILENAME
    df = pd.read_csv(filename)
    # df.info
    # df.columns
    sec_nums_cols = df['Section Number'].fillna('0').tolist() # we need this
    sec_names_cols = df['Section Name'].fillna('0').tolist() # we need this 
    all_sec_li=[]  # we need this = 29
    for num, name in zip(sec_nums_cols, sec_names_cols):
        all_sec_li.append({"num": num, "name": name})
    #
    # cols  d, e, f
    conn1_cols = df['Other section that always accompanies this one (1)'].fillna('0').tolist() # we need this 
    conn2_cols = df['Other section that always accompanies this one (2)'].fillna('0').tolist() # we need this 
    conn3_cols = df['Other section that always accompanies this one (3)'].fillna('0').tolist() # we need this 
    #
    secs_every_project_cols = df["Every Project"].fillna('0').tolist() # this will be 595
    sec_nums_every_project=[] # we need this = 29
    for i, e in enumerate(secs_every_project_cols):
        if e != '0':
            sec_num = sec_nums_cols[i]
            sec_nums_every_project.append(sec_num)

    return sec_nums_cols, sec_names_cols, all_sec_li, sec_nums_every_project, conn1_cols, conn2_cols, conn3_cols

def check_all_sec_nums(secs_in_every_project, sec_num_li):
    x=[]
    for e in secs_in_every_project:
        if e not in sec_num_li and e != "0":
            x.append(e)
    return x  

def get_sec_name_from_num(num):
    index = -1
    for i, e in enumerate(SEC_NUMS_COLS):
        if num == e:
            index = i
            return True, SEC_NAMES_COLS[index]
    return False, None

def get_question_sections_obj_csv(secs_in_every_project, sec_nums, q_num, q_desc, ans):
    filename = "mw_spec_toc_updated.csv"
    df = pd.read_csv(filename)
    q_li = df[q_desc].fillna('0').tolist()
    count=0
    sec_count = 0
    sec_num_li=[]
    sec_name_li=[]
    for num, q1 in zip(sec_nums, q_li):
        if q1 != '0':
            t, name = get_sec_name_from_num(num)
            if t==True:
                sec_num_li.append(num)
                sec_name_li.append(name)
            sec_count +=1 
        count += 1
    # get names for all sections
    # x = check_all_sec_nums(secs_in_every_project, sec_num_li) # array of sections in all projects
    # for e in x:
    #     (t, name) = get_sec_name_from_num(e)
    #     if t == True:
    #         sec_name_li.append(name)
    #         sec_num_li.append(e)
    q = QuestionSection(q_num, q_desc, ans, sec_num_li, sec_name_li)
    # return q.get_dict()
    return q.get_csv()


# col G, H, I
def ask_question_1():
    all_question_sections = []
    # col G
    q1_desc_1 = """Is the project a new building,  addition/renovation or renovation?\nNew Building"""
    ans = "New Building"
    Q1_1 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 1, q1_desc_1, ans)
    all_question_sections.append(Q1_1)
    # 
    # col H
    q1_desc_2 = """Is the project a new building, addition/renovation or renovation?\nAddition/Renovation"""
    ans2 = "Addition_Renovation"
    Q1_2 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 1, q1_desc_2, ans2)
    all_question_sections.append(Q1_2)
    #
    # col I
    q1_desc_3 = """Is the project a new building, addition/renovation or renovation?\nRenovation"""
    ans3 = "Renovation"
    Q1_3 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 1, q1_desc_3, ans3)
    all_question_sections.append(Q1_3)
    return all_question_sections



# col K
def ask_question_2():
    all_question_sections = []
    # col K
    q3_desc = """Does the project require demolition?\nYes"""
    ans = "Yes"
    Q2 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 2, q3_desc, ans)
    all_question_sections.append(Q2)
    return all_question_sections


# col L, M
def ask_question_3():
    all_question_sections =[]
    # col L
    q3_desc_1 = """Is the project multiple stories?\nYes (New Building, Addition, Addition/Renovation)"""
    ans = "Yes, New Building, Addition, Addition/Renovation"
    Q3_1 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 3, q3_desc_1, ans)
    all_question_sections.append(Q3_1)

    # col M
    q3_desc_2 = """Is the project multiple stories?\nYes (Renovation)"""
    ans = "Yes, Renovation"
    Q3_2 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 3, q3_desc_2, ans)
    all_question_sections.append(Q3_2)
    return all_question_sections


# col M, N, O, P, R, S, T, U, V
def ask_question_4():
    all_question_sections = []
    # col M
    q4_desc_1 = """What are the opaque exterior materials? (Select as many as applicable)\nMasonry"""
    ans = "Masonry"
    Q4_1 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_1, ans)
    all_question_sections.append(Q4_1)

    # col N
    q4_desc_2 = """What are the opaque exterior materials? (Select as many as applicable)\nStone"""
    ans = "Stone"
    Q4_2 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_2, ans)
    all_question_sections.append(Q4_2)

    # col O
    q4_desc_3 = """What are the opaque exterior materials? (Select as many as applicable)\nMetal Panel"""
    ans = "Metal Panel"
    Q4_3 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_3, ans)
    all_question_sections.append(Q4_3)

    # col P
    q4_desc_4 = """What are the opaque exterior materials? (Select as many as applicable)\nFiber Cement Panel"""
    ans = "Fiber Cement Panel"
    Q4_4 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_4, ans)
    all_question_sections.append(Q4_4)

    # col Q
    q4_desc_5 = """What are the opaque exterior materials? (Select as many as applicable)\nTerra Cotta"""
    ans = "Terra Cotta"
    Q4_5 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_5, ans)
    all_question_sections.append(Q4_5)

    # col R
    q4_desc_6 = """What are the opaque exterior materials? (Select as many as applicable)\nPhenolic Panel"""
    ans = "Phenolic Panel"
    Q4_6 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_6, ans)
    all_question_sections.append(Q4_6)

    # col S
    q4_desc_7 = """What are the opaque exterior materials? (Select as many as applicable)\nEIFS"""
    ans = "EIFS"
    Q4_7 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_7, ans)
    all_question_sections.append(Q4_7)

    # col T
    q4_desc_8 = """What are the opaque exterior materials? (Select as many as applicable)\nPrecast Concrete"""
    ans = "Precast Concrete"
    Q4_8 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_8, ans)
    all_question_sections.append(Q4_8)

    # col U
    q4_desc_9 = """What are the opaque exterior materials? (Select as many as applicable)\nCast Stone"""
    ans = "Cast Stone"
    Q4_9 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_9, ans)
    all_question_sections.append(Q4_9)

    # col V
    q4_desc_10 = """What are the opaque exterior materials? (Select as many as applicable)\nArchitectural Concrete"""
    ans = "Architectural Concrete"
    Q4_10 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 4, q4_desc_10, ans)
    all_question_sections.append(Q4_10)
    return all_question_sections

# col W
def ask_question_5():
    all_question_sections=[]
    
    # col W
    q5_desc_1 = """Do you have CMU backup for the opaque exterior walls?\nYes"""
    ans = "CMU"
    Q5_1 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 5, q5_desc_1, ans)
    all_question_sections.append(Q5_1)

    return all_question_sections


# col X, Y, Z, AA, AB
def ask_question_6():
    all_question_sections=[]

    # col X
    q6_desc_1 = """What are the anticipated floor finishes? (Select as many as applicable)\nCarpet"""
    ans = "Carpet"
    Q6_1 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 6, q6_desc_1, ans)
    all_question_sections.append(Q6_1)

    # col Y
    q6_desc_2 = """What are the anticipated floor finishes? (Select as many as applicable)\nResilient Flooring"""
    ans = "Resilient Flooring"
    Q6_2 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 6, q6_desc_2, ans)
    all_question_sections.append(Q6_2)

    # col Z
    q6_desc_3 = """What are the anticipated floor finishes? (Select as many as applicable)\nTile"""
    ans = "Tile"
    Q6_3 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 6, q6_desc_3, ans)
    all_question_sections.append(Q6_3)

    # col AA
    q6_desc_4 = """What are the anticipated floor finishes? (Select as many as applicable)\nWood"""
    ans = "Wood"
    Q6_4 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 6, q6_desc_4, ans)
    all_question_sections.append(Q6_4)

    # col AB
    q6_desc_5 = """What are the anticipated floor finishes? (Select as many as applicable)\nTerrazzo"""
    ans = "Terrazzo"
    Q6_5 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 6, q6_desc_5, ans)
    all_question_sections.append(Q6_5)

    return all_question_sections


# col AC, AD, AE, AF
def ask_question_7():
    all_question_sections=[]

    # col AC
    q7_desc_1 = """Are there any special ceiling materials? (Select as many as applicable)\nAcoustical Gypsum Board"""
    ans81 = "Acoustical Gypsum Board"
    Q7_1 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 7, q7_desc_1, ans81)
    all_question_sections.append(Q7_1)

    # col AD
    q7_desc_2 = """Are there any special ceiling materials? (Select as many as applicable)\nAcoustical Baffles"""
    ans82 = "Acoustical Baffles"
    Q7_2 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 7, q7_desc_2, ans82)
    all_question_sections.append(Q7_2)

    # col AE
    q7_desc_3 = """Are there any special ceiling materials? (Select as many as applicable)\nWood"""
    ans83 = "Wood"
    Q7_3 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 7, q7_desc_3, ans83)
    all_question_sections.append(Q7_3)

    # col AF
    q7_desc_4 = """Are there any special ceiling materials? (Select as many as applicable)\nMetal"""
    ans84 = "Metal"
    Q7_4 = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 7, q7_desc_4, ans84)
    all_question_sections.append(Q7_4)

    return all_question_sections


def get_every_sections_for_every_project():
    all_question_sections=[]
    # col AC
    q = """Every Project"""
    ans = "Every_Project"
    Q_ = get_question_sections_obj_csv(SEC_NUMS_EVERY_PROJECT, SEC_NUMS_COLS, 0, q, ans)
    all_question_sections.append(Q_)

    return all_question_sections


def question_driver():
    all_question_sections = {}
    all_question_sections["q0"] = get_every_sections_for_every_project()
    all_question_sections["q1"] = ask_question_1()
    all_question_sections["q2"] = ask_question_2()
    all_question_sections["q3"] = ask_question_3()
    all_question_sections["q4"] = ask_question_4()
    all_question_sections["q5"] = ask_question_5()
    all_question_sections["q6"] = ask_question_6()
    all_question_sections["q7"] = ask_question_7()
    return all_question_sections


def question_driver_csv():
    arr=[]
    arr += get_every_sections_for_every_project()
    arr += ask_question_1()
    arr += ask_question_2()
    arr += ask_question_3()
    arr += ask_question_4()
    arr += ask_question_5()
    arr += ask_question_6()
    arr += ask_question_7()
    write_csv_to_file(arr)

    
def add_connected_sections(x):
    for k, v in x.items():
        print("\n\n" + k)
        for e in v:
            # print(e['q_num'], e['desc'], )
            nums =e['sec_num_li']
            names =e['sec_name_li']
            for i, j in zip(nums, names):
                print(i, j)

def write_to_file(y):
    with open("output.json", "w") as f:
        f.write(json.dumps(y, indent=4))


def write_csv_to_file(arr):
    s="q_num,answer,sec_num,sec_name\n"
    for sub_q in arr:
        e = sub_q
        s += e
    fn = OUTPUT_FILENAME
    with open(fn, "w") as f2:
        f2.write(s)

##################################################
#
#                   driver
#
####################################################

INPUT_FILENAME = "mw_spec_toc_updated.csv"
# OUTPUT_FILENAME = "output_updated.csv"
OUTPUT_FILENAME = "output_updated_separation.csv"
(SEC_NUMS_COLS, SEC_NAMES_COLS, ALL_SEC_LI, SEC_NUMS_EVERY_PROJECT, CONN1_COLS, CONN2_COLS, CONN3_COLS) = init()
question_driver_csv()


