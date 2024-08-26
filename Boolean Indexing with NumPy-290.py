## 1. Reading CSV files with NumPy ##

import numpy as np

taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
taxi_shape = taxi.shape

taxi_ohne_header = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)
taxi_ohne_header_shape = taxi_ohne_header.shape





## 2. Reading CSV Files with NumPy (Continued) ##

taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)
taxi_shape = taxi.shape

print(taxi.dtype)
print(taxi.max())

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3
b_bool = b == 'blue'
c_bool = c > 100


## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

print(february_rides > january_rides)

junho_bool = pickup_month == 6
junho = pickup_month[junho_bool]
junho_rides = junho.shape[0]

print(junho_rides > january_rides)

## 5. Boolean Indexing with 2D Ndarrays ##

tip_amount = taxi[:,12]

tip_bool = tip_amount > 50
top_tips = taxi[tip_bool, 5:14]

print(top_tips.shape)

## 6. Assigning Values in Ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()

a = [[0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3]]

a_array = np.array(a)


#ones = np.array([[1, 1, 1, 1, 1],
 #                [1, 1, 1, 1, 1],
  #               [1, 1, 1, 1, 1]])

#ones[0] = 99
#a_array = np.array(a)

a_array[0] = 99
print(a_array)
#print(ones)
a_array[0,4] = 100
print(a_array)

a_array[1:,4] = 69
print(a_array)

taxi_modified[28214,5] = 1
taxi_modified[:, 0] = 16
taxi_modified[1800:1802, 7] = taxi_modified[:, 7].mean()

print(taxi_modified[1800:1802, 7])

## 7. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

total_amount = taxi_copy[:,13]
total_amount[total_amount<0] = 0

print(total_amount[total_amount<0].shape)




## 8. Assignment Using Boolean Arrays (Continued) ##

# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)

taxi_modified[taxi_modified[:,5] == 2, 15] = 1
taxi_modified[taxi_modified[:,5] == 3, 15] = 1
taxi_modified[taxi_modified[:,5] == 5, 15] = 1


## 9. Challenge: Which Is the Busiest Airport? ##

jfk = taxi[taxi[:,6] == 2]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:,6] == 3]
laguardia_count = laguardia.shape[0]

newark = taxi[taxi[:,6] == 5]
newark_count = newark.shape[0]

print(max(jfk_count, laguardia_count, newark_count))
              

## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)

cleaned_taxi = taxi[trip_mph<100]

mean_distance = np.mean(cleaned_taxi[:,7])
mean_length = np.mean(cleaned_taxi[:,8])
mean_total_amount = np.mean(cleaned_taxi[:,13])

#print(trip_mph.shape)
#print(taxi.shape)

print('mean_length_hours:') 
print(round(mean_length/3600, 2))
print('\n')
print('mean_distance_km:')
print(round(mean_distance*1.61, 2))
