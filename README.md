# A-Law-Compander
This python program is used to read a xls file to do A-Law Companding on a Signal, in my case ss.xls. 
Note:Please edit the file name before running your signal.

The code has three methods:
1. run() : To run the speech signal.
   Input your signal here.
2. alaw() : To do A-Law companding per bit.  
   Parameters: z  
               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integer  
               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The value that has to be encoded. Also works as a stand-alone function.
3. dealaw()n : To decode the coded signal.  
   Parameters: z   
               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8 bit Character  
               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The value that has to be decoded. Inputs a string containing 8 bit binary value. Also works as a &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stand-alone function.



![Original and Decoded Signal Error](https://github.com/thejithinmathew/A-Law-Compander/blob/master/as2.png)

![Another Sample](https://github.com/thejithinmathew/A-Law-Compander/blob/master/as1.png)


