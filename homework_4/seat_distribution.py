# TOTAL_VOTES = 4,410,052
# BLOCKING_PERCENTAGE = 3.25
SEATS = 120
DIVISOR = 1
""" or DIVISOR = 0.5 or DIVISOR = 0 """

class Party:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes
        self.seats = 0
        self.quotient = self.votes/(self.seats + DIVISOR)

    def update(self):
        self.seats = self.seats + 1
        self.quotient = self.votes/(self.seats + DIVISOR)
        
partys = [Party("מחל", 1066892), Party("פה", 614112), Party("שס", 316008), Party("כן", 292257),
          Party("ב", 273836), Party("אמת", 268767), Party("ג", 248391), Party("ל", 248370),
          Party("ט", 225641), Party("ודעם", 212583), Party("ת", 209161), Party("מרצ", 202218), Party("עם", 167064)]

"""Party("יז", 34883), Party("ר", 17346), Party("ףז", 1309), Party("כך", 1291), Party("רנ", 1189),
          Party("י", 811), Party("קץ", 729), Party("זץ", 663), Party("רף", 592), Party("קך", 514),
          Party("נ", 486), Party("ק", 463), Party("כ", 443), Party("צי", 441), Party("יק", 429),
          Party("ני", 429), Party("ינ", 408), Party("ז", 395), Party("קי", 395), Party("ץ", 385),
          Party("יר", 256), Party("צכ", 253), Party("צף", 226), Party("נר", 220), Party("יף", 196), Party("רק", 0)"""

for i in range(SEATS):
    
    """print("*** quotients ***")
    for p in partys:
        print(p.name,": ",p.quotient, sep="")
    print()"""

    max_quotient = 0
    max_party = None
    for p in partys:
        if p.quotient > max_quotient:
            max_quotient = p.quotient
            max_party = p

    Party.update(max_party)

    """print("*** distribution ***")
    for p in partys:
        print(p.name,": ",p.seats, sep="")
    print()"""

#results
for p in partys:
    print(p.name,": ",p.seats, sep="")
