def merge(leftPartition,rightPartition,array):
    sizeLeft=len(leftPartition)
    sizeRight=len(rightPartition)

    i=0 #index of left partition
    j=0 #index of right partition
    k=0 #index of the merged array

    while (i<sizeLeft) & (j<sizeRight):
        if leftPartition[i]<=rightPartition[j]:#putting the smaller vale to the array from the two partitions

            array[k]=leftPartition[i]

            i=i+1
        else:
            array[k]=rightPartition[j]

            j=j+1
        k=k+1

    while i<sizeLeft:#if the right  partition is already exhausted
        array[k]=leftPartition[i]
        i=i+1
        k=k+1

    while j<sizeRight:#if the left  partition is already exhausted
        array[k]=rightPartition[j]
        j=j+1
        k=k+1
    return  array


def mergeSort(array):
    n=len(array)
    if n<2:
        return

    partition=round(len(array)/2)
    leftPartition=array[:partition]
    rightPartition=array[partition:]

    mergeSort(leftPartition)
    mergeSort(rightPartition)
    merge(leftPartition,rightPartition,array)

import  unittest

class TestMergeSort(unittest.TestCase):
    def testWhenOneElement(self):
        array=[1]
        mergeSort(array)
        self.assertEquals(array,[1]);
    def testWhenTwoElements(self):
        array=[3,1]
        mergeSort(array)
        self.assertEquals(array,[1,3])
    def testWhenThreeElements(self):
        array=[5,9,1]
        mergeSort(array)
        self.assertEquals(array,[1,5,9])
    def testWhenHaveEqualElements(self):
        array=[1,12,4,9,1]
        mergeSort(array)
        self.assertEquals(array,[1,1,4,9,12])
    def testWhenHighVariation(self):
        array=[-9,10,1000000,2,0.001,90000,-8]
        mergeSort(array)
        self.assertEquals(array,[-9,-8,0.001,2,10,90000,1000000])