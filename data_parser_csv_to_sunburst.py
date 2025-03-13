
class section:
    def __init__(self, q_num, ans, sec_num, sec_name):
        self.q_num = q_num
        self.ans = ans
        self.sec_num = sec_num
        self.sec_name = sec_name
        self.div_num = '100'
        self.get_div_num()

    def get_div_num(self):
        self.div_num = self.sec_num.split(" ")[0]

    def __str__(self):
        s = f"{self.q_num},"
        s += f"{self.div_num},"
        s += f"{self.sec_num}"
        return s

def get_sec_objs():
    with open("output.csv", "r") as f:
        data = f.readlines()
    sec_li=[]
    for i, e in enumerate(data):
        if i==0:
            continue
        x = e.split(",")
        q_num = x[0]
        ans = x[1]
        sec_num = x[2]
        sec_name = x[3]
        sec = section(q_num, ans, sec_num, sec_name)
        sec_li.append(sec)
    return sec_li

def get_div_1(sec_li):
    li = '01 02 03 04 05 06 07 08 09 10 11 12 13 14 31 32 33 34'.split(' ')
    all_div_li=[]
    for div_num in li:
        div_li=[]
        for e in sec_li:
            if e.div_num == div_num:
                if e.sec_num not in div_li: #### there are many duplicates for each section
                    div_li.append(e.sec_num)
        #div_dict={div_num_: div_li}
        all_div_li.append(div_li)
    return all_div_li

def get_div_2(sec_obj_li):
    div_li=[""]
    sec_li=[]
    for e in sec_obj_li:
        div = e.sec_num.split(" ")[0]
        div_li.append(div)
        sec_li.append(e.sec_num)
    return div_li, sec_li


def driver():
    sec_obj_li = get_sec_objs()
    al_div_li = get_div_1(sec_obj_li)
    print(len(al_div_li))
    sum=0
    for i, div_li in enumerate(al_div_li):
        print(len(div_li), div_li)
    print(f"total secs = {sum}")

    (div_li, sec_li) = get_div_2(sec_obj_li)
    return (div_li, sec_li)

(div_li, sec_li) = driver()

# print(len(div_li))
# print(div_li)