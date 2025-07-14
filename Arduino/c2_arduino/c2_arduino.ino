int ledPin = 13;
String command = "";

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {

  int valueA = random(-100, 101);
  float valueB = random(-100, 101) / 100.0;
  int valueC = analogRead(A0);
  String valueD = "Test_Input";

  Serial.print("A:");
  Serial.println(valueA);

  Serial.print("B:");
  Serial.println(valueB);

  Serial.print("C:");
  Serial.println(valueC);

  Serial.print("D:");
  Serial.println(valueD);

  if (Serial.available() > 0) {
    command = Serial.readStringUntil('\n');
    command.trim();
    if (command == "ON") {
      digitalWrite(ledPin, HIGH);
    } else if (command == "OFF") {
      digitalWrite(ledPin, LOW);
    }
  }

  delay(1000);
}
