import numpy as np


def testFun():
    points=np.array([[-1,1],[-2,2]])
    #creating voting table
    #angle:+-90
    #rho:+-max(x+y)
    #a,b: y=ax+b
    bins = np.zeros((20, 180), dtype=int)
    for x,z in points:
        for angle, dx in enumerate(np.arange(-90,90)):
                bin = int(np.round(x*np.cos(np.deg2rad(angle))+z*np.sin(np.deg2rad(angle))))
                bins[bin, abs(angle)] += 1    
    #get potential results
    winners = np.argwhere(bins == np.amax(bins))
    #make filter masks.
    
    minErr=float("inf")
    fitOne = 0
    coefs=[]
    #Get the line formula
    for winner in winners:
        rho,theta = winner
        A= -1/(np.tan(np.deg2rad(theta)))
        B= rho/np.sin(np.deg2rad(theta))
        X = points[:,[0]]
        err=0
        for point in points:
            predY = A*point[0]+B
            err += (point[1]-predY)**2
        err/=len(winners)
        err = err**0.5
        if err<=minErr:
            minErr=err
            fitOne=winner
            coefs=[A,B]
        # print("winner:", winner)
        # print(err)
        # print("=====")
    print("final:")
    print(fitOne)
    print("coefs:",coefs)
    print("min err:", minErr)
        


    # best = np.unravel_index(winners, bins.shape)
    # print(best)

testFun()