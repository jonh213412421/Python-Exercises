#simple prompt calculator
import sys

class calc:
    def eval_func(self):
        func = sys.argv[2] #receives args
        result = eval(func) #eval string
        return result
    def eval_func_file(self):
        self.file = sys.argv[2]
        with open(self.file, "r") as f:
            func = f.read() #read args from file
            f.close()
        result = eval(func) #eval string
        return result

if __name__ == "__main__":
    method = sys.argv[1]
    if method == "eval_file":
        if len(sys.argv) < 2:
            print("insuficient args")
        result = calc().eval_func_file() #eval file
        print(result)
    if method == "eval_func":
        if len(sys.argv) < 2:
            print("insuficient args")
        result = calc().eval_func() #eval func
        print(result)
