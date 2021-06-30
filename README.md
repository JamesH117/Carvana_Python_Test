# Carvana_Python_Test
## Document of test copy/paste

2. Operating Hours Calculation

There is a warehouse in CarvanaLand. Trucks come and leave at anytime of the day, and are
loaded with packages at the warehouse. Behind the scene, there is an online platform that
continuously taking in new orders from customers. Each order comes with a delivery due date.
The manager at the warehouse can generate an optimal plan which guarantees all packages
arrive at customers on time.
There are also loaders working at the warehouse, who help load trucks with packages. One
loader can only load one truck at a time. It takes a loader several work hours to fill a truck.
Before a loader starts to load a truck, the manager is expected to give him/her a list of delivery
packages that need to be loaded to the truck. Please note that:
1) Each loader has his/her own work schedule.
For example, some loaders work from 8:00 am to 2:00 pm Monday through Saturday,
while some loaders work from 10:00 am to 6:00 pm Tuesday to Sunday.
2) The time it takes to load a truck differs from truck to truck.
For example, experienced loaders may be able to load a truck in 3 hours, while other
loaders need 4 hours.
3) Moreover, some loaders prefer loading all packages to a truck on the same day,
while some loaders are willing to load a truck across multiple days.
For example, a truck leaves at 10:00 am tomorrow, and the loader works from 8:00 am
to 4:00 pm everyday, assuming loading the truck takes 3 hours. If the loader prefers
doing all the loading work on the same day, then it means the manager needs to give
this loader the list of deliveries before 1:00 pm today. So that the loader will have 3
continuous work hours (1:00 pm ~ 4:00 pm) on the previous day to load the truck. But if
the loader is willing to divide loading workload into two consecutive days, then he can
start loading at 3:00pm today, work for one hour, and continue with the rest of the
loading work 8:00 ~ 10:00 am tomorrow. The difference between the two
options/configurations is whether the loading time has to be a continuous chunk of time
or not.

Exercise:
Write a python script that takes the following inputs:
1. Loader work hours
2. Loader work days
3. Total time the loader needs to load the truck
4. Truck departure datetime
5. Does the loading time have to be on the same day or not?
The script is expected to export a datetime string which tells the manager when she should give
the loader a list of delivery packages.

Example 1:
Inputs:
1. Work hours: 08:00 ~ 14:00
2. Work days: Monday through Saturday
3. Loading Time: 3 Hours
4. Truck departure time: 2018-08-13 10:00 (CarvanaLand local timezone)
5. Loading time has to be on the same day
Expected Output: 2018-08-11 11:00
Explanation : The loader has only 2 hours prior to truck departure, and the previous day is a
Sunday. So the loader will need to start loading the truck on Saturday afternoon.

Example 2:
Inputs:
1. Work hours: 08:00 ~ 14:00
2. Work days: Monday through Saturday
3. Loading Time: 3 Hours
4. Truck departure time: 2018-08-14 10:00 (CarvanaLand local timezone)
5. Loading time can be spread across different days
Expected Output: 2018-08-13 13:00
Explanation : The loader has 2 hours prior to truck departure, which he/she can use for loading.
He/she needs one more hour from the previous work day to complete the loading. The day
before truck departure is a regular workday for this loader. So the loader needs to start loading
at 13:00 the day before.

Please run your script against the following test cases, and submit your outputs along
with your code. All outputs are expected to be datetime strings in “%Y-%m-%d %H:%M”
format.

Test case 1 inputs:
1. Work hours: 08:00 ~ 14:00
2. Work days: Monday through Friday
3. Loading Time: 3 Hours
4. Truck departure time: 2018-08-15 14:00
5. Loading time can be spread across different days

Test case 2 inputs:
1. Work hours: 08:00 ~ 14:00
2. Work days: Monday through Friday
3. Loading Time: 3 Hours
4. Truck departure time: 2018-08-15 14:00
5. Loading time cannot be spread across different days

Test case 3 inputs:
1. Work hours: 12:00 ~ 18:00
2. Work days: Monday, Wednesday, Friday
3. Loading Time: 3 Hours
4. Truck departure time: 2018-08-15 10:00
5. Loading time can be spread across different days

Test case 4 inputs:
1. Work hours: 08:00 ~ 14:00
2. Work days: Monday through Saturday
3. Loading Time: 3.5 Hours
4. Truck departure time: 2018-08-14 10:00
5. Loading time can be spread across different days

Test case 5 inputs:
1. Work hours: 08:00 ~ 14:00
2. Work days: Monday through Saturday
3. Loading Time: 3.5 Hours
4. Truck departure time: 2018-08-14 10:00
5. Loading time cannot be spread across different days
