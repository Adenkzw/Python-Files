from InhChefEG import Chef

class ChineseChef(Chef):
    def make_special_dish(self):#overwrites the prev special dish of the chef (bbq ribs)
        print('The Chef makes orange chicken')
    def make_fried_rice(self):
        print('The Chef makes fried rice')