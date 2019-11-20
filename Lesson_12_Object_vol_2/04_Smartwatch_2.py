class UsefulStuff:
    def __init__(self, name):
        print("I'm Useful")

class Watch(UsefulStuff):
    def __init__(self):
        print("I Can check: what time is it")

class SmartWatch(Watch, Phone):
    def __init__(self):
        Watch.__init__(self)
        Phone.__init__(self)
        UsefulStuff.__init__(self)

# u = UsefulStuff()
# w = Watch()
# p = Phone()
sw = SmartWatch()


# class UsefulStuff:
#     def __init__(self, name):
#         print(name, 'is used to make life easier!')
#
#
# class Watch(UsefulStuff):
#     def __init__(self, watch_name):
#         print(watch_name, "is small and convenient")
#         super().__init__(watch_name)
#
#
# class Phone(UsefulStuff):
#     def __init__(self, phone_name):
#         print(phone_name, "can make a call")
#         super().__init__(phone_name)
#
#
# class SmartWatch(Watch, Phone):
#     def __init__(self):
#         print('Smartwatch is great!')
#         super().__init__('Smartwatch')