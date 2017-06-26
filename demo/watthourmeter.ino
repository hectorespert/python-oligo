#include <CmdMessenger.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

CmdMessenger c = CmdMessenger(Serial);

enum {
  watt,
};

void on_watt(void){
  lcd.clear();
  double value = c.readBinArg<double>();
  lcd.print("Wh ");
  lcd.print(value);
}

void setup() {
  lcd.begin(16, 2);
  
  Serial.begin(9600);
  c.attach(watt, on_watt);
  
  delay(500);
  lcd.clear();
}

void loop() {
  c.feedinSerialData();
}

