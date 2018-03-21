import re

re_obj = re.compile("{{(.*?)}}")
some_string = "this is a string with {{words}} embedded in {{curly brackets}} to show an {{example}} of {{regular expressions}}"


[print("MATCH->" + e) for e in re_obj.findall(some_string)]