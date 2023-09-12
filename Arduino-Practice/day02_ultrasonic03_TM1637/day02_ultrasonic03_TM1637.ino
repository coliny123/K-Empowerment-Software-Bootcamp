
#include <TM1637Display.h>
#define CLK 2
#define DIO 3

TM1637Display dsp(CLK, DIO); // TM1637Display 객체 dsp 생성

uint8_t dist[4]={ 0x0, 0x0, 0x0, 0x0 };

int trigPin = 13;
int echoPin = 12;

long duration;
int distance;

void setup() {
  Serial.begin(9600);
  dsp.setBrightness(7);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  dsp.setSegments(dist);
}

void loop() {
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10); // 10us
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.017;  

  if(isPrime(distance)){
    Serial.print("Distance : ");
    Serial.print(distance);
    Serial.println("cm");  
    dsp.showNumberDec(distance);   
  } else {
    dist[0] = 0x0; 
    dist[1] = 0x0;
    dist[2] = 0b01010100;
    dist[3] = 0b01011100;
    dsp.setSegments(dist);
    Serial.print("no\n");
  }
  delay(1000);
}

bool isPrime(int number){
      if(number <= 1)
          return false;
      else {
          for(int i = 2; i < number; i++)
              if (number % i == 0)  // 약수가 발견되면
                  return false;
      }
      return true;  // 소수. 1이하의 수도 아니고 1과 자기자신을 제외한 약수도 발견되지 않음
}