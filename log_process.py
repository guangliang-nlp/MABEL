"""
sen_list = []
sen = ""
for line in open("crowspair.log"):

    if line.strip().startswith("/scratch0/liuguan5/models/cda/"):
        sen = sen + line.strip().split("/")[-1]
        #print(sen)

    elif line.strip().startswith("Metric score"):
        score = line.strip().split(":")[-1].strip()
        print(line,score)
        sen = sen + "\t" + score
        sen_list.append(sen)
        sen = ""

with open("crowspair.score.log",'w') as writer:
    writer.write('\n'.join(sen_list))

"""

sen_list = []
sen=""
for line in open("stereoset.bert.log"):

    if line.strip().startswith("/scratch0/liuguan5/models/cda/"):
        sen = sen + line.strip().split("/")[-1]
        #print(sen)

    elif line.strip().startswith("LM Score"):
        score = line.strip().split(":")[-1].strip()

        sen = sen + "\t" + score

    elif line.strip().startswith("SS Score"):
        score = line.strip().split(":")[-1].strip()
        sen = sen + "\t" + score
        sen_list.append(sen)
        sen = ""

with open("stereoset.bert.score.log",'w') as writer:
    writer.write('\n'.join(sen_list))