'''
amy = {
	  "Name": "Amy",
	  "Final Assessment": 74,
	  "Second Test": 72,
	  "First Test": 68
}

def show_grades(student, *pog, grades):
	   print("Student record for {}: ".format(student))

	   for key, value in grades.items():
		        print("{} earned a grade of {} in their {}.".format(student, value, key))

'''

import os, argparse
'''parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store_true')
parser.add_argument('dir', nargs='?', default=os.getcwd())
parser.parse_args('somedir -v'.split())
parser.parse_args('-v'.split())
parser.parse_args(''.split())
parser.parse_args(['somedir'])
parser.parse_args('somedir -h -v'.split())'''


'''def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)'''


'''def f (a=None, **kwargs):
    print(a)


dct2 = {"a":"Foo", "b":"Bar"}
f(**dct2)

import inspect
def filter_dict(dict_to_filter, thing_with_kwargs):
    sig = inspect.signature(thing_with_kwargs)
    filter_keys = [param.name for param in sig.parameters.values() if param.kind == param.POSITIONAL_OR_KEYWORD]
    filtered_dict = {filter_key:dict_to_filter[filter_key] for filter_key in filter_keys}
    return filtered_dict

def myfunc(x=0):
    print(x)
mydict = {'x':2, 'y':3}
filtered_dict = filter_dict(mydict, myfunc)
myfunc(**filtered_dict) # 2
myfunc(x=3) # 3'''

#def f(**kwargs):
#    print(kwargs['b'])

#f(grid=13, b=55)

def f(a='default_a', KFC='', **kwargs):
    print(a)
    print(KFC)
   

f(b=44, e=12, KFC=1,d=3, a=4)
f(c=33)
