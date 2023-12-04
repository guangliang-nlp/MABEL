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

try:
    for line in  open("datasize.stereoset.log"):


            if "24464"  in line:
                continue
            print(line)

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
except: pass


with open("stereoset.bert.datasize.log",'w') as writer:
    writer.write('\n'.join(sen_list))