import os
import face_recognition
def cluster(dir):
    box = []
    main = []

        
    for kk in range(len(os.listdir(dir))):
        bc = []
        bc.append(os.listdir(dir)[kk])
        for jj in range(len(os.listdir(dir))):
            if kk != jj:
                file1 = '{}/{}'.format(dir,os.listdir(dir)[kk])
                file2 = '{}/{}'.format(dir,os.listdir(dir)[jj])
                known_image = face_recognition.load_image_file(file1)
                unknown_image = face_recognition.load_image_file(file2)

                biden_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

                results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
                if results[0] == True:
                
                    #box[str(kk)]=([os.listdir(dir)[kk]])
                    
                    #box[str(kk)].append(os.listdir(dir)[kk])
                    bc.append(os.listdir(dir)[jj])
                    
        box.append(bc)
        

            
    
    
    new_arr = []
    arr = box
    for i in range(len(arr)):

        for j in range(i+1, len(arr)):

            if set(arr[i]).intersection(set(arr[j])):

                new_arr.append(list(set(arr[i]).union(set(arr[j]))))
                
    res = []
    for ic in new_arr:
        ic.sort()
        if ic not in res:
            res.append(ic)
    return res
print(cluster('image'))