import os
import requests

url = "https://ci.fredboat.com/app/rest/buildQueue"

payload = '''
<build>
    <buildType id="FredBoat_Integration"/>
    <comment><text>Integration build triggered by {}</text></comment>
    <properties>
        <property name="env.{}" value="{}"/>
    </properties>
</build>
'''

confName = os.environ["teamcity.buildConfName"]

displayName = ""

if confName == "FredBoat_Build":
    displayName = "FredBoat"
elif confName == "Lavalink_Build":
    displayName = "Lavalink"
elif confName == "Private_Dike_Build":
    displayName = "Dike"
else:
    raise RuntimeError("Unexpected build config: " + confName)

payload = payload.format(displayName,
                         displayName.lower() + "Branch",
                         os.environ["teamcity.build.branch"])

print(payload)

headers = {
    'content-type': "application/xml",
}

username = os.environ["tempUser"]
password = os.environ["tempPass"]

response = requests.request("POST", url, data=payload, headers=headers, auth=(username, password))

print(response.text)
