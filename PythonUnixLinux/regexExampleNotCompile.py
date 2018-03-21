import re

re_string = "{{(.*?)}}"
some_string = "this is a string with {{words}} embedded in {{curly brackets}}"


[print("MATCH->" + match) for match in re.findall(re_string, some_string)]