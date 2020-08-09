import time
print "($) Core Modules Ready"

# SkyBiometry
import face_client
skybio = face_client.FaceClient("on276kmkjhhpijcl5q3q6djjd5", "v6up76j6n2dbf0vabnet0oee9j")
data_skybio = open("data_skybio.txt", "a+")
print "($) Initialized SkyBiometry Service"

#F.A.C.E.
import requests
face_api_key = "ec73e70b3f5a4ef39b9344a39b569753"
data_face = open("data_face.txt", "a+")
print "($) Initialized F.A.C.E. Service"

#Eyeris
import unirest
eyeris = None
eyeris_api_key = "aMBCqE6llemshZEBObu4JN9sz2UNp1dGpPKjsnhHhTYSzWkmXk"
print "(!) Unable to Initialize Eyeris Service"

print "(*) Starting Routine"
try:
    emotion = ""
    for i in range(1,16):
        if i < 10:
            i = "0" + str(i)
        else:
            i = str(i)

        for j in range(3):
            if j == 0:
                emotion = "happy"
            elif j == 1:
                emotion = "sad"
            elif j == 2:
                emotion = "surprised"

            print "(*) Analyzing Subject [" + i + "] for: " + emotion
            with open(("Yale_DB/subject" + str(i) + "." + str(emotion) + ".png")) as current_img:
                try:
                    #data_temp = skybio.faces_detect(file=current_img)
                    #data_skybio.write("\"" + str(i) + emotion + "\" : " + str(data_temp) + "\n\n")
                    data_temp = requests.post('https://api-face.sightcorp.com/api/detect/', data={'app_key' : face_api_key}, files={'img':(str('subject' + i + "_" + emotion), current_img)})
                    data_face.write(data_temp.text + "\n")
                except:
                    print "(!) Error at Subject" + str(i) + emotion
                    print "(!) Continuing..."
            #time.sleep(600)  #SkyBiometry
            time.sleep(60) #FACE

except Exception, e:
    print "(!) Error caught, contents are: " + str(e)
