import pickle
import json
import numpy as np
import config

class MobilePrice():
    def __init__(self,Sale,weight,resoloution,ppi,cpu_core,cpu_freq,internal_mem,ram,RearCam,Front_Cam,battery,thickness):
        print("****** INIT Function *********")
        self.Sale = Sale
        self.weight = weight
        self.resoloution = resoloution
        self.ppi = ppi
        self.cpu_core = cpu_core
        self.cpu_freq = cpu_freq 
        self.internal_mem = internal_mem
        self.ram = ram
        self.RearCam = RearCam
        self.Front_Cam = Front_Cam
        self.battery = battery
        self.thickness = thickness
    
    def __load_saved_data(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_predicted_price(self):
        self.__load_saved_data()
    
        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.Sale
        test_array[0,1] = self.weight
        test_array[0,2] = self.resoloution
        test_array[0,3] = self.ppi 
        test_array[0,4] = self.cpu_core
        test_array[0,5] = self.cpu_freq
        test_array[0,6] = self.internal_mem
        test_array[0,7] = self.ram
        test_array[0,8] = self.RearCam
        test_array[0,9] = self.Front_Cam
        test_array[0,10] = self.battery
        test_array[0,11] = self.thickness


        predicted_price = np.around(self.model.predict(test_array)[0],3)
        return predicted_price