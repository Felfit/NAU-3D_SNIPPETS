

import sys
import json

f = open("NAU_COMPONENTS.json","r")

j = json.load(f)

arr = j["arr"]


snip = {}

for type in arr:
    print(type["name"])
    for var in type["vars"]:
        #print("\t",var["name"],"\t\t\t",var["data"].split()[0])
        snippetName = f"nau::valueof::{type['name']}::{var['name']}"
        description=[
            f"materialLib>>materials>>material>>shader>>values",
            f"\tValue Of {type['name']} {var['name']}"
        ]
        if type["name"] == "TEXTURE_BINDING":
            snip[snippetName] = {
                "scope":"xml",
                "prefix":[f"valueof {type['name']} {var['name']}"],
                "body":[
                    f"<valueof uniform=\"${'{1:'+var['name']+'}'}\" 		type=\"{type['name']}\" 		context=\"CURRENT\" 		component=\"{var['name']}\" id=\"$2\" />"
                ],
                "description":description       
            }
        else:
            snip[snippetName] = {
                "scope":"xml",
                "prefix":[f"valueof {type['name']} {var['name']}"],
                "body":[
                    f"<valueof uniform=\"${'{1:'+var['name']+'}'}\" 		type=\"{type['name']}\" 		context=\"CURRENT\" 		component=\"{var['name']}\" />"
                ],
                "description":description       
            }

out = open("valueof.code-snippets","w")
json.dump(snip,out,indent=2)
