
#include <TimerOne.h>
volatile int sesv;


void setup () {
 pinMode (A0, INPUT_PULLUP);
 Timer1.initialize(2000);
 Timer1.attachInterrupt(function);
 Serial.begin(9600);
}

void function () {
 sesv = analogRead(0);
 if(sesv>30){
 Serial.println(sesv);
}
}

void loop () {
 Serial.println("I am delaying");
 delay(10000);
}
