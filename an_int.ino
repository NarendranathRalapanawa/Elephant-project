
#include <TimerOne.h>
volatile int sesv;
int n =0;
int sesv_arr[50];
bool printst=false;// to find the state of data transmitte
bool datast=false;// to find the the state of datacollecting
int a=0;
void setup () {
 pinMode (A0, INPUT_PULLUP);
 Timer1.initialize(5000);
 Timer1.attachInterrupt(function);
 Serial.begin(9600);
}

void function () {
 sesv = analogRead(0);
 //Serial.println(n);
 //Serial.println(datast);
 if(sesv>100){
  datast=true;
 // Serial.println("can be elephant");
 }

 if(datast && n<50){
  printst=false;
  sesv_arr[n]=sesv;
  n=n+1;
 }

 else if (n==50){
  printst=true;
  datast=false;

}
}

void loop () {
  if(printst){
      
  for(int i = 0; i <  sizeof(sesv_arr); i++)
{
  Serial.println(sesv_arr[i]);
}
Serial.println(n);
n=0;
printst=0;

 
  }
}

