#!/usr/bin/python3
'''Defines the working of HBnB console'''
import cmd
import re
import sys
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity


def parse(arg):
    '''
    Method that splits the args str into a list of strings,
    and then appends the curly braces or brackets at the end of the
    list
    '''
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [n.strip(",") for n in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            ret_len = [n.strip(",") for n in lexer]
            ret_len.append(brackets.group())
            return ret_len
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        ret_len = [n.strip(",") for n in lexer]
        ret_len.append(curly_braces.group())
        return ret_len


class HBNBCommand(cmd.Cmd):
    '''Defines the HBnB command interpreter

        Attributes:
            prompt (str): Command prompt
    '''
    prompt = "(hbnb) "

    class_names = {
            "BaseModel": BaseModel,
            "User": User, "State": State,
            "City": City, "Amenity": Amenity,
            "Place": Place, "Review": Review
            }

    def emptyline(self):
        '''When empty line is received do nothing'''
        pass

    def default(self, arg):
        '''
        Receives str but handles the cmd module by default if invalid input
        '''
        dictionary_args = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        to_match = re.search(r"\.", arg)
        if to_match is not None:
            arg_one = [arg[:to_match.span()[0]], arg[to_match.span()[1]:]]
            to_match = re.search(r"\((.*?)\)", arg_one[1])
            if to_match is not None:
                command = [arg_one[1][:to_match.span()[0]],
                           to_match.group()[1:-1]]
                if command[0] in dictionary_args.keys():
                    call = "{} {}".format(arg_one[0], command[1])
                    return dictionary_args[command[0]](call)
        print("Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        '''Command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''End of File EOF command to exit program'''
        print()
        exit()

    def help_EOF(self):
        '''Help documentation for EOF'''
        print("Exits the program without formatting\n")

    def do_create(self, arg):
        '''Creates a new instance of BaseModel and prints its id'''

        arg_len = parse(arg)
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
        else:
            print(eval(arg_len[0])().id)
            storage.save()

    def do_show(self, arg):
        '''
        Prints the string representation of an instance based
        on the class name and id
        Usage: show <class> <id> or <class>.show(<id>)
        '''
        arg_len = parse(arg)
        dictionary_obj = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
        elif len(arg_len) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_len[0], arg_len[1]) not in dictionary_obj:
            print("** no instance found **")
        else:
            print(dictionary_obj["{}.{}".format(arg_len[0], arg_len[1])])

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        '''
        arg_len = parse(arg)
        dictionary_obj = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
        elif len(arg_len) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_len[0], arg_len[1])
        not in dictionary_obj.keys():
            print("** no instance found **")
        else:
            del dictionary_obj["{}.{}".format(arg_len[0], arg_len[1])]
            storage.save()

    def do_all(self, arg):
        '''
        Prints all string representation of all instances based
        or not on the class name
        Usage: all or all <class> or <class>.all()
        '''
        arg_len = parse(arg)
        if len(arg_len) > 0 and arg_len[0] not in
        HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
        else:
            obj_len = []
            for obj in storage.all().values():
                if len(arg_len) > 0 and arg_len[0] == obj.__class__.__name__:
                    obj_len.append(obj.__str__())
                elif len(arg_len) == 0:
                    obj_len.append(obj.__str__())
            print(obj_len)

    def do_count(self, arg):
        '''
        Counts the number of objects of a given class
        Usage: count <class> or <class>.count()
        '''
        arg_one = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_one[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id by adding or
        updating attribute
        Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        '''
        arg_len = parse(arg)
        dictionary_obj = storage.all()

        if len(arg_len) == 0:
            print("** class name missing **")
            return False
        if arg_len[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return False
        if len(arg_len) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_len[0], arg_len[1]) not in dictionary_obj.keys():
            print("** no instance found **")
            return False
        if len(arg_len) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_len) == 3:
            try:
                type(eval(arg_len[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_len) == 4:
            obj = dictionary_obj["{}.{}".format(arg_len[0], arg_len[1])]
            if arg_len[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_len[2]])
                obj.__dict__[arg_len[2]] = valtype(arg_len[3])
            else:
                obj.__dict__[arg_len[2]] = arg_len[3]
        elif type(eval(arg_len[2])) == dict:
            obj = dictionary_obj["{}.{}".format(arg_len[0], arg_len[1])]
            for key, value in eval(arg_len[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in
                        {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
