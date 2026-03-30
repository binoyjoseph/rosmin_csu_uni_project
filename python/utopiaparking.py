# This program calculates the paking fees in Utopia Parking
# variable to control the loop
option = 1

#begin while loop
while option != 3:
   # Display the Utopia parking menu
   print('Welcome to Utopia Parking ')
   print('Menu:')
   print('1:  View Rates')
   print('2:  Check-in and Check-out')
   print('3:  Exit\n')
   # get input from the useer
   option = int(input('>>Select an option:'))

   # processing user's inputs

   if option == 1:
      print(' \n Our rates are follows:' )
      print(' 0-1 hour  $19 \n 1-2 hour  $29  \n 2-3 hour  $79 \n 3-24 hour $89\n')
      input(' \n Press ENTER to return to the main menu:\n')
   elif option == 2:
      # getting check in time and check out time
      print('\nCheck in time')
      checkintime_hr = int(input('>> hour (0-23): '))
      if checkintime_hr > 23  or checkintime_hr < 0:
         print('Invalid input\n')
         break
      checkintime_min = int(input('>> minute (0-59):'))
      print('\nCheck out time')
      checkouttime_hr = int(input('>> hour (0-23): '))
      checkouttime_min = int(input('>> minute (0-59): '))
      #converting into minutes
      intime = checkintime_hr * 60 + checkintime_min
      outtime = checkouttime_hr * 60 + checkouttime_min
      if outtime < intime:
         print('\n Invalid check out time. Please try again\n')
      else:
         total_time_min = outtime - intime
         #converting minutes to hours
         hours = total_time_min // 60
         minutes = total_time_min % 60
        
         # calculating fee based on time
         if total_time_min >= 60 and total_time_min <= 120: 
            fees = 29
         elif total_time_min >= 120 and total_time_min <= 180:
            fees = 79
         elif total_time_min > 180:
            fees = 89
         print(f'Total parking time: {hours} hours and  {minutes} minutes')
         print(f'Total due: ${fees}')  

         # getting money from the user
         total_paid = 0
         balance_amt = fees
         # loop till balance amount is greater than 0
         while balance_amt > 0:
            collected = int(input('Insert cash amount (1, 2, 5, 10, 20, 50, 100 only):' ) )  
            total_paid = total_paid + collected
            print(f'Total collected: ${total_paid}') 
            
            if balance_amt > collected:
               balance_amt = balance_amt - collected
               print(f'Remaining balance: ${balance_amt}') 
            else:  
               print(f'Change due: ${collected - balance_amt}')
               balance_amt = balance_amt - collected
         # end while
         print('\nThanks for parking with us!\n')
      # end else
   #end option 2
   elif option == 3:
      print('\n Thank you for using Utopia Parking!')
   else:
      print('Invalid input\n')
#end while loop