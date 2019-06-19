
from math import *

class kalman(object):
    '''Class to demonstrate kalman filter in 1 dimension'''
    def __init__(self):
        #measurement updates after each cycle
        self.measurements = [5., 6., 7., 9., 10.]
        #motion information, which the "object" would know.
        self.motion = [1., 1., 2., 1., 1.]
        assert len(self.measurements) == len(self.motion), "number of measurements and motions is not equal"
        
        #Variance, or error or uncertaintly which can be introduced in measurement
        self.measurement_sig = 4.
        #Variance, or error or uncertaintly which can be introduced when the motion is performed
        self.motion_sig = 2.
        #Current position
        self.mu = 0.
        #Variance in current position. Initialize to a large value to start with.
        self.sig = 10000.

    def update(self, measurement):
        '''Measure cycle'''
        #Update as per the measurements. Decreases un-certainty
        self.mu = (self.measurement_sig * self.mu + self.sig * measurement) * 1/(self.sig + self.measurement_sig)
        self.sig = 1/(1/self.sig + 1/self.measurement_sig)

    def predict(self, motion):
        '''Movement cycle'''
        #Move with un-certaintly
        self.mu = self.mu + motion
        self.sig = self.sig + self.motion_sig

    def kalman(self):
        '''Iterate over the given list of measurements and perform update and predict cycles'''
        for measurement, motion in zip(self.measurements, self.motion):
            self.update(measurement)
            print ("update : %s,%s"%(self.mu, self.sig))
            self.predict(motion)
            print ("predict : %s,%s"%(self.mu, self.sig))

if __name__ == "__main__":
    obj = kalman()
    obj.kalman()
