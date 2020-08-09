import json

file_face = open("data_face.txt", "r")
raw_data = file_face.read().split("\n\n")[0:-1]
data = []
output = open("data_face_processed.txt", "a+")
emotions = ["happiness", "surprise", "anger", "disgust", "fear", "sadness"]

for i in range(45):
    data.append(json.loads(raw_data[i]))

subject_num = 1
for i in range(1,46):
    if (i != 1) and (i%3 == 1): subject_num += 1

    if i%3 == 1:
        emotion = "happiness"
    elif i%3 == 2:
        emotion = "sadness"
    elif i%3 == 0:
        emotion = "surprise"

    temp = data[i-1]["people"][0]["emotions"]
    temp_list = []
    temp_dict = {}

    for feeling in emotions:
        temp_list.append(temp[feeling])

    for i, j in enumerate(emotions):
        temp_dict[j] = temp_list[i]
    
    temp_list2 = [(value, key) for key, value in temp_dict.items()]
    answer = max(temp_list2)[1]

    output.write("Subject " + str(subject_num) + " was " + emotion + ", result was: " + answer + "\n")
    
output.close()