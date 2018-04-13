#define LED 2

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  //Serial.println("Init arduino");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    //Serial.println("recibiendo datos!!");
    char Bytes = Serial.read();
    switch(Bytes){
      case ('A'):
        //Serial.println("Led on");
        digitalWrite(LED,HIGH);
        break;
      case ('B'):
        //Serial.println("Led off");
        digitalWrite(LED,LOW);
        break;
      case ('C'):
        int Sen = analogRead(A0);
        Serial.println(Sen);    
    }
  }
}
