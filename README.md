
<h3 align="center">Subnetting by Host or Network Requirement, an Algebraic Approach</h3>

---

<p align="center"> An Algebraic approach in getting all possible network ranges of all classes of IP Addresses even up to increments of 1 which can then result to 16,777,216 network addresses.
    <br> 
</p>

## Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Running The Tests](#tests)
- [Usage](#usage)
- [Built Using](#built_using)
- [Author](#authors)
- [Acknowledgments](#acknowledgment)

## ABOUT <a name = "about"></a>
This program is able to calculate all following data by taking advantage of some relevant Algebraic concepts and creating my own mathematical equations to generate these arithemtic sequences. This method was also inspired from the popular subnetting technique called by everyone else as the "Fingernetting." 
1. Number of bits 
2. Subnet Mask, long format
3. Increment to be added per network range
4. Class of IP Address
5. Classful IP Address
6. Number of Actual Networks
7. Number of Usable Hosts
8. All possible network ranges - until every octet reaches its maximum value of 255


**The following mathematical equations were ***created by myself*** to generate all possible arithmetic sequences having increments of 128, 64, 32, 16, 8, 4, 2, and 1.**

![subnet_eqn](https://user-images.githubusercontent.com/79388960/111165258-c84fc300-85d9-11eb-8274-9c6ce6b65a97.jpg)
- *assuming we are dealing with a Class A IP Address with a subnet mask of /25 to /32; wherein calculations will supposedly be performed starting from the 4th octet to the 2nd octet if the user intends to generate all possible network ranges until each octet reaches the maximum value of 255 which will then generate a total of exactly 16,777,216 network addresses having an increment of 1 - the maximum possible number of actual networks in subnetting*


## GETTING STARTED <a name = "getting_started"></a>
No other prerequisites required to run this program other than latest version of Python which is Python 3.9.0.


## RUNNING THE TESTS <a name = "tests"></a>
The following tests have been made to ensure that the program can generate all possible network ranges and also indicate whether an octet has reached a maximum value of 255.

Specifically, manual unit testing was done to ensure that X input results in Y output. This approach enables one to identify functions that compare the outcome of one's function to the expected outcome.

The following variables were directly substituted with a certain value to assess if it has returned a valid output:
* variables that determine which ranges to calculate  
    *range_first = 0*  
    *range_last = 50*  

* a sample Class A IP Address  
    *increm_ip = [80, 0, 0, 0]*  

* dictates the value that will be added per network address  
    *increm = 32*  

* increment will be added at nth octet, i.e., a /30 Subnet Mask will return a value of '4th' since an increment will be added at the 4th octet  
    *def add_increm_octet():*  
        *return '4th'*  

* determines the class of IP Address that has been provided and performs the necessary calculations thereafter  
    *def ip_class():*  
        *return 'Class C'*  

**RESULTS:**
- The following results prove that the program is capable of generating all possible network ranges until each octet reaches its maximum values.
1. [Class A IP Addresses](https://imgur.com/a/gPUnrkn)
2. [Class B IP Addresses](https://imgur.com/a/ZP3hXJY)
3. [Class C IP Addresses](https://imgur.com/a/9EVGpQ0)


## USAGE <a name="usage"></a>
The following reminders must be noted for this program to run successfully. Future updates will be implemented so as to resolve these issues.
1. As of 03.15.2021, this program is unable to accurately pinpoint which inputs provided are incorrect. Thus, make sure to only provide valid inputs for this program to run successfully.  
2. Proper format should be as follows: AAA.BBB.CCC.DDD/XX, where XX is the CIDR (no spaces please).  
3. The table below shows the maximum number of actual networks that can be generated per increment.

Class C
|             |            | 128 | 64 | 32 | 16 |  8 |  4 |  2  |  1  |
|:-----------:|:----------:|:---:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|
| Subnet Mask | /25 to /32 |  2  |  4 |  8 | 16 | 32 | 64 | 128 | 256 |
|             | /17 to /34 |  -  |  - |  - |  - |  - |  - |  -  |  -  |
|             |  /9 to /16 |  -  |  - |  - |  - |  - |  - |  -  |  -  |


Class B
|             |            | 128 |  64  |  32  |  16  |   8  |   4   |   2   |   1   |
|:-----------:|:----------:|:---:|:----:|:----:|:----:|:----:|:-----:|:-----:|:-----:|
| Subnet Mask | /25 to /32 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|             | /17 to /34 |  2  |   4  |   8  |  16  |  32  |   64  |  128  |  256  |
|             |  /9 to /16 |  -  |   -  |   -  |   -  |   -  |   -   |   -   |   -   |


Class A
|             |            |   128  |   64   |   32   |    16   |    8    |    4    |    2    |     1    |
|:-----------:|:----------:|:------:|:------:|:------:|:-------:|:-------:|:-------:|:-------:|:--------:|
| Subnet Mask | /25 to /32 | 131072 | 262144 | 524288 | 1048576 | 2097152 | 4194304 | 8388608 | 16777216 |
|             | /17 to /34 |   512  |  1024  |  2048  |   4096  |   8192  |  16384  |  32768  |   65536  |
|             |  /9 to /16 |    2   |    4   |    8   |    16   |    32   |    64   |   128   |    256   |



## BUILT USING  <a name = "built_using"></a>
- [Python](https://www.python.org/) 

## AUTHOR <a name = "authors"></a>
- [@ryanbelnas](https://github.com/ryanbelnas) - Idea & Initial work


## ACKNOWLEDGMENT <a name = "acknowledgment"></a>
- Yusof Bactong
- Marisyl Batal
- Sandra Dupio
