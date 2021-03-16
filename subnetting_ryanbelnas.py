import sys

# #### INPUT ########
print(f'REMINDERS: \n1. As of 03.15.2021, this program is unable to accurately pinpoint which inputs of yours are incorrect. Thus, make sure to only provide valid inputs for this program to run successfully. \n2. Proper format should be as follows: AAA.BBB.CCC.DDD/XX, where XX is the CIDR (no spaces please). \n3. Please see README file to be informed regarding the maximum number of actual networks that can be generated. \n4. This program can generate ALL possible network ranges per class of IP address. \n \n')
take_ip = input('Provide the IP address with its subnet mask in CIDR notation: ')

print(f'\nWhich type of subnetting do you want to perform?')
type_subnet = int(input('Choose 1 or 2: \n1. Network requirement \n2. Host requirement \n\n' ))

if type_subnet == 1:
    get_bits = int(input('How many networks?: '))

elif type_subnet == 2:
    get_bits = int(input('How many hosts?: '))

else:
    print('You provided an invalid input.')
    sys.exit()

print(f'\nWhat range of subnets would you like to generate?')
range_first = int(input('Provide the first range: '))
range_last = int(input('Provide the last range: '))
#######################




take_osm = take_ip.split('/')



################### Calculates the number of bits ###################
n = 1
bits_list = []

while n < get_bits:
	  bits_list.append(n)
	  n = n*2
	 
num_bits = len(bits_list)


################### Performs a calculation depending the type of subnetting (host/network) ###################
if type_subnet == 1:
    nsm_cidr = int(take_osm[1]) + num_bits
elif type_subnet == 2:
    nsm_cidr = 32 - num_bits



################### Converts CIDR to its long format ###################
nsm_lf_num = nsm_cidr // 8
nsm_lf_rem = nsm_cidr % 8


################### Method inspired from 'fingernetting' ###################
lower_finger = [None, 128, 192, 224, 240, 248, 252, 254, 255]
upper_finger = [None, 128, 64, 32, 16, 8, 4, 2, 1]
num_255 = [255, 255, 255, 255]

nsm_lf = []

def get_nsm_lf():
    if nsm_lf_num == 1:
        nsm_lf.extend([255, 0, 0])
        nsm_lf.insert(1, lower_finger[nsm_lf_rem])
        return nsm_lf
    elif nsm_lf_num == 2:
        nsm_lf.extend([255, 255, 0])
        nsm_lf.insert(2, lower_finger[nsm_lf_rem])
        return nsm_lf
    elif nsm_lf_num == 3:
        nsm_lf.extend([255, 255, 255])
        nsm_lf.insert(3, lower_finger[nsm_lf_rem])
        return nsm_lf
    else:
        return 'Invalid mask'
        sys.exit()




################### Calculates the increment ###################
increm = upper_finger[nsm_lf_rem]


################### Determines the class of IP address ###################
import re

det_class = re.split('[./]', take_ip)

det_class_int = []
for n in det_class:
    det_class_int.append(int(n))
    

def ip_class():
    if det_class_int[0] <= 127:
        return 'Class A'
    elif det_class_int[0] >= 128 and det_class_int[0] <= 191:
        return 'Class B'
    elif det_class_int[0] >= 192 and det_class_int[0] <= 223:
        return 'Class C'
    elif det_class_int[0] >= 224 and det_class_int[0] <= 239:
        return 'Class D'
    elif det_class_int[0] >= 240 and det_class_int[0] <= 254:
        return 'Class E'
    else:
        return 'You provided an invalid IP address.'
        sys.exit()


################### Generates all possible subnets ###################

def network_bits(): # Copies the bits that has been considered as network bits and stores it in a list []
	if ip_class() == 'Class A':  
		return det_class_int[0:1] + [0,0,0]
	elif ip_class() == 'Class B':
		return det_class_int[0:2] + [0,0]
	elif ip_class() == 'Class C':
		return det_class_int[0:3] + [0]
	else:
		return 'Unable to perform subnetting on this class of IP address'


     
		
initial_nsm_lf = get_nsm_lf().copy()

def add_increm_octet(): 
    if initial_nsm_lf[3] != 0:
        return '4th'
    elif initial_nsm_lf[2] != 0:
        return '3rd'
    elif initial_nsm_lf[1] != 0:
        return '2nd'
    else:
        return 'Invalid'



################### Generates all possible network addresses ###################

increm_ip = network_bits()
sel_net_range = range(range_first, range_last + 1)
reset_octet = 256 // increm # magic number!!!!!!!!!
reset_octet_2 = 256 ** 2 // increm
           
            
def net_addr():
    global x
    global y

    if add_increm_octet() == '4th': # S4 and S6
        x = 2
        y = 3

    elif add_increm_octet() == '3rd':
        x = 1
        y = 2

    elif add_increm_octet() == '2nd':
        y = 1
   
        #####
    for n in sel_net_range:
        #####
        
        increm_ip[y] = (n * increm) % 256    # WHERE INCREM IS ADDED 
        
        
        
        if add_increm_octet() == '3rd' and ip_class() == 'Class A':
            increm_ip[x] = increm * n // 256
            
        if add_increm_octet() == '4th' and ip_class() == 'Class B':
            increm_ip[x] = increm * n // 256
            
        if add_increm_octet() == '2nd': # S3
            increm_ip[2] = 0
            increm_ip[3] = 0
            
            if (increm * n // 256) >= 256:
                increm_ip[1] = 'MAXED OUT'
            
        
        if ip_class() in ('Class A', 'Class B') and add_increm_octet() == '3rd': # S2 and S5b
            increm_ip[3] = 0
            
        if add_increm_octet() == '4th' and ip_class() == 'Class A': # S1
            increm_ip[1] = (increm * n // 256 ** 2) % 256
            
            if (increm * n // 256 ** 2) >= 256:
                increm_ip[1] = 'MAXED OUT'
            
                
            increm_ip[x] = increm * n // 256 
    
            if increm_ip[x] >= 256: 
                increm_ip[x] = (increm * (n - reset_octet_2) // 256) % 256


        if add_increm_octet() == '3rd':
            if (increm * n // 256) >= 256:
                increm_ip[1] = 'MAXED OUT'
                
        if add_increm_octet() == '2nd':
            if n * increm >= 256:
                increm_ip[1] = 'MAXED OUT'
                
  
                
        if add_increm_octet() == '4th' and ip_class() == 'Class C':
            if (n * increm) >= 256:
                increm_ip[3] = 'MAXED OUT'
                
        if add_increm_octet() == '3rd' and ip_class() == 'Class B':
            if (n * increm) >= 256:
                increm_ip[2] = 'MAXED OUT'
                
        if add_increm_octet() == '4th' and ip_class() == 'Class B':
            if increm_ip[2] >= 256:
                increm_ip[2] = 'MAXED OUT'
            
                
        
        
        if 'MAXED OUT' in increm_ip:
            increm_ip[0] = 'MAXED OUT'
            increm_ip[1] = 'MAXED OUT'
            increm_ip[2] = 'MAXED OUT'
            increm_ip[3] = 'MAXED OUT'
        
        
        if add_increm_octet() == '2nd' and ip_class() in ('Class B', 'Class C'):
            increm_ip[0] = 'INVALID MASK'
            increm_ip[1] = 'INVALID MASK'
            increm_ip[2] = 'INVALID MASK'
            increm_ip[3] = 'INVALID MASK'
                
        #####       
        net_range_3 = '.'.join(str(x) for x in increm_ip)
        net_range_4 = str(n+1) + ': ' + net_range_3 + ' -' #Use 'n' when testing, 'n+1' when actual deployment
        yield net_range_4
        #####    
            
 
################### Generates all possible broadcast addresses ###################

def brdcst_addr():
        #####
    for n in range(range_first + 1, range_last + 2):
        brdcst_ip = increm_ip.copy()
        #####
        
        
        
        if add_increm_octet() == '2nd' and ip_class() in ('Class A', 'Class B'):
            brdcst_ip[2] = 255
            brdcst_ip[3] = 255
            
        
        
        if ip_class() in ('Class A', 'Class B') and add_increm_octet() == '3rd': # S5 and S2
            brdcst_ip[3] = 255

        
        brdcst_ip[y] = ((n * increm) % 256) - 1
        
        if brdcst_ip[y] == -1:
            brdcst_ip[y] = 255
        

        
        if 'MAXED OUT' in increm_ip:
            brdcst_ip[0] = 'MAXED OUT'
            brdcst_ip[1] = 'MAXED OUT'
            brdcst_ip[2] = 'MAXED OUT'
            brdcst_ip[3] = 'MAXED OUT'
            
        if 'INVALID MASK' in increm_ip:
            brdcst_ip[0] = 'INVALID MASK'
            brdcst_ip[1] = 'INVALID MASK'
            brdcst_ip[2] = 'INVALID MASK'
            brdcst_ip[3] = 'INVALID MASK'


        
        
        
        
        
        
        #####
        brdcst_range_3 = '.'.join(str(x) for x in brdcst_ip)
        brdcst_range_4 = brdcst_range_3
        yield brdcst_range_4
        #####
        
        


old_subnet_mask = det_class_int[4]


################### Calculates the actual number of networks ###################

def get_actual_nets():
    actual_nets = 2 ** (nsm_cidr - old_subnet_mask)
    return actual_nets


################### Calculates the number of usable hosts ###################

def get_usable_host():
    usable_host = (2 ** (32 - nsm_cidr)) - 2
    return usable_host






###################
print(f'\nNumber of bits: {num_bits}')

new_subnet_mask_lf = '.'.join(str(x) for x in initial_nsm_lf) 
print(f'New Subnet Mask \nCIDR: /{nsm_cidr} \nLong Format: {new_subnet_mask_lf}')

print(f'Increment: {increm}')

print(f'IP Address Class: {ip_class()}')

network_bits = '.'.join(str(x) for x in network_bits())
print(f'Classful Address: {network_bits}')

print(f'No. of Actual Networks: {get_actual_nets()}')

print(f'No. of Usable Hosts: {get_usable_host()}')

##############    
print(f'\nPossible networks from {range_first + 1} to {range_last}:')
for a,b in zip(net_addr(), brdcst_addr()):
    print(a, b)
##################







