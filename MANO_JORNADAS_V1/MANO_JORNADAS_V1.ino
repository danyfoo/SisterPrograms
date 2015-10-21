#include <Servo.h>

Servo myServoA;
Servo myServoB;
Servo myServoC;
Servo myServoD;
Servo myServoE;

const int izqMaximo = 500;  //VAlor Maximo de lectura
const int derMinimo = 0;    //VAlor Minimo de lectura
const int pinLectura = A1;  //Pin de Lectura por Defecto Analogico para 

long signalReal, posicionRelativa;

void setup() {
  myServoA.attach(5);
  myServoB.attach(6);
  myServoC.attach(9);
  myServoD.attach(10);
  myServoE.attach(11);
    
  Serial.begin(9600);
}

void loop() {
  
  int sensorValue = analogRead(pinLectura);
  
  /*****  ESTO VA CAMBIAR ****/
  float voltaje = sensorValue * (5.0 / 1023.0);
  signalReal = voltaje * 100;
  /*****  ESTO VA CAMBIAR ****/
    
  moverServos(signalReal);  //Llama a la funcion para mover los servos en relacion a la lectura de los ojos
  delay(15);
}

void moverServos(long posicionReal){
  posicionRelativa = map(posicionReal,derMinimo,izqMaximo,0,180);  //Devuelve un valor proporcional al rango que se desea mover
  Serial.println(posicionRelativa);
  
  myServoA.write(posicionRelativa);
  myServoB.write(posicionRelativa);
  myServoC.write(posicionRelativa);
  myServoD.write(posicionRelativa);
  myServoE.write(posicionRelativa);
}
