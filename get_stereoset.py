import os

ratios = ['0.0','0.25','0.5','0.75','1.0']
tasks = ['mnli','jigsaw-gender','snli']
models = ['bert-base-uncased','roberta-base']
methods = ['vanillia','debiased']

if __name__ == "__main__":


    prefix = "/scratch0/liuguan5/models/cda/iclr24/"


    for ratio in ratios:
        for task in tasks:
            for model in models:
                for method in methods:
                    model_file = prefix + 'biasdis.'+str(ratio)+"."+task+"."+model+"."+method+".{}.ckpt"

                    print(model_file)
                    os.system("")
