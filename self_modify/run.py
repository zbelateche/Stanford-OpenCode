import importlib
import sys
import os
import self_modify

# Usage: python run.py example.py example_fun
if __name__ == '__main__':

    if(len(sys.argv) != 3):
        print("run.py takes in two inputs, the file to run and the function to run")
    else:
        # TODO: Handle arbitrary locations for files
        # TODO: Handle Windows style paths
        input_file = sys.argv[1]
        module_name = os.path.splitext(input_file)[0]
        input_func = sys.argv[2]

        # import the input file ourselves and call the function
        self_modify.init_globals()
        self_modify.user_module = importlib.import_module(module_name)
        function_to_call = getattr(self_modify.user_module, input_func)
        function_to_call()
