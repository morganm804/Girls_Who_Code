void setup() {
pinMode(5, INPUT);
pinMode(9, OUTPUT);
int light = digitalRead(5);
}

void loop() {
while(light>5);
  pinMode(9,HIGH);
}

