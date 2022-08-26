"""
Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, ,
determine how many letters of the SOS message have been changed by radiation.

Example
The original message was SOSSOS. Two of the message's characters were changed in transit.

Function Description

Complete the marsExploration function in the editor below.

marsExploration has the following parameter(s):

string s: the string as received on Earth
Returns

int: the number of letters changed during transmission"""


def marsExploration(s):
    # Write your code here

    res = len(s)//3

    target = "SOS"*res

    count = 0

    for i,j in zip(s,target):
        if i != j:
            count += 1

    return count
