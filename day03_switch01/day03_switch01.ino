int trigPin = D9;
int echoPin = D8;

long duration;
int distance;
int red_led = D2;
int green_led = D4;
int cnt = 0;

void setup() {
  Serial.begin(115200);   // ET보드의 시리얼 통신 속도
  pinMode(trigPin, OUTPUT);   // 초음파 출력 트리거
  pinMode(echoPin, INPUT);    // 초음파 입력
  pinMode(red_led, OUTPUT);
  pinMode(green_led, OUTPUT);
  
}

void loop() {
  // 데이터 시트에 있는 규격대로 조작
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10); // 10us
  digitalWrite(trigPin, LOW);
  // Sonic wave 8 times

  duration = pulseIn(echoPin, HIGH);  // Receive sonic wave
  distance = duration * 0.017;    // convert to cm
  Serial.print("Distance : ");
  Serial.print(distance);
  Serial.println("cm");  
  delay(500);

  if(distance < 5){
    digitalWrite(green_led, LOW);
    digitalWrite(red_led, HIGH);
    cnt++;
    Serial.printf("드럼통 갯수 : %d\n", cnt);
  }else{
    digitalWrite(green_led, HIGH);
    digitalWrite(red_led, LOW);
  }
}
