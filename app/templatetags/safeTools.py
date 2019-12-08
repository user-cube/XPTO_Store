from django import template

register = template.Library()


@register.filter(name='spliter')
def spliter(value):
    value = str(value).split('/')[1:]
    a = "../"
    counter = 0
    for i in value[0:len(value)]:
        a = a + i
        if len(value) > counter:
            a = a + '/'
        counter += 1
    return a[:-1]
