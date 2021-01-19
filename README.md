# face detection + servo control
### Note
I didn't manage to get RabbitMQ working unfortunately. It is already installed on the Raspberry Pi (although an older version due to some dependency issues). The code and some info (Pinout Diagram) can be found on the Desktop of the Pi.
### Info
* `face_detection_arduino.ipynb` contains the face detection + arduino serial communication code in Python. Packages needed:
  * OpenCV
  * numpy
  * serial
* `servo.py` contains the code for controlling the servo that is run on the Raspberry Pi
  * The `angle` to `duty` conversion isn't calibrated. Duty only goes from 0.0 to 100.0, but doesn't seem to cover the whole 180 degrees, which can be achieved on the Arduino. I tried looking for the datasheet but couldn't find any.
  * You might want to look up Raspberry Pi PWM, duty cycles and servo control to understand this.
* `pythonservo.ino` file contains the script that needs to be loaded onto the Arduino
  * probably won't be using this, as Arduino servo updates very slowly
