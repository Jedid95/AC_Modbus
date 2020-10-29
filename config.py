'''File with the settings of the different types of AC command controlled by Modbus'''

'''Maker: Schneider
   Model: TC903-3ADLMSA
   Link: https://www.se.com/ww/resources/sites/SCHNEIDER_ELECTRIC/content/live/FAQS/406000/FA406342/en_US/TC900%20Series%20Digital%20Fan%20Coil%20Thermostat%20Installation%20Sheet.pdf

   ******** Array with the positions given with pyModbusTCP
   Function Code 03/06
   Array_Position
   [0] Thermostat Mode              [16] Differential                   [32] Unoccupied mode, fan speed
   [1] Operation Mode               [17] Eco mode differential          [33] Temp. value from connection
   [2] Set-Point                    [18] Auto deadband                  [34] Temp. input
   [3] Fan Mode                     [19] Operation Mode configuration   [35] Heating mode KP
   [4] Heating set-point, upper lim [20] Auto Fan                       [36] Cooling mode KP
   [5] Cooling set-point, lower lim [21] Display temperature            [37] PID sampling time
   [6] ECO mode                     [22] Temperature Sensor             [38] KI
   [7] ECO mode, cooling set-point  [23] Modbus connection              [39] Span    
   [8] ECO mode, heating set-point  [24] Modbus address setting         [40] Heating valve 2, output voltage
   [9] Temperature compensation     [25] Modbus baud rate               [41] Cooling valve 1, output voltage
   [10] Setpoint, upper limmit      [26] Modbus parity check            [42] Lower-speed fan output voltage
   [11] Setpoint, lower limmit      [27] RTC clock display              [43] Medium-speed fan output voltage
   [12] Sleep Mode                  [28] 12/24-hour clock               [44] High-speed fan output voltage
   [13] Low Temperature protection  [29] Auxiliary input close/open
   [14] Fan operation after setting [30] Unoccupied mode, cooling setpoint
        temperature is reached      [31] Unoccupied mode, heating setpoint                     
   [15] Power-on state                            


   Function Code 04
   Array_Position
   [0] Actual room temperature
   '''