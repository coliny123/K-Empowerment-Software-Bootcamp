int sensor = A1;                             // 조도센서
int led_red    = D2;                        // 빨강 LED
int led_blue   = D3;                        // 파랑 LED
int led_green  = D4;                        // 초록 LED
int led_yellow = D5;                        // 노랑 LED


void setup() {
  Serial.begin(115200);                      // 통신속도
  pinMode(led_red,OUTPUT);                  // 핀 모드 설정
  pinMode(led_blue,OUTPUT);                 // 핀 모드 설정
  pinMode(led_green,OUTPUT);                // 핀 모드 설정
  pinMode(led_yellow,OUTPUT);               // 핀 모드 설정
}


void loop() {
  int sensor_result = analogRead(sensor);    // 센서가 측정한 값 저장
  Serial.println(sensor_result);             // 센서가 측정한 값 시리얼 모니터에 출력
  
  digitalWrite(led_red,LOW);
  digitalWrite(led_blue,LOW);
  digitalWrite(led_green,LOW);
  digitalWrite(led_yellow,LOW);

    if(sensor_result<2000){                   // 센서 측정값이 2000미만 이라면 빨강 LED 켜기
    digitalWrite(led_red,HIGH);
  }
 
  if(sensor_result<1500){                   // 센서 측정값이 1500미만 이라면 파랑 LED 켜기
    digitalWrite(led_blue,HIGH);
  }
  
  if(sensor_result<1000){                   // 센서 측정값이 1000미만 이라면 초록 LED 켜기
    digitalWrite(led_green,HIGH);
  }
  
  if(sensor_result<500){                    // 센서 측정값이 500미만 이라면 노랑 LED 켜기
    digitalWrite(led_yellow,HIGH);
  }

}