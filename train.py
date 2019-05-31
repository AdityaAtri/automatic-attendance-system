import cognitive_face as CF
from global_variables import personGroupId

Base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # default endpoint when use free 
CF.BaseUrl.set(Base_url)
Key= 'ca31e5858d5b4e55ae010bc319f8654c' # subscription key needed 
CF.Key.set(Key)

res = CF.person_group.train(personGroupId)
print(res)