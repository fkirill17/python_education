def avd_deco_inner(**gkwargs):
    def avd_deco(my_class):
        def inner(*args, **kwargs):
            if gkwargs['password'] == '1337':
                return my_class(*args, **kwargs)
            else:
                print('Wrong password')

        return inner
    return avd_deco


@avd_deco_inner(password='13372')
# avd_deco
class MyClass:
    pass


obj = MyClass()

if obj:
    print(type(obj))
else:
    print('none obj')
