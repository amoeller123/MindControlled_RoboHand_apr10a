#include <Servo.h>
Servo myservo_thumb;
Servo myservo_index;
Servo myservo_middle;
Servo myservo_ring;
Servo myservo_pinkie;
char serialData;
boolean flag = false;

void setup() {
        Serial.begin(9600);       
        myservo_thumb.attach(11);
        myservo_index.attach(10);
        myservo_middle.attach(9);
        myservo_ring.attach(6);
        myservo_pinkie.attach(5);
}

void loop() {
//Servo start
          myservo_thumb.write(0);
          myservo_index.write(0);
          myservo_middle.write(0);
          myservo_ring.write(0);
          myservo_pinkie.write(0);
          
  if(Serial.available()) {
         serialData = Serial.read();
         
//Servos pointing two fingers
        if (serialData == 1) 
        {         
          myservo_thumb.write(0);
          myservo_index.write(0);
          myservo_middle.write(180);
          myservo_ring.write(180);
          myservo_pinkie.write(180);
          flag=true;
        }
        
//Servos pointing peace sign
        if (serialData == 2) 
        {         
          myservo_thumb.write(180);
          myservo_index.write(0);
          myservo_middle.write(0);
          myservo_ring.write(180);
          myservo_pinkie.write(180);
          flag=true;
        }
        
//Servos make a fist
        if (serialData == 3) 
        {         
          myservo_thumb.write(180);
          myservo_index.write(180);
          myservo_middle.write(180);
          myservo_ring.write(180);
          myservo_pinkie.write(180);
          flag=true;
        }
     if(flag)
        {
          delay(1000);
          flag=false;
        }
   }
}
 
