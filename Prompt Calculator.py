#simple prompt calculator
import sys

class calc:
    def eval_func(self):
        if len(sys.argv) < 3: #checks args
            print("Insuficient args")
        else:
            func = sys.argv[2] #gets func as string
            result = eval(func) #evals string
            print(result)
            return result
    def eval_func_file(self):
        if len(sys.argv) < 3:
            print("Insuficient args")
        else:
            self.file = sys.argv[2] #gets path to file
            with open(self.file, "r") as f:
                func = f.read() #read string expression to func
                f.close()
            result = eval(func) #eval func
            print(result)
            return result

if __name__ == "__main__":
    method = sys.argv[1]
    if method == "eval_file":
        result = calc().eval_func_file()
    if method == "eval_func":
        result = calc().eval_func()
