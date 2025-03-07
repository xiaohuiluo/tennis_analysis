import pickle
import numpy as np

f = open('./tracker_stubs/player_detections.pkl','rb')
data = pickle.load(f)
print(data)

# img_path = './train_data.pkl'
# img_data = np.load(img_path)
# print(img_data)

