int ledpin = 8;
int val;

void setup() {
  pinMode(ledpin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  val = Serial.read();
  if(val == 'y'){
    digitalWrite(ledpin, HIGH);
    delay(70);
  }
  digitalWrite(ledpin, LOW);
}
