import numpy as np


class Customer_Log_Reg:
    def __init__(self, x, y):
        self.intercept = np.ones((x.shape[0], 1))  
        self.x = np.concatenate((self.intercept, x), axis=1)
        self.y = y
        self.w = np.zeros(self.x.shape[1])
        self.n_iter = 100_000
        self.learn_rate = 0.0008

        
    def sigmoid(self, x, w):
        z = np.dot(x, w)
        return 1 / (1+np.exp(-z))
    
    def log_loss_func(self, f, y):
        return -np.mean((y * np.log(f) + (1 - y) * np.log(1 - f)))
    
    def gradients(self, x, f, y):
        return np.dot(x.T, (f-y)) / y.shape[0]
        
    def train(self):
        for _ in range(self.n_iter):
            s = self.sigmoid(self.x, self.w)
            lf = self.log_loss_func(s, self.y)
            dw = self.gradients(self.x, s, self.y)
            self.w -= self.learn_rate * dw
        return lf
    
    def predict(self, x_input, tolerance=1e-6):
        x_input = np.concatenate((self.intercept, x_input), axis=1)
        result = self.sigmoid(x_input, self.w)
        result = result >= tolerance
        y_pred = np.zeros(result.shape[0])
        for i in range(len(y_pred)):
            if result[i] == True: 
                y_pred[i] = 1
            else:
                continue
                 
        return y_pred

    


   

        
        
        
        
                
        
        
        
    

  
    
    

