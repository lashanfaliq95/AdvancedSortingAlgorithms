def partition(array,start,end):#function to set the pivot and return the index of the pivot
    pivot=array[end] #setting the pivot as the last element of the given range
    index=start
    for i in range(start,end):
        if array[i]<pivot:#checking if the element is less than the pivot if it is swap and moe the index by one
            temp=array[i]
            array[i]=array[index]
            array[index]=temp
            index=index+1
    temp=array[index]
    array[index]=pivot
    array[end]=temp
    return  index


def quickSort(array):
    quickSort1(array,0,len(array)-1) #so we can give the additional inputs
def quickSort1(array,start,end):
    if start<end:
        index=partition(array,start,end)
        quickSort1(array,start,index-1)
        quickSort1(array,index+1,end)

import  unittest

class TestQuickSort(unittest.TestCase):
    def testWhenOneElement(self):
        array=[1]
        quickSort(array)
        self.assertEquals(array,[1]);
    def testWhenTwoElements(self):
        array=[3,1]
        quickSort(array)
        self.assertEquals(array,[1,3])
    def testWhenThreeElements(self):
        array=[5,9,1]
        quickSort(array)
        self.assertEquals(array,[1,5,9])
    def testWhenHaveEqualElements(self):
        array=[1,12,4,9,1]
        quickSort(array)
        self.assertEquals(array,[1,1,4,9,12])
    def testWhenHighVariation(self):
        array=[-9,10,1000000,2,0.001,90000,-8]
        quickSort(array)
        self.assertEquals(array,[-9,-8,0.001,2,10,90000,1000000])


