
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

    def driver(self):
        SEC_LI = self.get_sec_objs()
        ALL_DIV_LI = self.get_div_1(SEC_LI)

    def get_sec_objs(self):
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

    def get_div_1(self, sec_li):
        li = '01 02 03 04 05 06 07 08 09 10 11 12 13 14 31 32 33 34'.split(' ')
        all_div_li=[]
        for div_num in li:
            div_li=[]
            div_num_=None
            div_num_=div_num
            for e in sec_li:
                if e.div_num == div_num:
                    if e.sec_num not in div_li: #### there are many duplicates for each section
                        div_li.append(e.sec_num)
            div_dict={div_num_: div_li}
            all_div_li.append(div_dict)
        return all_div_li


def driver():
    SEC_LI = get_sec_objs()
    ALL_DIV_LI = get_div_1(SEC_LI)
    # print(len(ALL_DIV_LI))
    # sum=0
    # for i, div_di in enumerate(ALL_DIV_LI):
    #     for k, v in div_di.items():
    #         sum += len(v)
    #         print(f"{k}  has {len(v)} elements")
    #         print(k, v)
    # print(f"total secs = {sum}")