
from os.path import isfile, exists
from os import sep

class Replaced:
    def __init__(self):
        self.result = ''
        self.replaced_lst = []
        self.brun = True
        self._msg = ''
    
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def get_replace_list(self, values_to_replace):
        try:
            lst = []
            for x in values_to_replace:
                if len(x.strip()) > 0:
                    lst.append(x)
            
            if len(lst) % 2 != 0:
                self._msg = '[ERROR] values to replace is an odd list'
                raise Exception

            for index in range(0, len(lst), 2):
                self.replaced_lst.append((lst[index], lst[index+1]))
        except:
            if self.msg == '':
                self._msg = '[ERROR] generic error in list with values to replace'
            raise Exception
    
    def open_file(self, load_path):
        try:
            with open(load_path, 'r') as f:
                self.result = f.readlines()
        except:
            self._msg = '[ERROR] open file'
            raise Exception

    def save_file(self, save_path):
        try:
            with open(save_path, 'w') as f:
                for _ in self.result:
                    f.write(_)
        except:
            self._msg = '[ERROR] save file'
            raise Exception

    def __replace_comma_in_dot(self):
        self.result = [ x.replace(',','.') for x in self.result]

    def __replace_semicolon_in_comma(self):
        self.result = [ x.replace(';',',') for x in self.result]

    def replace_generic_values(self, old_value, new_value):
        self.result = [ x.replace(old_value, new_value) for x in self.result]
    
    def replace_values(self):
        if len(self.replaced_lst) == 0:
            print('[WORKING] Default replace: , to .')
            self.__replace_comma_in_dot()
            print('[WORKING] Default replace: ; to ,')
            self.__replace_semicolon_in_comma()
        else:
            for _ in self.replaced_lst:
                print(f'[WORKING] Replace values: {_[0]} to {_[1]}')
                self.replace_generic_values(_[0], _[1])

    def _validate_paths(self, open_path, save_path):
        if not isfile(open_path):
            self._msg = '[ERROR] Open path does not exists'
            raise Exception

        tmp = save_path.split(sep)[:-1]
        if not exists(sep.join(tmp)):
            self._msg = '[ERROR] Save path does not exists'
            raise Exception

    def run(self, open_path, save_path):
        try:
            self._validate_paths(open_path, save_path)
            self.open_file(open_path)
            self.replace_values()
            self.save_file(save_path)
            self._msg = '[SUCCESS] Replaced was done successufully'
        except:
            raise Exception


if __name__ == '__main__':
    print('[START SCRIPT]')
    try:
        import sys
        args = sys.argv
        res = Replaced()

        if len(args) == 4:
            res.get_replace_list(args[3])
            
        elif len(args) < 3:
            res.msg = '[WARNING] needs input and output path file'
            res.brun = False

        if res.brun:
            res.run(args[1], args[2])
    except:
        if res.msg == '':
            res.msg = f'[ERROR] something was wrong: {sys.exc_info()[0]}'
    finally:
        print(res.msg)
        print('[END SCRIPT]')
